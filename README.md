python fastapi 快速开发框架


请求url时，需要携带指定header: `token:fake-super-secret-token`

修改orm模块下的数据库连接地址, 目前只支持mysql


fastapi官网: https://fastapi.tiangolo.com/tutorial/sql-databases/

SQLAlchemy ORM:  https://docs.sqlalchemy.org/en/20/orm/

接口文档访问地址： http://127.0.0.1:8000/docs

项目启动命令:
```
环境要求： python3.10以上版本

部署教程：
1. 拷贝项目到目标目录
2. 在项目根目录下执行 'pip install -r requirements.txt'
3. 新增数据库并将sql在库中初始化
4. 修改项目`.evn` 配置文件
5. 安装完成后，在项目根目录下执行 'nohup uvicorn app.main:app --port=8000 --reload &' 启动服务
6. 停止服务通过查询端口, kill -9 停止


启动命令
uvicorn app.main:app --port=8000 --reload

```

数据库脚本:

```sql
/*
 Navicat MySQL Data Transfer

 Source Server         : MyTest47.109.108.16
 Source Server Type    : MySQL
 Source Server Version : 80200
 Source Host           : 47.109.108.16:7501
 Source Schema         : fastapi_demo

 Target Server Type    : MySQL
 Target Server Version : 80200
 File Encoding         : 65001

 Date: 09/07/2024 09:59:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` int(0) NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user`(`id`, `name`, `status`, `create_time`, `update_time`) VALUES (1, '123', 1, '2024-07-10 10:04:00', '2024-07-10 10:04:02');
INSERT INTO `t_user`(`id`, `name`, `status`, `create_time`, `update_time`) VALUES (2, '123', 1, '2024-07-10 10:04:07', '2024-07-10 10:04:09');


-- ----------------------------
-- Table structure for t_user_addresss
-- ----------------------------
DROP TABLE IF EXISTS `t_user_addresss`;
CREATE TABLE `t_user_addresss`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;


```



备注:

可以使用 pyarmor 对代码进行混肴

1. 执行 `pip install pyarmor`
2. 执行命令 `pyarmor g .` 生成混肴代码









2. 目录结构
```bat
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
```