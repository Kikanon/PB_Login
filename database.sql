CREATE DATABASE IF NOT EXISTS PB_Login;
USE PB_Login;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_slovenian_ci NOT NULL,
  `pass` varchar(64) COLLATE utf8_slovenian_ci NOT NULL,
  PRIMARY KEY(`id`)
);

CREATE USER 'programski_dostop'@'%' IDENTIFIED BY 'programsko_geslo';
CREATE USER 'jakob'@'%' IDENTIFIED BY 'tezkogeslo123';

GRANT SELECT,INSERT ON PB_Login.users TO 'programski_dostop'@'%';
GRANT SELECT (name) ON PB_Login.users TO 'jakob'@'%';