CREATE DATABASE  IF NOT EXISTS `album`; 
USE `album`;

DROP TABLE IF EXISTS `paises`;
CREATE TABLE `paises` (
  `id` char(3) NOT NULL,
  `nome_pais` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
); 

INSERT INTO `paises` VALUES ('ARG','Argentina'),('BRA','Brasil'),('POR','Portugal');

DROP TABLE IF EXISTS `figurinhas`;
CREATE TABLE `figurinhas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_pais` char(3) NOT NULL,
  `jogador` varchar(50) DEFAULT NULL,
  `numero` int(11) NOT NULL,
  `tem` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `id_pais` (`id_pais`),
  CONSTRAINT `figurinhas_ibfk_1` FOREIGN KEY (`id_pais`) REFERENCES `paises` (`id`)
);

INSERT INTO `figurinhas` (`id_pais`,`jogador`,`numero`) VALUES ('por','time',1),('por','escudo',2),('por','diogo costa',3),('por','rui patricio',4),('por','joao cancelo',5),('por','jose fonte',6),('por','nuno mendes',7),('por','pepe',8),('por','raphael guerreiro',9),('por','ruben dias',10),('por','bernardo silva',11),('por','bruno fernandes',12),('por','danilo pereira',13),('por','joao moutinho',14),('por','renato sanches',15),('por','ruben neves',16),('por','andre silva',17),('por','cristiano ronaldo',18),('por','diogo jota',19),('por','goncalo guedes',20),('bra','time',1),('bra','escudo',2),('bra','alisson',3),('bra','ederson',4),('bra','alex sandro',5),('bra','danilo',6),('bra','eder militao',7),('bra','marquinhos',8),('bra','thiago silva',9),('bra','casemiro',10),('bra','philippe coutinho',11),('bra','fabinho',12),('bra','fred',13),('bra','lucas paqueta',14),('bra','antony',15),('bra','gabriel jesus',16),('bra','neymar jr',17),('bra','raphinha',18),('bra','richarlison',19),('bra','vinicius jr',20),('arg','time',1),('arg','escudo',2),('arg','emiliano martinez',3),('arg','franco armani',4),('arg','marcos acuna',5),('arg','nahuel molina',6),('arg','nicolas otamendi',7),('arg','german pezzella',8),('arg','cristian romero',9),('arg','rodrigo de paul',10),('arg','angel di maria',11),('arg','giovani lo celso',12),('arg','leandro paredes',13),('arg','guido rodriguez',14),('arg','julian alvarez',15),('arg','joaquin correa',16),('arg','alejandro gomez',17),('arg','nicolas gonzalez',18),('arg','lautaro martinez',19),('arg','lionel messi',20);


