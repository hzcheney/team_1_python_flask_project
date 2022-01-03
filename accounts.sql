/*
 Navicat Premium Data Transfer

 Source Server         : demo
 Source Server Type    : MySQL
 Source Server Version : 50736
 Source Host           : localhost:3306
 Source Schema         : demo

 Target Server Type    : MySQL
 Target Server Version : 50736
 File Encoding         : 65001

 Date: 03/01/2022 14:33:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP DATABASE IF EXISTS demo;

CREATE DATABASE demo CHARACTER SET utf8mb4;

USE demo;
-- ----------------------------
-- Table structure for accounts
-- ----------------------------
DROP TABLE IF EXISTS `accounts`;
CREATE TABLE `accounts`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of accounts
-- ----------------------------
INSERT INTO `accounts` VALUES (4, 'Odette Gray', '6', 'erat.in@icloud.net', 0);
INSERT INTO `accounts` VALUES (5, 'Leslie Brady', '4', 'quis.diam@google.ca', 1);
INSERT INTO `accounts` VALUES (6, 'Fletcher Frye', '7', 'quisque@hotmail.ca', 0);
INSERT INTO `accounts` VALUES (8, 'Valentine Estrada', '221122', 'vel.lectus.cum@icloud.edu', 1);
INSERT INTO `accounts` VALUES (9, 'Marshall Walker', '5', 'consequat.nec.mollis@outlook.org', 0);
INSERT INTO `accounts` VALUES (11, 'Brendan Jackson', '2', 'vulputate@google.ca', 0);
INSERT INTO `accounts` VALUES (12, 'Arden Summers', '2', 'nullam@hotmail.org', 0);
INSERT INTO `accounts` VALUES (14, 'test111', 'test111', 'test111@test111.com', 0);
INSERT INTO `accounts` VALUES (15, 'testtest', 'testtest', 'test@test.com', 0);
INSERT INTO `accounts` VALUES (17, 'admin', 'admin', 'chenhan199781@gmail.com', 1);
INSERT INTO `accounts` VALUES (18, 'adass', '123', 'chenhan199781@gmail.com', 1);
INSERT INTO `accounts` VALUES (20, 'testt', 'testt', 'a@a.com', 0);

SET FOREIGN_KEY_CHECKS = 1;
