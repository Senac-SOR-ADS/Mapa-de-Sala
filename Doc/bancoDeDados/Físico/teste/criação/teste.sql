-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 11/09/2024 às 14:50
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mapasalat`
--
CREATE DATABASE IF NOT EXISTS `teste`
COLLATE 'utf8_bin';
USE `teste`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `area`
--

CREATE TABLE `area` (
  `idArea` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL UNIQUE COMMENT 'Nome da área',
  PRIMARY KEY (`idArea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `curso`
--

CREATE TABLE `curso` (
  `idCurso` int(11) NOT NULL AUTO_INCREMENT,
  `idArea` int(11) NOT NULL COMMENT 'ID da área associada',
  `nome` varchar(100) NOT NULL COMMENT 'Nome do curso',
  `oferta` varchar(50) NOT NULL UNIQUE COMMENT 'Oferta do curso',
  `periodo` enum('Manha','Tarde','Noite') NOT NULL COMMENT 'Período do curso',
  `cargaHoraria` int(11) NOT NULL COMMENT 'Carga horária do curso',
  `horasDia` time NOT NULL COMMENT 'Horas diárias de aula',
  `qtdAlunos` int(11) NOT NULL COMMENT 'Quantidade de alunos',
  PRIMARY KEY (`idCurso`),
  FOREIGN KEY (`idArea`) REFERENCES `area`(`idArea`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipamento`
--

CREATE TABLE `equipamento` (
  `idEquipamento` int(11) NOT NULL AUTO_INCREMENT,
  `idArea` int(11) NOT NULL COMMENT 'Id da área associada',
  `nome` varchar(100) NOT NULL COMMENT 'Nome do equipamento',
  `marca` varchar(100) NOT NULL COMMENT 'Marca do equipamento',
  `quantidade` int(11) NOT NULL COMMENT 'Quantidade do equipamento',
  PRIMARY KEY (`idEquipamento`),
  FOREIGN KEY (`idArea`) REFERENCES `area`(`idArea`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `sala`
--

CREATE TABLE `sala` (
  `idSala` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL COMMENT 'Nome da sala',
  `tipo` varchar(50) NOT NULL COMMENT 'Tipo da sala',
  `predio` varchar(10) NOT NULL COMMENT 'Prédio onde a sala está localizada',
  `equipamentos` varchar(255) NOT NULL COMMENT 'Equipamentos na sala',
  `capacidade` int(11) NOT NULL COMMENT 'Capacidade da sala',
  `observacao` varchar(255) DEFAULT NULL COMMENT 'Observação',
  PRIMARY KEY (`idSala`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------
--
-- Estrutura para tabela `pessoa`
--

CREATE TABLE `pessoa` (
  `idPessoa` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL COMMENT 'Nome da pessoa',
  `CPF_CNPJ` varchar(18) NOT NULL UNIQUE COMMENT 'CPF ou CNPJ',
  `nascimento` date NOT NULL COMMENT 'Data de nascimento',
  `telefone` varchar(15) NOT NULL COMMENT 'Telefone de contato',
  `email` varchar(100) NOT NULL UNIQUE COMMENT 'Email da pessoa',
  `cargo` enum('Comum','Suporte','Administrador') NOT NULL COMMENT 'Cargo ou função da pessoa',
  PRIMARY KEY (`idPessoa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------
--
-- Estrutura para tabela `login`
--

CREATE TABLE `login` (
  `idLogin` int(11) NOT NULL AUTO_INCREMENT,
  `idPessoa` int(11) NOT NULL COMMENT 'ID da pessoa associada',
  `email` varchar(100) NOT NULL UNIQUE COMMENT 'Email do login',
  `senha` varchar(100) NOT NULL COMMENT 'Senha do login',
  `nivelAcesso` ENUM('admin', 'suporte', 'user') NOT NULL DEFAULT 'user' COMMENT 'Nível de acesso do usuário',
  PRIMARY KEY (`idLogin`),
  FOREIGN KEY (`idPessoa`) REFERENCES `pessoa`(`idPessoa`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `reserva`
--

CREATE TABLE `reserva` (
  `idReserva` int(11) NOT NULL AUTO_INCREMENT,
  `idLogin` int(11) NOT NULL COMMENT 'ID do login associado',
  `idPessoa` int(11) NOT NULL COMMENT 'ID da pessoa associada',
  `idCurso` int(11) NOT NULL COMMENT 'ID do curso associado',
  `idSala` int(11) NOT NULL COMMENT 'ID da sala associada',
  `dia` date NOT NULL COMMENT 'Dia da reserva',
  `hrInicio` time NOT NULL COMMENT 'Horário de início',
  `hrFim` time NOT NULL COMMENT 'Horário de término',
  `chaveDevolvida` tinyint(1) NOT NULL COMMENT 'Se a chave já foi devolvida',
  `observacao` varchar(255) DEFAULT NULL COMMENT 'Observação',
  PRIMARY KEY (`idReserva`),
  FOREIGN KEY (`idLogin`) REFERENCES `login`(`idLogin`) ON DELETE CASCADE,
  FOREIGN KEY (`idPessoa`) REFERENCES `pessoa`(`idPessoa`) ON DELETE CASCADE,
  FOREIGN KEY (`idCurso`) REFERENCES `curso`(`idCurso`) ON DELETE CASCADE,
  FOREIGN KEY (`idSala`) REFERENCES `sala`(`idSala`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `ocupado`
--

CREATE TABLE `ocupado` (
  `qtdOcupado` int(11) NOT NULL COMMENT 'Quantidade de equipamentos ocupados',
  `idReserva` int(11) NOT NULL COMMENT 'ID de reserva associada',
  `idEquipamento` int(11) NOT NULL COMMENT 'ID do equipamento associado',
  FOREIGN KEY (`idReserva`) REFERENCES `reserva`(`idReserva`) ON DELETE CASCADE,
  FOREIGN KEY (`idEquipamento`) REFERENCES `equipamento` (`idEquipamento`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Finalizando a transação
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
