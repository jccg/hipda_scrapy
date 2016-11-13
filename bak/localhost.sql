-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2016-11-06 16:16:04
-- 服务器版本： 5.5.53-0ubuntu0.14.04.1
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
CREATE TABLE `nowproc` (
  `prockey` varchar(5) CHARACTER SET utf8 NOT NULL,
  `procvalue` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='过程记录表';

-- --------------------------------------------------------

--
-- 表的结构 `tlist`
--

DROP TABLE IF EXISTS `tlist`;
CREATE TABLE `tlist` (
  `tid` int(6) NOT NULL COMMENT '帖子id',
  `head` varchar(60) CHARACTER SET utf8 NOT NULL COMMENT '标题',
  `uid` int(6) NOT NULL COMMENT '作者id',
  `uname` varchar(20) CHARACTER SET utf8 NOT NULL COMMENT '作者名字',
  `repcnt` int(8) NOT NULL COMMENT '回复数',
  `readcnt` int(8) NOT NULL COMMENT '阅读数',
  `ctime` varchar(20) NOT NULL COMMENT '发帖时间',
  `rtime` varchar(20) NOT NULL COMMENT '最后回帖时间',
  `sptime` int(8) NOT NULL COMMENT '抓取时间',
  `page` int(10) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `nowproc`
--
ALTER TABLE `nowproc`
  ADD UNIQUE KEY `proc` (`prockey`);

--
-- Indexes for table `tlist`
--
ALTER TABLE `tlist`
  ADD PRIMARY KEY (`tid`),
  ADD KEY `sptime` (`sptime`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
