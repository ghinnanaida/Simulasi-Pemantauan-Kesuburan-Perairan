# Host: localhost  (Version 5.5.5-10.4.14-MariaDB)
# Date: 2020-12-14 12:18:29
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "stasiun1"
#

DROP TABLE IF EXISTS `stasiun1`;
CREATE TABLE `stasiun1` (
  `no` int(11) NOT NULL AUTO_INCREMENT,
  `tgljam` varchar(100) DEFAULT NULL,
  `sensor1` varchar(12) DEFAULT NULL,
  `sensor2` varchar(12) DEFAULT NULL,
  `sensor3` varchar(12) DEFAULT NULL,
  `sensor4` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB AUTO_INCREMENT=169 DEFAULT CHARSET=utf8mb4;

#
# Data for table "stasiun1"
#


#
# Structure for table "stasiun2"
#

DROP TABLE IF EXISTS `stasiun2`;
CREATE TABLE `stasiun2` (
  `no` int(11) NOT NULL AUTO_INCREMENT,
  `tgljam` varchar(100) DEFAULT NULL,
  `sensor1` varchar(12) DEFAULT NULL,
  `sensor2` varchar(12) DEFAULT NULL,
  `sensor3` varchar(12) DEFAULT NULL,
  `sensor4` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

#
# Data for table "stasiun2"
#


#
# Structure for table "stasiun3"
#

DROP TABLE IF EXISTS `stasiun3`;
CREATE TABLE `stasiun3` (
  `no` int(11) NOT NULL AUTO_INCREMENT,
  `tgljam` varchar(100) DEFAULT NULL,
  `sensor1` varchar(12) DEFAULT NULL,
  `sensor2` varchar(12) DEFAULT NULL,
  `sensor3` varchar(12) DEFAULT NULL,
  `sensor4` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

#
# Data for table "stasiun3"
#


#
# Structure for table "stasiun4"
#

DROP TABLE IF EXISTS `stasiun4`;
CREATE TABLE `stasiun4` (
  `no` int(11) NOT NULL AUTO_INCREMENT,
  `tgljam` varchar(100) DEFAULT NULL,
  `sensor1` varchar(12) DEFAULT NULL,
  `sensor2` varchar(12) DEFAULT NULL,
  `sensor3` varchar(12) DEFAULT NULL,
  `sensor4` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

#
# Data for table "stasiun4"
#


#
# Structure for table "user"
#

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

#
# Data for table "user"
#

INSERT INTO `user` VALUES (1,'ghinna','ghinna_08@apps.ipb.ac.id','123123');
