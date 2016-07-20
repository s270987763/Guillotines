/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50549
Source Host           : localhost:3306
Source Database       : guillotines

Target Server Type    : MYSQL
Target Server Version : 50549
File Encoding         : 65001

Date: 2016-07-20 23:31:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for gu_shelldbconf
-- ----------------------------
DROP TABLE IF EXISTS `gu_shelldbconf`;
CREATE TABLE `gu_shelldbconf` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `host` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `port` varchar(5) NOT NULL DEFAULT '3306',
  `create_time` timestamp NOT NULL DEFAULT '2016-07-20 23:30:27' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gu_shelldbconf
-- ----------------------------

-- ----------------------------
-- Table structure for gu_user
-- ----------------------------
DROP TABLE IF EXISTS `gu_user`;
CREATE TABLE `gu_user` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `salt` varchar(10) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT '2016-07-20 21:35:31' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gu_user
-- ----------------------------

-- ----------------------------
-- Table structure for gu_webshell
-- ----------------------------
DROP TABLE IF EXISTS `gu_webshell`;
CREATE TABLE `gu_webshell` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `ip` varchar(20) NOT NULL,
  `ip_address` varchar(255) NOT NULL,
  `category` varchar(6) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT '2016-07-20 22:52:47' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gu_webshell
-- ----------------------------
SET FOREIGN_KEY_CHECKS=1;
