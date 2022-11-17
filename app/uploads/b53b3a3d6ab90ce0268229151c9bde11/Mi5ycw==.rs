pub mod api;
pub mod errors;
pub mod handle;
pub mod jwt;
pub mod static_server;

use clap::Parser;
use std::path::PathBuf;
use tracing_subscriber::{
    filter::filter_fn, prelude::__tracing_subscriber_SubscriberExt, util::SubscriberInitExt, Layer,
};
#[derive(Parser)]
#[command(version)]
pub struct Config {
    #[arg(long, default_value = "postgresql://localhost:5432/QADiscuz")]
    pub db: String,
    #[arg(short, long, default_value_t = 100)]
    pub db_connection: u32,
    #[arg(short, long, default_value_t = 0)]
    pub thread: usize,
    #[arg(short, long, default_value = "./out")]
    pub static_path: PathBuf,
    #[arg(short, long, default_value_t = 3001)]
    pub port: u16,
}
fn main() -> Result<(), anyhow::Error> {
    // tracing_subscriber::registry().with(fmt::layer()).init();
    let stdout_filter = tracing_subscriber::fmt::layer().with_filter(filter_fn(|metadata| {
        #[cfg(debug_assertions)]
        {
            metadata.target().starts_with("qaweb::")
                || metadata.target().starts_with("jwt::")
                || metadata.target().starts_with("login::")
                || metadata.target().starts_with("api::")
        }
        #[cfg(not(debug_assertions))]
        {
            metadata.target().starts_with("qaweb::") && metadata.level() <= &tracing::Level::INFO
        }
    }));
    tracing_subscriber::registry().with(stdout_filter).init();
    let config = Config::parse();
    let mut builder = tokio::runtime::Builder::new_multi_thread();
    builder.enable_all();
    if config.thread != 0 {
        builder.worker_threads(config.thread);
    }
    builder.build()?.block_on(api::server(&config)).ok();
    Ok(())
}