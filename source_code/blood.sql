
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `blood_bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `New_Patient`
--

CREATE TABLE `New_Patient` (
  `Adhar_ID` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Blood_group` varchar(255) NOT NULL,
  `Pincode` int(11) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone` int(11) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='data of new patient';

--
-- Dumping data for table `New_Patient`
--

INSERT INTO `New_Patient` (`Adhar_ID`, `Name`, `Blood_group`, `Pincode`, `Email`, `Phone`) VALUES
('323655837546', 'Vinaysingh Patil', 'A+', '111903124', 'vinaypatil7454@gmail.com', '9022579040'),
('987654321000', 'Vedashree satpute', 'O+', '654123', 'ved7pute@gmail.com', '8888446179'),

-- --------------------------------------------------------

--
-- Indexes for dumped tables
--

--
-- Indexes for table `New_Patient`
--
ALTER TABLE `New_Patient`
  ADD PRIMARY KEY (`Blood_group`);


--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `New_Patient`
--
ALTER TABLE `New_Patient`
  MODIFY `Blood_group` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
  MODIFY `Pincode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
  MODIFY `Phone` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
  
;
