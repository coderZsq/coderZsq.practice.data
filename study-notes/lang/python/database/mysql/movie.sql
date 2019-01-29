/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost
 Source Database       : movie

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : utf-8

 Date: 08/17/2018 10:57:53 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `top250`
-- ----------------------------
DROP TABLE IF EXISTS `top250`;
CREATE TABLE `top250` (
  `title` varchar(100) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `rate` varchar(20) DEFAULT NULL,
  `url` varchar(100) NOT NULL,
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
