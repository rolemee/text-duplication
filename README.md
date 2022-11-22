# text-duplication


## 1.安装包
```
pip install -r requirements.txt
npm install pnpm
```
## 2.环境依赖
**mysql >8.0**

**python=3.10.0**

**nodejs >=14.18.0**

## 3.使用说明
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
# vite.config.js  
server {
    host: '服务器ip',
    port: '端口号'
}
```

二、 项目说明

- 前端采用 Vue3 版本框架代码；采用element-ui 主题
- 采用Rute路由跳转实现网页切换
- 采用Vite手脚架进行服务器，插件搭建

### 后端部署说明文档

```shell
python app/app.py
```