-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 26, 2021 at 03:47 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


--Databse: 'College'
--table structure for student

CREATE TABLE `Student` (
  `id` int(11) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `sem` int(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` varchar(12) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `branch` varchar(50) NOT NULL,
  `aadharno` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `Student`
--
DELIMITER $$
CREATE TRIGGER `DELETE` BEFORE DELETE ON `Student` FOR EACH ROW INSERT INTO trig VALUES(null,OLD.id,'STUDENT DELETED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Insert` AFTER INSERT ON `Student` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.id,'STUDENT INSERTED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `UPDATE` AFTER UPDATE ON `Student` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.id,'STUDENT UPDATED',NOW())
$$
DELIMITER ;

--table structure for staff
CREATE TABLE `Staff` (
  `id` int(11) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phno` varchar(12) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `branch` varchar(50) NOT NULL,
  `aadharno` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `Staff`
--
DELIMITER $$
CREATE TRIGGER `DELETE` BEFORE DELETE ON `Staff` FOR EACH ROW INSERT INTO trig VALUES(null,OLD.id,'STUDENT DELETED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `Insert` AFTER INSERT ON `Staff` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.id,'STUDENT INSERTED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `UPDATE` AFTER UPDATE ON `Staff` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.id,'STUDENT UPDATED',NOW())
$$
DELIMITER ;



--table structure for user
CREATE TABLE `user`(
`id` int(11) NOT NULL,
`username` varcar(100) NOT NULL,
`email` varchar(50) NOT NULL,
`password` varchar(1000) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(4, 'anees', 'anees@gmail.com', 'ai023@bnm');
--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(52) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(43, 'jayasri');

--
-- Indexes for table `student`
--
ALTER TABLE `Student`
  ADD PRIMARY KEY (`id`);


--
-- Indexes for table `User`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);


-
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `Student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

- AUTO_INCREMENT for table `Staff`
--

--
-- AUTO_INCREMENT for table `User`
--
ALTER TABLE `User`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;