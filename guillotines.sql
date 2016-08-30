/*
Navicat MySQL Data Transfer

Source Server         : mydb
Source Server Version : 50540
Source Host           : localhost:3306
Source Database       : guillotines

Target Server Type    : MYSQL
Target Server Version : 50540
File Encoding         : 65001

Date: 2016-08-30 14:19:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `gu_shelldbconf`
-- ----------------------------
DROP TABLE IF EXISTS `gu_shelldbconf`;
CREATE TABLE `gu_shelldbconf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` varchar(128) NOT NULL DEFAULT '127.0.0.1' COMMENT 'ipv4和ipv6',
  `port` varchar(5) DEFAULT '3306' COMMENT '端口号',
  `password` varchar(32) NOT NULL DEFAULT 'root' COMMENT '数据库密码',
  `create_time` timestamp NOT NULL DEFAULT '2016-07-20 23:30:27' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='websehll数据库配置信息';

-- ----------------------------
-- Records of gu_shelldbconf
-- ----------------------------

-- ----------------------------
-- Table structure for `gu_users`
-- ----------------------------
DROP TABLE IF EXISTS `gu_users`;
CREATE TABLE `gu_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '用户名',
  `email` varchar(100) NOT NULL COMMENT '邮箱',
  `password` varchar(32) NOT NULL COMMENT '密码',
  `salt` varchar(10) NOT NULL,
  `utype` varchar(10) NOT NULL DEFAULT 'user' COMMENT '用户类型',
  `create_time` timestamp NOT NULL DEFAULT '2016-07-20 21:35:31' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表';

-- ----------------------------
-- Records of gu_users
-- ----------------------------

-- ----------------------------
-- Table structure for `gu_webshell`
-- ----------------------------
DROP TABLE IF EXISTS `gu_webshell`;
CREATE TABLE `gu_webshell` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `password` varchar(32) NOT NULL,
  `ip` varchar(128) NOT NULL COMMENT 'IP地址',
  `ip_address` varchar(255) NOT NULL COMMENT '归属地',
  `category` varchar(6) NOT NULL COMMENT 'shell类型',
  `create_time` timestamp NOT NULL DEFAULT '2016-07-20 22:52:47' ON UPDATE CURRENT_TIMESTAMP,
  `httpcode` varchar(3) DEFAULT NULL COMMENT '状态码',
  `br` int(1) DEFAULT NULL COMMENT '权重',
  `pr` int(1) DEFAULT NULL COMMENT 'PR',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gu_webshell
-- ----------------------------
