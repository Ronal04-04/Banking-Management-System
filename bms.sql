-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2024 at 06:59 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bms`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_details`
--

CREATE TABLE `account_details` (
  `Account_no` int(255) NOT NULL,
  `F_Name` varchar(255) NOT NULL,
  `M_Name` varchar(255) NOT NULL,
  `L_Name` varchar(255) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email_address` varchar(255) NOT NULL,
  `Adhar_no` varchar(255) NOT NULL,
  `Pan_no` varchar(255) NOT NULL,
  `Total_Balance` decimal(65,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_details`
--

INSERT INTO `account_details` (`Account_no`, `F_Name`, `M_Name`, `L_Name`, `DOB`, `Address`, `Email_address`, `Adhar_no`, `Pan_no`, `Total_Balance`) VALUES
(3, 'Roy', 'Joy', 'Souz', '2008-09-09', 'Bandra', 'RAY345@', '543209875436', 'GFR34OkJ', 1800),
(4, 'Renita', 'Baban', 'Dsouza', '2004-06-06', 'Malad', 'REN123@', '786512340987', 'AWQ234HY', 0),
(5, 'Mick', 'Sheldon', 'Cruz', '2005-08-08', 'Ville Parle', 'Mic123@', '789756789007', 'RTYJ78G', 0),
(6, 'Riya', 'Jack', 'Fers', '2023-09-07', 'Dadar', 'Riya123@', '782389219032', 'JKL76UI', 0),
(7, 'Liza', 'Francis', 'Dsouza', '2003-09-21', 'Nalasopara', 'Liza123@', '876543234509', 'GH78JK78KL', 0),
(8, 'Nick', 'Anton', 'Lopes', '2009-08-02', 'Parel', 'Nick123@', '7687976565', 'GF56GF78KJ', 0);

-- --------------------------------------------------------

--
-- Table structure for table `entry`
--

CREATE TABLE `entry` (
  `ID` int(255) NOT NULL,
  `Account_no` int(255) NOT NULL,
  `Date` date NOT NULL,
  `Credit` decimal(65,0) NOT NULL,
  `Debit` decimal(65,0) NOT NULL,
  `Total_Balance` decimal(65,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `entry`
--

INSERT INTO `entry` (`ID`, `Account_no`, `Date`, `Credit`, `Debit`, `Total_Balance`) VALUES
(1, 4, '2024-10-20', 2000, 0, 2000),
(2, 4, '2024-10-20', 3456, 0, 3456),
(3, 4, '2024-10-20', 2345, 0, 2345),
(4, 5, '2024-10-20', 2000, 0, 2000),
(5, 5, '2024-10-20', 1234, 0, 1234),
(6, 6, '2024-10-20', 9000, 0, 9000),
(7, 3, '2024-10-20', 2000, 0, 2000),
(8, 3, '2024-10-20', 0, 200, 1800);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_details`
--
ALTER TABLE `account_details`
  ADD PRIMARY KEY (`Account_no`);

--
-- Indexes for table `entry`
--
ALTER TABLE `entry`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_details`
--
ALTER TABLE `account_details`
  MODIFY `Account_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `entry`
--
ALTER TABLE `entry`
  MODIFY `ID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
