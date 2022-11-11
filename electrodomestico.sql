-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-11-2022 a las 03:42:25
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30
--NOMBRE DE BASE DE DATOS ES centro_comercial

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `centro_comercial`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `electrodomestico`
--

CREATE TABLE `electrodomestico` (
  `producto` varchar(30) NOT NULL,
  `valor` varchar(8) NOT NULL,
  `stock` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `electrodomestico`
--

INSERT INTO `electrodomestico` (`producto`, `valor`, `stock`) VALUES
('lavadora', '29990', '12'),
('microonda', '30000', '5'),
('refrigerador', '89990', '6');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
