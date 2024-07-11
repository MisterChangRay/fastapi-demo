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

 Date: 11/07/2024 14:05:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_keyvalue
-- ----------------------------
DROP TABLE IF EXISTS `t_keyvalue`;
CREATE TABLE `t_keyvalue`  (
  `key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `value` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  `expire_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`key`) USING BTREE,
  INDEX `expire_time`(`expire_time`) USING BTREE,
  UNIQUE INDEX `key`(`key`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES (1, NULL, 1, NULL, NULL);
INSERT INTO `t_user` VALUES (2, NULL, 2, NULL, NULL);
INSERT INTO `t_user` VALUES (4, '123', 1, '2024-07-10 10:04:00', '2024-07-10 10:04:02');
INSERT INTO `t_user` VALUES (5, '123', 1, '2024-07-10 10:04:07', '2024-07-10 10:04:09');
INSERT INTO `t_user` VALUES (6, '123', 0, NULL, NULL);
INSERT INTO `t_user` VALUES (7, '123', 0, NULL, NULL);
INSERT INTO `t_user` VALUES (8, '123', 0, NULL, NULL);
INSERT INTO `t_user` VALUES (9, '123', 0, NULL, NULL);
INSERT INTO `t_user` VALUES (10, '123', 0, NULL, NULL);
INSERT INTO `t_user` VALUES (11, '123', 0, NULL, NULL);
INSERT INTO `t_user` VALUES (12, '123', 0, NULL, NULL);
INSERT INTO `t_user` VALUES (13, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (14, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (15, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (16, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (17, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (18, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (19, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (20, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (21, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (22, '321', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (23, '123', 1, NULL, NULL);
INSERT INTO `t_user` VALUES (24, '123', 1, NULL, NULL);

SET FOREIGN_KEY_CHECKS = 1;
