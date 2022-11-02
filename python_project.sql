-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2022-11-02 19:27:27
-- 服务器版本： 8.0.12
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `python_project`
--

-- --------------------------------------------------------

--
-- 表的结构 `homework`
--

CREATE TABLE `homework` (
  `homeworkId` int(11) UNSIGNED NOT NULL,
  `usernameId` int(11) UNSIGNED NOT NULL,
  `homeworkName` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `homeworkDescribe` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `start_time` datetime NOT NULL,
  `stop_time` datetime NOT NULL,
  `similarity` json DEFAULT NULL,
  `homework_type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 表的结构 `rights`
--

CREATE TABLE `rights` (
  `rights` int(20) UNSIGNED NOT NULL,
  `describe` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `rights`
--

INSERT INTO `rights` (`rights`, `describe`) VALUES
(0, 'teacher'),
(1, '学生');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `usernameId` int(20) UNSIGNED NOT NULL,
  `name` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `nickname` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `rights` int(20) UNSIGNED NOT NULL,
  `avatar` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`usernameId`, `name`, `nickname`, `password`, `rights`, `avatar`) VALUES
(1, 'jrm', 'rolemee', '1234', 0, NULL),
(2, 'wsc', 'tbao', '1234', 1, NULL),
(3, 'yyj', 'future', '1234', 1, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `user_homework`
--

CREATE TABLE `user_homework` (
  `usernameId` int(11) UNSIGNED NOT NULL,
  `homeworkId` int(11) UNSIGNED NOT NULL,
  `is_Finish` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转储表的索引
--

--
-- 表的索引 `homework`
--
ALTER TABLE `homework`
  ADD PRIMARY KEY (`homeworkId`),
  ADD KEY `homework_user_usernameId_fk` (`usernameId`);

--
-- 表的索引 `rights`
--
ALTER TABLE `rights`
  ADD PRIMARY KEY (`rights`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`usernameId`),
  ADD KEY `user_rights_rights_fk` (`rights`);

--
-- 表的索引 `user_homework`
--
ALTER TABLE `user_homework`
  ADD PRIMARY KEY (`usernameId`,`homeworkId`),
  ADD KEY `user_homework_homework_homeworkId_fk` (`homeworkId`);

--
-- 限制导出的表
--

--
-- 限制表 `homework`
--
ALTER TABLE `homework`
  ADD CONSTRAINT `homework_user_usernameId_fk` FOREIGN KEY (`usernameId`) REFERENCES `user` (`usernameid`);

--
-- 限制表 `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_rights_rights_fk` FOREIGN KEY (`rights`) REFERENCES `rights` (`rights`);

--
-- 限制表 `user_homework`
--
ALTER TABLE `user_homework`
  ADD CONSTRAINT `user_homework_homework_homeworkId_fk` FOREIGN KEY (`homeworkId`) REFERENCES `homework` (`homeworkid`),
  ADD CONSTRAINT `user_homework_user_usernameId_fk` FOREIGN KEY (`usernameId`) REFERENCES `user` (`usernameid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
