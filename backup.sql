-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: cine
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `cine`
--

DROP TABLE IF EXISTS `cine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cine` (
  `citykey` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `cityname` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `id_cine` int DEFAULT NULL,
  `cinekey` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `hours` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `country` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `id_cinema_chain` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cine`
--

LOCK TABLES `cine` WRITE;
/*!40000 ALTER TABLE `cine` DISABLE KEYS */;
INSERT INTO `cine` VALUES ('panama-david-chiriqui','Panamá, David Chiriquí',672,'cinepolis-federal-mall','Cinépolis Federal Mall','Alarido','[\'20:00\', \'22:30\']',NULL,NULL,NULL,NULL),('panama-david-chiriqui','Panamá, David Chiriquí',672,'cinepolis-federal-mall','Cinépolis Federal Mall','Bestia','[\'21:15\']',NULL,NULL,NULL,NULL),('panama-david-chiriqui','Panamá, David Chiriquí',672,'cinepolis-federal-mall','Cinépolis Federal Mall','Cambio de planes','[\'19:30\', \'21:50\']',NULL,NULL,NULL,NULL),('panama-david-chiriqui','Panamá, David Chiriquí',672,'cinepolis-federal-mall','Cinépolis Federal Mall','Dragon Ball Super: Super Héroe','[\'19:00\', \'19:45\', \'21:00\', \'21:30\', \'22:00\']',NULL,NULL,NULL,NULL),('panama-david-chiriqui','Panamá, David Chiriquí',672,'cinepolis-federal-mall','Cinépolis Federal Mall','Top Gun: Maverick','[\'20:15\']',NULL,NULL,NULL,NULL),('panama-david-chiriqui','Panamá, David Chiriquí',672,'cinepolis-federal-mall','Cinépolis Federal Mall','Tren bala','[\'19:20\', \'22:20\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',639,'cinepolis-anclas-mall-plaza','Cinépolis Anclas Mall  Plaza','Alarido','[\'19:15\', \'21:30\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',639,'cinepolis-anclas-mall-plaza','Cinépolis Anclas Mall  Plaza','Bestia','[\'20:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',639,'cinepolis-anclas-mall-plaza','Cinépolis Anclas Mall  Plaza','Cambio de planes','[\'20:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',639,'cinepolis-anclas-mall-plaza','Cinépolis Anclas Mall  Plaza','Dragon Ball Super: Super Héroe','[\'18:45\', \'19:45\', \'21:15\', \'22:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',639,'cinepolis-anclas-mall-plaza','Cinépolis Anclas Mall  Plaza','Tren bala','[\'20:15\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',246,'cinepolis-westland-mall','Cinépolis Westland Mall','Alarido','[\'20:25\', \'22:30\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',246,'cinepolis-westland-mall','Cinépolis Westland Mall','Bestia','[\'18:40\', \'21:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',246,'cinepolis-westland-mall','Cinépolis Westland Mall','Cambio de planes','[\'19:25\', \'21:25\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',246,'cinepolis-westland-mall','Cinépolis Westland Mall','Dragon Ball Super: Super Héroe','[\'19:00\', \'19:40\', \'20:05\', \'22:05\', \'21:40\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',246,'cinepolis-westland-mall','Cinépolis Westland Mall','Top Gun: Maverick','[\'20:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',246,'cinepolis-westland-mall','Cinépolis Westland Mall','Tren bala','[\'19:10\', \'21:55\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',567,'cinepolis-town-center','Cinépolis Town Center','Bestia','[\'21:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',567,'cinepolis-town-center','Cinépolis Town Center','Cambio de planes','[\'19:30\', \'21:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',567,'cinepolis-town-center','Cinépolis Town Center','Dragon Ball Super: Super Héroe','[\'19:00\', \'21:25\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',567,'cinepolis-town-center','Cinépolis Town Center','Elvis','[\'20:30\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',567,'cinepolis-town-center','Cinépolis Town Center','Tren bala','[\'20:00\', \'22:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',568,'cinepolis-vip-town-center','Cinépolis VIP Town Center','Dragon Ball Super: Super Héroe','[\'19:15\', \'22:20\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',568,'cinepolis-vip-town-center','Cinépolis VIP Town Center','Elvis','[\'21:50\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',568,'cinepolis-vip-town-center','Cinépolis VIP Town Center','Tren bala','[\'20:00\', \'22:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',498,'cinepolis-altaplaza','Cinépolis Altaplaza','Alarido','[\'18:45\', \'21:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',498,'cinepolis-altaplaza','Cinépolis Altaplaza','Bestia','[\'19:15\', \'21:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',498,'cinepolis-altaplaza','Cinépolis Altaplaza','Cambio de planes','[\'19:45\', \'22:00\', \'23:05\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',498,'cinepolis-altaplaza','Cinépolis Altaplaza','Dragon Ball Super: Super Héroe','[\'19:00\', \'20:30\', \'20:00\', \'22:30\', \'21:30\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',498,'cinepolis-altaplaza','Cinépolis Altaplaza','El teléfono negro','[\'20:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',498,'cinepolis-altaplaza','Cinépolis Altaplaza','Tren bala','[\'19:30\', \'21:15\', \'22:15\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',538,'cinepolis-el-dorado','Cinépolis El Dorado','Alarido','[\'20:25\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',538,'cinepolis-el-dorado','Cinépolis El Dorado','Bestia','[\'19:10\', \'21:15\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',538,'cinepolis-el-dorado','Cinépolis El Dorado','Cambio de planes','[\'20:35\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',538,'cinepolis-el-dorado','Cinépolis El Dorado','Dragon Ball Super: Super Héroe','[\'19:40\', \'21:05\', \'22:00\', \'19:00\', \'21:25\', \'19:25\', \'20:10\', \'22:25\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',538,'cinepolis-el-dorado','Cinépolis El Dorado','Top Gun: Maverick','[\'21:40\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',538,'cinepolis-el-dorado','Cinépolis El Dorado','Tren bala','[\'20:55\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',432,'cinepolis-andes-mall','Cinépolis Andes Mall','Alarido','[\'20:05\', \'22:05\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',432,'cinepolis-andes-mall','Cinépolis Andes Mall','Bestia','[\'21:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',432,'cinepolis-andes-mall','Cinépolis Andes Mall','Cambio de planes','[\'19:20\', \'21:40\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',432,'cinepolis-andes-mall','Cinépolis Andes Mall','Dragon Ball Super: Super Héroe','[\'19:00\', \'19:40\', \'21:20\', \'22:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',432,'cinepolis-andes-mall','Cinépolis Andes Mall','Tren bala','[\'20:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','Alarido','[\'20:05\', \'22:20\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','Bestia','[\'18:40\', \'21:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','Cambio de planes','[\'18:55\', \'21:20\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','DC Liga de Supermascotas','[\'19:15\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','Dragon Ball Super: Super Héroe','[\'19:05\', \'19:45\', \'21:30\', \'22:15\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','El teléfono negro','[\'22:40\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','Thor: Amor y trueno','[\'21:10\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','Top Gun: Maverick','[\'19:55\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',171,'cinepolis-metro-mall','Cinépolis Metro Mall','Tren bala','[\'20:50\', \'21:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',328,'cinepolis-multiplaza-pacific','Cinépolis Multiplaza Pacific','Alarido','[\'20:10\', \'22:25\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',328,'cinepolis-multiplaza-pacific','Cinépolis Multiplaza Pacific','Bestia','[\'19:30\', \'22:05\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',328,'cinepolis-multiplaza-pacific','Cinépolis Multiplaza Pacific','Cambio de planes','[\'18:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',328,'cinepolis-multiplaza-pacific','Cinépolis Multiplaza Pacific','Dragon Ball Super: Super Héroe','[\'20:35\', \'19:05\', \'19:45\', \'22:15\', \'21:30\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',328,'cinepolis-multiplaza-pacific','Cinépolis Multiplaza Pacific','Elvis','[\'20:55\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',328,'cinepolis-multiplaza-pacific','Cinépolis Multiplaza Pacific','Top Gun: Maverick','[\'20:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',328,'cinepolis-multiplaza-pacific','Cinépolis Multiplaza Pacific','Tren bala','[\'19:15\', \'20:45\', \'21:55\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',499,'cinepolis-vip-altaplaza','Cinépolis VIP Altaplaza','Dragon Ball Super: Super Héroe','[\'19:05\', \'22:10\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',499,'cinepolis-vip-altaplaza','Cinépolis VIP Altaplaza','Tren bala','[\'20:05\', \'21:05\', \'22:50\', \'23:45\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',143,'cinepolis-vip-multiplaza-pacific','Cinépolis VIP Multiplaza Pacific','Dragon Ball Super: Super Héroe','[\'20:15\', \'18:50\', \'21:30\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',143,'cinepolis-vip-multiplaza-pacific','Cinépolis VIP Multiplaza Pacific','Tren bala','[\'19:20\', \'20:50\', \'22:05\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',431,'cinepolis-vip-soho','Cinépolis VIP Soho','Bestia','[\'20:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',431,'cinepolis-vip-soho','Cinépolis VIP Soho','Cambio de planes','[\'18:40\', \'21:20\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',431,'cinepolis-vip-soho','Cinépolis VIP Soho','Dragon Ball Super: Super Héroe','[\'20:30\', \'19:00\', \'21:30\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',431,'cinepolis-vip-soho','Cinépolis VIP Soho','Elvis','[\'21:00\']',NULL,NULL,NULL,NULL),('panama-panama','Panamá, Panamá',431,'cinepolis-vip-soho','Cinépolis VIP Soho','Tren bala','[\'19:35\', \'21:40\', \'22:20\']',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `cine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cinema_chain`
--

DROP TABLE IF EXISTS `cinema_chain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cinema_chain` (
  `id` int NOT NULL,
  `cinema_chain` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cinema_chain`
--

LOCK TABLES `cinema_chain` WRITE;
/*!40000 ALTER TABLE `cinema_chain` DISABLE KEYS */;
/*!40000 ALTER TABLE `cinema_chain` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-19  3:24:23
