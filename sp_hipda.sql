-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2016-10-06 14:24:16
-- 服务器版本： 5.5.52-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sp_hipda`
--
CREATE DATABASE IF NOT EXISTS `sp_hipda` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `sp_hipda`;

-- --------------------------------------------------------

--
-- 表的结构 `nowproc`
--

DROP TABLE IF EXISTS `nowproc`;
CREATE TABLE IF NOT EXISTS `nowproc` (
  `prockey` varchar(5) CHARACTER SET utf8 NOT NULL,
  `procvalue` int(10) NOT NULL,
  UNIQUE KEY `proc` (`prockey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='过程记录表';

--
-- 转存表中的数据 `nowproc`
--

INSERT INTO `nowproc` (`prockey`, `procvalue`) VALUES
('page', 1),
('tid', 1);

-- --------------------------------------------------------

--
-- 表的结构 `tlist`
--

DROP TABLE IF EXISTS `tlist`;
CREATE TABLE IF NOT EXISTS `tlist` (
  `tid` int(6) NOT NULL COMMENT '帖子id',
  `head` varchar(60) CHARACTER SET utf8 NOT NULL COMMENT '标题',
  `uid` int(6) NOT NULL COMMENT '作者id',
  `uname` varchar(20) CHARACTER SET utf8 NOT NULL COMMENT '作者名字',
  `repcnt` int(8) NOT NULL COMMENT '回复数',
  `readcnt` int(8) NOT NULL COMMENT '阅读数',
  `ctime` varchar(20) NOT NULL COMMENT '发帖时间',
  `rtime` varchar(20) NOT NULL COMMENT '最后回帖时间',
  `sptime` int(8) NOT NULL COMMENT '抓取时间',
  `page` int(10) NOT NULL DEFAULT '1',
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
