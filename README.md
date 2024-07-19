python fastapi 快速开发框架

### 1.简介
这是一个简单的，python-web项目。主要用于可快速开发pyhonweb项目。


### 2.食用方法

```
环境要求： python3.10以上版本

部署教程：
1. 拷贝项目到目标目录
2. 在项目根目录下执行 'pip install -r requirements.txt'
3. 新增数据库并将sql在库中初始化
4. 修改项目`.evn` 配置文件
5. 安装完成后，在项目根目录下执行 'nohup uvicorn app.main:app --host=0.0.0.0 --port=8000  --reload &' 启动服务
6. 停止服务通过查询端口, kill -9 停止

启动命令
uvicorn app.main:app --host=0.0.0.0 --port=8000 --reload

```


### 3. 备注说明

- 请求url时，需要携带指定header: `token:fake-super-secret-token`
- 修改orm模块下的数据库连接地址, 目前只支持mysql
- fastapi官网: https://fastapi.tiangolo.com/tutorial/sql-databases/
- SQLAlchemy ORM:  https://docs.sqlalchemy.org/en/20/orm/
- 接口文档访问地址： http://127.0.0.1:8000/docs
- 可以使用 pyarmor 对代码进行混肴
    1. 执行 `pip install pyarmor`
    2. 执行命令 `pyarmor g .` 生成混肴代码


### 4. 目录结构
```bat
D:.
└─fastapi-demo
    │  .env                                         # 项目配置文件, 使用configuration.py读取
    │  .gitignore
    │  fastapi_demo.sql                             # 数据库文件, 记得导入数据时
    │  readme.md
    │  requirements.txt
    ├─app
    │  │  configuration.py                          # 配置文件映射实体
    │  │  dependencies.py                           # 一些公共依赖函数
    │  │  main.py                                   # 启动类
    │  │  scheduleService.py                        # 计划调度任务参考实现
    │  │  __init__.py
    │  │
    │  ├─controller                                 # 接口定义目录
    │  │  │  consoleController.py
    │  │  │  userController.py
    │  │  │  __init__.py
    │  │  │
    │  │  ├─models
    │  │  │  │  models.py
    │  ├─orm                                        # orm 定义
    │  │  │  schemas.py
    │  │  │  __init__.py
    │  ├─service                                    # 公用service接口
    │  │  │  KVService.py
    │  │  │  __init__.py
    │  ├─static                                     # 静态文件放这个目录就可以http直接访问,访问路径:/static/test.json
    │  │      test.json
    └─logs                                          # 日志目录
            mylog.log
```


### 5. 版本记录

V0.0.3
1. 新增使用mysql实现kv访问操作


V0.0.2
1. 新增日志框架，存放日志
2. 配置日志打印格式
3. 新增支持配置文件

V0.0.1
1. 搭建一个简单的fastapi-demo 项目
2. 支持http接口请求，文件分目录存放
3. 支持请求参数校验
4. 支持mysql数据库