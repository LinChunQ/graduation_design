/*
 Navicat Premium Data Transfer

 Source Server         : Practice
 Source Server Type    : MySQL
 Source Server Version : 50744
 Source Host           : localhost:3306
 Source Schema         : uga-flask

 Target Server Type    : MySQL
 Target Server Version : 50744
 File Encoding         : 65001

 Date: 03/03/2025 21:45:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `age` int(11) NULL DEFAULT NULL,
  `email` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `school` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `profession` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password_hash` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`teacher_id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  UNIQUE INDEX `sex`(`sex`) USING BTREE,
  UNIQUE INDEX `age`(`age`) USING BTREE,
  UNIQUE INDEX `phone`(`phone`) USING BTREE,
  UNIQUE INDEX `address`(`address`) USING BTREE,
  UNIQUE INDEX `school`(`school`) USING BTREE,
  UNIQUE INDEX `profession`(`profession`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, '小明', '男', 18, '小明@163.com', '15037626907', NULL, '湖州学院', '计算机科学与技术', 'scrypt:32768:8:1$LIE8cAgaQTnoSK0y$46c63f249dfaac2b1e1ec15d0c6d333e02389a92d003b300c2553b559a98a11e5fc57f499c715d4f2070db380454e6452b6707dd147fd59171960485200ed5de');

SET FOREIGN_KEY_CHECKS = 1;
