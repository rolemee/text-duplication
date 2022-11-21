### 前端部署说明文档

一、	使用准备

- [下载Node.js版本需&gt;=14.18.0]: https://nodejs.org/zh-cn/download/

- 安装环境包

```
# 安装环境
pnpm install

# 如果安装错误 先删除node_modules包,执行下面操作在重新安装
pnpm config set registry https://registry.npmmirror.com/ # 切换为国内镜像源
```

- 运行

```
pnpm run dev
```

- 部署到服务器

```
# vite.config.js  server host
```

二、 项目说明

- 前端采用 Vue3 版本框架代码；采用element-ui 主题
- 采用Rute路由跳转实现网页切换
- 采用Vite手脚架进行服务器，插件搭建