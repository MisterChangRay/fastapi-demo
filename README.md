python fastapi 快速开发框架


fastapi官网: https://fastapi.tiangolo.com/tutorial/sql-databases/
SQLAlchemy ORM:  https://docs.sqlalchemy.org/en/20/orm/


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
INSERT INTO `t_user` VALUES (1, NULL, NULL, NULL, NULL);
INSERT INTO `t_user` VALUES (2, NULL, NULL, NULL, NULL);
INSERT INTO `t_user` VALUES (3, '123', NULL, NULL, NULL);

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








2. 目录结构
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