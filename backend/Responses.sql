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

INSERT INTO Responses (UserID, Question1, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9, Question10, Question11, Question12, Question13, Question14, Question15, Question16, Question17, Question18, Question19, Question20, Question21, Question22, Question23, Question24):
VALUES ("001",2,2,2,3,2,3,2,1,4,1,2,3,1,2,4,2,3,1,2,2,3,3,4,4),
("002",3,2,4,1,2,3,4,3,2,1,2,3,4,3,4,2,1,2,3,2,1,1,1,1),
("003",2,1,4,3,2,1,3,2,4,1,2,3,2,1,2,1,2,3,4,3,2,1,2,1),
("004",2,1,2,4,3,3,2,1,2,3,4,1,2,3,1,2,1,2,4,3,2,3,4,1),
("005",3,3,2,2,2,3,4,1,2,2,1,3,4,2,1,2,4,3,2,3,2,1,3,1),
("006",4,4,3,3,2,1,4,3,2,3,1,1,3,4,2,1,1,2,3,2,1,2,3,2),
("007",1,2,4,3,2,3,2,1,2,2,4,4,3,2,1,2,3,4,4,3,2,2,3,1),
("008",1,2,2,1,3,4,3,2,1,2,3,4,3,2,2,1,2,1,1,4,3,2,1,1),
("009",2,1,3,1,2,4,3,2,3,2,3,4,1,2,3,4,2,3,4,5,3,2,4,2),
("010",1,2,3,1,4,3,2,1,2,3,4,2,1,2,3,4,1,1,2,2,3,3,4,1),
("011",3,2,4,1,2,4,3,3,1,1,1,4,2,3,3,2,4,4,2,3,3,2,1,4),
("012",4,2,1,2,3,3,4,2,3,1,2,1,2,3,4,3,2,1,2,3,4,1,2,4),
("013",1,3,4,2,3,4,4,3,1,3,2,1,4,3,1,2,4,4,3,4,1,2,3,4),
("014",4,2,3,4,1,2,3,3,2,2,2,1,2,3,4,4,4,2,1,1,1,2,3,4),
("015",1,1,1,4,4,2,2,3,4,1,2,3,3,2,2,2,4,4,1,2,3,4,2,3),
("016",2,3,4,2,1,2,3,2,1,2,3,4,3,2,1,2,3,4,3,2,1,1,3,4),
("017",3,2,1,2,3,4,3,2,1,2,3,2,1,2,2,2,3,2,1,2,3,4,2,1),
("018",1,2,3,2,1,2,1,2,3,4,2,3,2,3,4,3,2,1,3,3,2,1,2,3),
("019",3,3,4,3,2,1,2,3,2,3,2,1,2,3,2,1,2,3,4,1,2,1,2,1),
("020",2,1,2,3,4,4,3,3,2,1,2,3,4,3,2,1,2,3,4,4,3,2,1,1);