# Project Name
小型动物识别科普网站

## 项目说明
### 什么是小型动物识别科普网站？

小型动物识别科普网站是一个利用计算机视觉技术及 Web 开发技术，
旨在提供关于小型动物生态系统、生物多样性、环境保护等方面的知识，帮助大家认识身边的小型动物。
这个系统能够有效地传达生态环境的复杂性和对人类生活的重要性。

## 安装项目
### 后端
```bash
# clone 项目
git https://github.com/www-light/COD.git
# 切换目录
cd COD
# 安装依赖
pip3 install -r ./requirements.txt
# 更新数据库
python manage.py migrate
# 运行后端（dev or Production）
python manage.py runserver
``` 

### 前端
```bash
# 切换目录
cd COD
cd app_front
# 安装依赖
npm install
# 运行前端（dev）
npm run serve
...
```

## 运行环境
python + Node.js

## 项目结构

Django + vue

## 分支说明
- main: 主分支，用于发布版本

不能直接push，只能接受其他分支的PR

- service-core: 后端分支，用于开发后端

可以直接push

- app-front: 前端分支，用于开发前端

可以直接push
