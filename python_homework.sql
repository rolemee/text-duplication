-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2022-11-22 21:16:52
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
-- 数据库： `python_homework`
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
  `homework_type` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `start_time` datetime NOT NULL,
  `stop_time` datetime NOT NULL,
  `teacher_name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `completeness` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `homework`
--

INSERT INTO `homework` (`homeworkId`, `usernameId`, `homeworkName`, `homeworkDescribe`, `homework_type`, `start_time`, `stop_time`, `teacher_name`, `completeness`) VALUES
(11, 2, '测试', '这是测试', 'c++', '2022-11-04 12:12:56', '2022-12-04 12:12:57', 'wsc', 0.89),
(22, 2, 'test2', '这是测试py', 'python', '2022-11-15 16:08:30', '2022-12-15 16:08:32', 'wsc', 0.54),
(33, 2, 'test3', '测试java', 'java', '2022-11-17 14:21:22', '2022-12-17 14:21:23', 'wsc', 0.58),
(44, 2, 'test4', '测试go', 'go', '2022-11-17 14:56:49', '2022-12-17 14:56:51', 'wsc', 0.68),
(55, 2, 'test5', '测试rust', 'rust', '2022-11-17 14:57:16', '2022-12-17 14:57:17', 'wsc', 0.46),
(66, 2, 'test6', '测试文本', 'txt', '2022-11-17 18:42:18', '2022-12-17 18:43:20', 'wsc', 0.85),
(77, 2, 'test7', '测试汇编', 'asm', '2022-11-17 19:05:26', '2022-12-17 19:05:28', 'wsc', 0.6);

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
(0, 'student'),
(1, 'teacher');

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
(1, 'jrm', 'rolemee', 'a123456', 0, NULL),
(2, 'wsc', 'tbao', 'a123456', 1, NULL),
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
-- 转存表中的数据 `user_homework`
--

INSERT INTO `user_homework` (`usernameId`, `homeworkId`, `is_Finish`) VALUES
(1, 11, 0),
(1, 22, 0),
(1, 33, 0),
(1, 44, 0),
(1, 55, 0),
(1, 66, 0),
(1, 77, 0),
(2, 11, 0),
(2, 22, 0),
(2, 33, 0),
(2, 44, 0),
(2, 55, 0),
(2, 66, 0),
(2, 77, 0);

--
-- 转储表的索引
--

--
-- 表的索引 `homework`
--
ALTER TABLE `homework`
  ADD PRIMARY KEY (`homeworkId`),
  ADD KEY `homework_user_usernameId_fk` (`usernameId`),
  ADD KEY `homework_user_name_fk` (`teacher_name`);

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
  ADD KEY `user_rights_rights_fk` (`rights`),
  ADD KEY `user_name_index` (`name`);

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
  ADD CONSTRAINT `homework_user_name_fk` FOREIGN KEY (`teacher_name`) REFERENCES `user` (`name`),
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
