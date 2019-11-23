-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  sam. 23 nov. 2019 à 10:45
-- Version du serveur :  5.7.23
-- Version de PHP :  7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `cine-users`
--
CREATE DATABASE IF NOT EXISTS `cine-users` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `cine-users`;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lastname` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `age` int(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `lastname`, `firstname`, `login`, `password`, `age`) VALUES
(1, 'Thomas', 'Hippolyte', 'hippolyte', '$5$rounds=535000$6cbHayb03H4f5mU6$srnWhvx2wO5BwUPrtpTqWRQGXpxIyEn82kr8iDL6UZ8', 20),
(2, 'Chauveau', 'Bastien', 'bastien', '$5$rounds=535000$6cbHayb03H4f5mU6$srnWhvx2wO5BwUPrtpTqWRQGXpxIyEn82kr8iDL6UZ8', 20),
(3, 'Caillaud', 'Hugo', 'hugo', '$5$rounds=535000$6cbHayb03H4f5mU6$srnWhvx2wO5BwUPrtpTqWRQGXpxIyEn82kr8iDL6UZ8', 19),
(4, 'Galerne', 'Valentin', 'valentin', '$5$rounds=535000$6cbHayb03H4f5mU6$srnWhvx2wO5BwUPrtpTqWRQGXpxIyEn82kr8iDL6UZ8', 20),
(5, 'Dandouau', 'Alexandre', 'alexandre', '$5$rounds=535000$6cbHayb03H4f5mU6$srnWhvx2wO5BwUPrtpTqWRQGXpxIyEn82kr8iDL6UZ8', 21);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
