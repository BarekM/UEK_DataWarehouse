-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dev_uek_dw
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_animal`
--

DROP TABLE IF EXISTS `tbl_animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_animal` (
  `animal` varchar(20) NOT NULL,
  PRIMARY KEY (`animal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_animal`
--

LOCK TABLES `tbl_animal` WRITE;
/*!40000 ALTER TABLE `tbl_animal` DISABLE KEYS */;
INSERT INTO `tbl_animal` VALUES ('mozna'),('nie mozna');
/*!40000 ALTER TABLE `tbl_animal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_city`
--

DROP TABLE IF EXISTS `tbl_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_city` (
  `city` varchar(20) NOT NULL,
  PRIMARY KEY (`city`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_city`
--

LOCK TABLES `tbl_city` WRITE;
/*!40000 ALTER TABLE `tbl_city` DISABLE KEYS */;
INSERT INTO `tbl_city` VALUES ('Bialystok'),('Gdansk'),('Katowice'),('Kielce'),('Krakow'),('Lodz'),('Lublin'),('Olsztyn'),('Opole'),('Poznan'),('Rzeszow'),('Szczecin'),('Warszawa'),('Wroclaw'),('Zielona Gora');
/*!40000 ALTER TABLE `tbl_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_main`
--

DROP TABLE IF EXISTS `tbl_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_main` (
  `id` varchar(20) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `rooms` varchar(20) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `parking` varchar(20) DEFAULT NULL,
  `animal` varchar(20) DEFAULT NULL,
  `smoking` varchar(20) DEFAULT NULL,
  `deal` varchar(20) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `k_city_idx` (`city`),
  KEY `k_room_idx` (`rooms`),
  KEY `k_type_idx` (`type`),
  KEY `k_smoking_idx` (`smoking`),
  KEY `k_animal_idx` (`animal`),
  KEY `k_parking_idx` (`parking`),
  KEY `k_renting_idx` (`deal`),
  CONSTRAINT `k_animal` FOREIGN KEY (`animal`) REFERENCES `tbl_animal` (`animal`),
  CONSTRAINT `k_city` FOREIGN KEY (`city`) REFERENCES `tbl_city` (`city`),
  CONSTRAINT `k_parking` FOREIGN KEY (`parking`) REFERENCES `tbl_parking` (`parking`),
  CONSTRAINT `k_renting` FOREIGN KEY (`deal`) REFERENCES `tbl_renting` (`owner`),
  CONSTRAINT `k_room` FOREIGN KEY (`rooms`) REFERENCES `tbl_room` (`room`),
  CONSTRAINT `k_smoking` FOREIGN KEY (`smoking`) REFERENCES `tbl_smoking` (`smoking`),
  CONSTRAINT `k_type` FOREIGN KEY (`type`) REFERENCES `tbl_type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_main`
--

LOCK TABLES `tbl_main` WRITE;
/*!40000 ALTER TABLE `tbl_main` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_parking`
--

DROP TABLE IF EXISTS `tbl_parking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_parking` (
  `parking` varchar(20) NOT NULL,
  PRIMARY KEY (`parking`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_parking`
--

LOCK TABLES `tbl_parking` WRITE;
/*!40000 ALTER TABLE `tbl_parking` DISABLE KEYS */;
INSERT INTO `tbl_parking` VALUES ('brak'),('dedykowane miejsce'),('garaz'),('zamkniete osiedle');
/*!40000 ALTER TABLE `tbl_parking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_renting`
--

DROP TABLE IF EXISTS `tbl_renting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_renting` (
  `owner` varchar(20) NOT NULL,
  PRIMARY KEY (`owner`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_renting`
--

LOCK TABLES `tbl_renting` WRITE;
/*!40000 ALTER TABLE `tbl_renting` DISABLE KEYS */;
INSERT INTO `tbl_renting` VALUES ('agencja'),('wlasciciel');
/*!40000 ALTER TABLE `tbl_renting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_room`
--

DROP TABLE IF EXISTS `tbl_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_room` (
  `room` varchar(3) NOT NULL,
  PRIMARY KEY (`room`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_room`
--

LOCK TABLES `tbl_room` WRITE;
/*!40000 ALTER TABLE `tbl_room` DISABLE KEYS */;
INSERT INTO `tbl_room` VALUES ('0'),('1'),('2'),('3'),('4'),('5'),('5<');
/*!40000 ALTER TABLE `tbl_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_smoking`
--

DROP TABLE IF EXISTS `tbl_smoking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_smoking` (
  `smoking` varchar(20) NOT NULL,
  PRIMARY KEY (`smoking`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_smoking`
--

LOCK TABLES `tbl_smoking` WRITE;
/*!40000 ALTER TABLE `tbl_smoking` DISABLE KEYS */;
INSERT INTO `tbl_smoking` VALUES ('mozna'),('nie mozna');
/*!40000 ALTER TABLE `tbl_smoking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_type`
--

DROP TABLE IF EXISTS `tbl_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_type` (
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_type`
--

LOCK TABLES `tbl_type` WRITE;
/*!40000 ALTER TABLE `tbl_type` DISABLE KEYS */;
INSERT INTO `tbl_type` VALUES ('dom'),('mieszkanie'),('pokoj');
/*!40000 ALTER TABLE `tbl_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-10 23:56:49
