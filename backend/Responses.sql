-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 01, 2024 at 02:15 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `CelebratoryTech`
--

-- --------------------------------------------------------

--
-- Table structure for table `Responses`
--

CREATE TABLE `Responses` (
  `UserID` int(4) NOT NULL,
  `Question1` int(4) NOT NULL,
  `Question2` int(4) NOT NULL,
  `Question3` int(4) NOT NULL,
  `Question4` int(4) NOT NULL,
  `Question5` int(4) NOT NULL,
  `Question6` int(4) NOT NULL,
  `Question7` int(4) NOT NULL,
  `Question8` int(4) NOT NULL,
  `Question9` int(4) NOT NULL,
  `Question10` int(4) NOT NULL,
  `Question11` int(4) NOT NULL,
  `Question12` int(4) NOT NULL,
  `Question13` int(4) NOT NULL,
  `Question14` int(4) NOT NULL,
  `Question15` int(4) NOT NULL,
  `Question16` int(4) NOT NULL,
  `Question17` int(4) NOT NULL,
  `Question18` int(4) NOT NULL,
  `Question19` int(4) NOT NULL,
  `Question20` int(4) NOT NULL,
  `Question21` int(4) NOT NULL,
  `Question22` int(4) NOT NULL,
  `Question23` int(4) NOT NULL,
  `Question24` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
