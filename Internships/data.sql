-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: Internships
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add offer',7,'add_offer'),(20,'Can change offer',7,'change_offer'),(21,'Can delete offer',7,'delete_offer'),(22,'Can add institution',8,'add_institution'),(23,'Can change institution',8,'change_institution'),(24,'Can delete institution',8,'delete_institution');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$d29J6JH5ozOV$Ki86XqU07K0N7U4p8R0wo8oqUHX9xxGv/Z/csO4/kio=','2017-04-05 10:21:56.349457',1,'anna','','','anna@anna.pl',1,1,'2017-04-04 19:11:18.208341'),(2,'pbkdf2_sha256$30000$i3f7B1TLkqDz$uRtsJ8crUgbo8jjg7V48+r+tH/WDB71w7LkQ8m8iSvM=','2017-04-05 07:59:44.415941',0,'Centrum_Kultury_w_Rzeszowie','','','',0,1,'2017-04-04 19:28:04.082007'),(3,'pbkdf2_sha256$30000$jNby7T658DNe$SDxstm5WLJQ4kFZleDKj2eVzWPZidHe+ama1DCGXa7o=','2017-04-05 08:33:47.556978',0,'MCK','','','',0,1,'2017-04-05 08:14:31.717572'),(4,'pbkdf2_sha256$30000$W4efxdOMUnS6$szG5/zaTsp9ZKOcXzHnoaxzq7D7xrMkLMtmDVjwn6jA=','2017-04-05 08:51:31.888527',0,'NCK','','','',0,1,'2017-04-05 08:51:16.692480'),(5,'pbkdf2_sha256$30000$a4ELdWiNfGUn$+d92/vbTVp0ROsWBYFvqp8jCPQSb36UdhFgUu4KmAoE=','2017-04-05 08:54:59.315714',0,'Mubabao','','','',0,1,'2017-04-05 08:54:48.180767'),(6,'pbkdf2_sha256$30000$1hNWW6QE1wvq$Tl+wKhh0n4Bwi0bYDXln5OPtVqzUQkVT41VHPzTo4o8=','2017-04-05 09:14:17.739016',0,'CNK','','','',0,1,'2017-04-05 09:14:04.179990'),(7,'pbkdf2_sha256$30000$q9O2ACJBYJ1e$OCavo5URDkKpgsuzRLVLxbZ+Md/JsmCO/qQJp5MoBtQ=','2017-04-05 12:48:14.482949',0,'DKBronowice','','','',0,1,'2017-04-05 09:55:21.833830'),(8,'pbkdf2_sha256$30000$vetGAhJBtfwQ$50vfp4sJkuns8e6/xE7Tfobf0DgvKU3vQjqAJLRCE8Q=','2017-04-05 12:52:53.258431',0,'MSN','','','',0,1,'2017-04-05 12:52:24.749498');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(8,'intern_app','institution'),(7,'intern_app','offer'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-04-04 19:09:24.487069'),(2,'auth','0001_initial','2017-04-04 19:09:34.514728'),(3,'admin','0001_initial','2017-04-04 19:09:36.828599'),(4,'admin','0002_logentry_remove_auto_add','2017-04-04 19:09:36.978110'),(5,'contenttypes','0002_remove_content_type_name','2017-04-04 19:09:38.322388'),(6,'auth','0002_alter_permission_name_max_length','2017-04-04 19:09:39.233672'),(7,'auth','0003_alter_user_email_max_length','2017-04-04 19:09:40.187101'),(8,'auth','0004_alter_user_username_opts','2017-04-04 19:09:40.253016'),(9,'auth','0005_alter_user_last_login_null','2017-04-04 19:09:40.884129'),(10,'auth','0006_require_contenttypes_0002','2017-04-04 19:09:40.974610'),(11,'auth','0007_alter_validators_add_error_messages','2017-04-04 19:09:41.041802'),(12,'auth','0008_alter_user_username_max_length','2017-04-04 19:09:42.028746'),(13,'intern_app','0001_initial','2017-04-04 19:09:44.599294'),(14,'sessions','0001_initial','2017-04-04 19:09:45.253803'),(15,'intern_app','0002_offer_name','2017-04-04 19:23:49.009278');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('rjxw1kyr054202nvdtbzkvljaa4vuwvw','YjMwODViNDJiOTI2ODZhODMzNWQ2OGE2YWMwZmNlZWFiODEwMWY2Mzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMjE5MmViMmMxMGU3Zjg5MmY3ZjEwNTk4ZGQ0ZDc4YWExYmUzNTdjNSIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2017-04-19 12:52:53.368421');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `intern_app_institution`
--

LOCK TABLES `intern_app_institution` WRITE;
/*!40000 ALTER TABLE `intern_app_institution` DISABLE KEYS */;
INSERT INTO `intern_app_institution` VALUES (1,'Międzynarodowe Centrum Kultury','MCK ma status narodowej instytucji kultury, która prowadzi działalność badawczą, edukacyjną, wydawniczą i wystawienniczą, wypełniając misję dyplomacji publicznej poprzez międzynarodowy dialog w kulturze. Punktem wyjścia do naszych działań i rozważań na temat dziedzictwa jest Europa Środkowa.','Kraków','Rynek Główny','25','mp',3),(2,'Narodowe Centrum Kultury','Narodowe Centrum Kultury jest państwową instytucją kultury, której statutowym zadaniem jest podejmowanie działań na rzecz rozwoju kultury w Polsce.','Warszawa','Płocka','13','maz',4),(3,'Muzeum Bajek, Baśni i Opowieści','The custodian and originator of MuBaBaO, storyteller, writer, tutor and traveller. The author of innovative methods of storytelling and inspiration seeker. As a prevailing member of Intangible Herritage Board in Polish Ministry of Culture he is struggling to protect the words from sinking into oblivion.','Konstancin Jeziorna','Diamentowa','8','maz',5),(4,'Centrum Nauki Kopernik','Centrum Nauki Kopernik to nie jest muzeum. Nie mamy gablot ani przewodników. To przestrzeń, która zainspiruje Cię do obserwacji, doświadczania, zadawania pytań i poszukiwania odpowiedzi. Od Ciebie zależy, ile z tego weźmiesz.','Warszawa','Wybrzeże Kościuszkowskie','20','maz',6),(5,'Dom Kultury Bronowice','Zapraszamy wszystkich do odwiedzenia nas i skorzystania z naszej oferty.\r\nDzielnicowy Dom Kultury \"Bronowice\" posiada aktualnie trzy siedziby.','Lublin','Krańcowa','106','lbl',7);
/*!40000 ALTER TABLE `intern_app_institution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `intern_app_offer`
--

LOCK TABLES `intern_app_offer` WRITE;
/*!40000 ALTER TABLE `intern_app_offer` DISABLE KEYS */;
/*!40000 ALTER TABLE `intern_app_offer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-05 15:10:08
