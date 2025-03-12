# 项目名称
本项目是一个前后端分离的应用，前端基于Vue 3构建用户界面，后端基于Django处理业务逻辑和提供API。
可用于生成多设备适配在线作品集，并可在编辑过程中预览不同设备显示效果。

## 项目图片
### 首页
![首页](https://img.picui.cn/free/2025/03/12/67d0e998135bb.png)

### 编辑器
![PC端效果](https://img.picui.cn/free/2025/03/12/67d0e99a53ed3.png)
![移动端效果](https://img.picui.cn/free/2025/03/12/67d0e999715b3.png)

### 多种模版开发中 >> 未来加入简历模版，支持简历PDF生成 
![部分模版列表](https://img.picui.cn/free/2025/03/12/67d0e99a373d0.png)

## 项目架构
### 前端（`frontend/src`）
- **`App.vue`**：Vue应用的根组件，承载整个页面布局。
- **`assets`**：存储静态资源，如图片、样式表等。
- **`components`**：可复用的Vue组件，方便代码维护与扩展。
- **`main.js`**：应用的入口文件，初始化Vue实例并配置全局设置。
- **`plugins`**：存放项目中使用的各类插件。
- **`router`**：管理前端路由，实现页面的切换与导航。
- **`stores`**：状态管理相关代码，用于统一管理应用状态。
- **`utils`**：工具函数集合，提高代码复用性。
- **`views`**：页面级的视图组件，对应不同的路由页面。

### 后端（`backend`）
基于Django框架开发，包含配置文件、路由定义以及业务逻辑相关的应用模块。

## 环境配置
### 前端
- **Node.js**：建议使用14及以上版本。
- **包管理器**：`npm`或`yarn`。

### 后端
- **Python**：推荐使用3.8及以上版本。
- **Django**：3.2及以上版本。

## 快速开始
### 前端
1. 进入`frontend`目录：`cd frontend`
2. 安装依赖：`npm install` 或 `yarn install`
3. 启动开发服务器：`npm run serve` 或 `yarn serve`
4. 在浏览器中访问 `http://localhost:8080` 查看应用。

### 后端
1. 进入`backend`目录：`cd backend`
2. 创建并激活虚拟环境（推荐操作）。
3. 安装依赖：`pip install -r requirements.txt`
4. 执行数据库迁移：`python manage.py migrate`
5. 启动服务器：`python manage.py runserver`
6. 后端API默认在 `http://localhost:8000` 可访问。

## 参与贡献
欢迎大家提交PR来改进项目，提交前请确保代码格式规范，并且通过必要的测试。

## 问题反馈
若在使用过程中遇到任何问题，或者有好的建议，欢迎在 [issues](https://github.com/你的仓库地址/issues) 中反馈。 



