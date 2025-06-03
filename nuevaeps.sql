# Host: localhost  (Version 5.5.5-10.4.32-MariaDB)
# Date: 2025-05-30 11:22:39
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "medicamentos"
#

DROP TABLE IF EXISTS `medicamentos`;
CREATE TABLE `medicamentos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `es_no_pos` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "medicamentos"
#

INSERT INTO `medicamentos` VALUES (1,'Paracetamol',1),(2,'Quita Fiebre',0);

#
# Structure for table "usuarios"
#

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "usuarios"
#

INSERT INTO `usuarios` VALUES (1,'tatto','$2b$12$HaF5okd2sV.cJe0H5Df5Q.OJVeFc.EyCxaV5g0KdFcNKh46xRLyga'),(2,'wendi','$2b$12$EGSzWu4jExw5SI1BkgU3A.qIwn.MNxaCI4.o7jPwkGgATUp.ZDpne');

#
# Structure for table "solicitudes"
#

DROP TABLE IF EXISTS `solicitudes`;
CREATE TABLE `solicitudes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medicamento_id` int(11) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `numero_orden` varchar(100) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `medicamento_id` (`medicamento_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `solicitudes_ibfk_1` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamentos` (`id`),
  CONSTRAINT `solicitudes_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#
# Data for table "solicitudes"
#

INSERT INTO `solicitudes` VALUES (1,1,1,'ORD123','Calle 123','3214567890','correo@dominio.com'),(2,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(3,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(4,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(5,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(6,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(7,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(8,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(9,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(10,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(11,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(12,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(13,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(14,1,1,'ORD123','Calle 123','3214567890','corre1o@dominio.com'),(15,1,1,'ORD123','Calle 456','3214567890','corre1o@dominio.com'),(16,1,1,'12312','sadasd','asdsad','asdasd@sdsa.com'),(17,1,1,'2322','sadasd','asdasd','asdsad@asdas.com'),(18,1,1,'1','1','1','pepe@prueba.com'),(19,1,1,'12312','1','1','prueba@prueba.com'),(20,1,1,'1','1','9','1@sd.cpom'),(21,2,2,'1111qqq','qqq','22222222','2@sd.cpom'),(22,1,2,'33333','asd','3333','3@sd.cpom'),(23,1,2,'guyg8sdf','sadsa','2312321','aa@sd.com'),(24,2,1,'12312','sdasd','1231312','pepe@asd.com');
