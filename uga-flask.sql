-- MySQL dump 10.13  Distrib 8.0.41, for Linux (x86_64)
--
-- Host: localhost    Database: uga-flask
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `teacher_id` int NOT NULL,
  `course_name` varchar(256) NOT NULL,
  `stu_count` int NOT NULL,
  `submit_count` int NOT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`course_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `users` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,1,'数据结构',48,0,0),(2,1,'计算机网络',48,0,0),(3,1,'计算机组成原理',47,0,0),(4,1,'高等数学',30,0,1),(5,1,'高等数学上',30,0,1),(6,1,'数据结构',48,10,1),(7,1,'计算机操作系统',48,0,0);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_paper`
--

DROP TABLE IF EXISTS `test_paper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_paper` (
  `test_id` int NOT NULL AUTO_INCREMENT,
  `course_id` int DEFAULT '1',
  `teacher_id` int NOT NULL,
  `college` varchar(256) NOT NULL,
  `stu_class` varchar(256) DEFAULT NULL,
  `stu_name` varchar(64) DEFAULT NULL,
  `stu_no` varchar(128) NOT NULL,
  `p1` int DEFAULT NULL,
  `p2` int DEFAULT NULL,
  `p3` int DEFAULT NULL,
  `p4` int DEFAULT NULL,
  `p5` int DEFAULT NULL,
  `p6` int DEFAULT NULL,
  `total` int DEFAULT NULL,
  `isDelete` int DEFAULT '0',
  PRIMARY KEY (`test_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `test_paper_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `users` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_paper`
--

LOCK TABLES `test_paper` WRITE;
/*!40000 ALTER TABLE `test_paper` DISABLE KEYS */;
INSERT INTO `test_paper` VALUES (1,1,1,'电子信息学','计算机2101','林栋哲','2021283122',10,10,20,0,15,5,60,0),(2,1,1,'电子信息学','计算机2101','卢忠强','2021283119',10,10,10,20,10,10,70,0),(3,1,1,'电子信息学院','计算机210J','江舞成','2021283121',10,15,0,15,5,0,45,0),(4,1,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(5,1,1,'电子信息学院','计算机2101','马捷','2021283126',10,20,15,20,0,15,80,0),(6,1,1,'电子信自学','计算机2101','徐栀','2021283124',0,15,0,0,15,15,45,0),(7,1,1,'电子信息学','计算机2101','林栋哲','2021283122',10,10,20,0,15,5,60,0),(8,1,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(9,1,1,'电子信息学','计算机2101','林栋哲','2021283122',10,10,20,0,15,5,60,0),(10,1,1,'电子信息学院','计算机210J','江舞成','2021283121',10,15,0,15,5,0,45,0),(11,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(12,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(13,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(14,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(15,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(16,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(17,1,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(18,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(19,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(20,1,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(21,1,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(22,1,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(23,1,1,'电子信息学','计算机2101','卢忠强','2021283119',10,10,10,20,10,10,70,0),(24,1,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(25,1,1,'电子信自学','计算机2101','徐栀','2021283124',0,15,0,0,15,15,45,0),(26,1,1,'电子信息学院','计算机2101','马捷','2021283126',10,20,15,20,0,15,80,0),(27,1,1,'电子信息学','计算机2101','林栋哲','2021283122',10,10,20,0,15,5,60,0),(28,1,1,'电子信息学院','计算机210J','江舞成','2021283121',10,15,0,15,5,0,45,0),(29,1,1,'电子信息学','计算机2101','庞桂慧','2021283116',20,5,10,15,0,0,50,0),(30,1,1,'电子信息学','计算机2101','林栋哲','2021283122',10,10,20,0,15,5,60,0),(31,1,1,'电子信息学院','计算机210J','江舞成','2021283121',10,15,0,15,5,0,45,0),(32,1,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(33,1,1,'电子信息学院','计算机2101','马捷','2021283126',10,20,15,20,0,15,80,0),(34,NULL,1,'电子信息学','计算机2101','庞桂慧','2021283116',20,5,10,15,0,0,50,0),(35,1,1,'电子信息学院','计算机2101','马捷','2021283126',10,20,15,20,0,15,80,0),(36,2,1,'电子信息学院','计算机2101','温以凡','2021283128',5,15,0,5,20,25,70,0),(37,2,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(38,2,1,'电子信息学院','计算机210','庄晓婷','2021283123',10,15,0,15,10,15,65,0),(39,2,1,'电子信息学','计算机2101','庞桂慧','2021283116',20,5,10,15,0,0,50,0);
/*!40000 ALTER TABLE `test_paper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `teacher_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `sex` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `age` int DEFAULT NULL,
  `email` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `phone` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `address` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `school` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `profession` varchar(128) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `password_hash` varchar(512) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `nickname` varchar(255) NOT NULL,
  PRIMARY KEY (`teacher_id`) USING BTREE,
  UNIQUE KEY `username` (`username`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE,
  UNIQUE KEY `sex` (`sex`) USING BTREE,
  UNIQUE KEY `age` (`age`) USING BTREE,
  UNIQUE KEY `phone` (`phone`) USING BTREE,
  UNIQUE KEY `address` (`address`) USING BTREE,
  UNIQUE KEY `school` (`school`) USING BTREE,
  UNIQUE KEY `profession` (`profession`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','男',22,'小明@163.com','15037626907',NULL,'湖州学院','计算机科学与技术','scrypt:32768:8:1$LIE8cAgaQTnoSK0y$46c63f249dfaac2b1e1ec15d0c6d333e02389a92d003b300c2553b559a98a11e5fc57f499c715d4f2070db380454e6452b6707dd147fd59171960485200ed5de','李华');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-28 18:10:32
