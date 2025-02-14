-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 13/11/2024 às 15:44
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
-- Banco de dados: `oficialt`
--
CREATE DATABASE IF NOT EXISTS `oficialt`
COLLATE 'utf8_bin';
USE `oficialt`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `area`
--

CREATE TABLE `area` (
  `idArea` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL COMMENT 'Nome da área'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `area`
--

INSERT INTO `area` (`idArea`, `nome`) VALUES
(1, 'Idiomas');

-- --------------------------------------------------------

--
-- Estrutura para tabela `curso`
--

CREATE TABLE `curso` (
  `idCurso` int(11) NOT NULL,
  `idArea` int(11) NOT NULL COMMENT 'ID da área associada',
  `nome` varchar(100) NOT NULL COMMENT 'Nome do curso',
  `oferta` varchar(50) NOT NULL COMMENT 'Oferta do curso',
  `periodo` enum('Manha','Tarde','Noite') NOT NULL COMMENT 'Período do curso',
  `cargaHoraria` int(11) NOT NULL COMMENT 'Carga horária do curso',
  `horasDia` time NOT NULL COMMENT 'Horas diárias de aula',
  `qtdAlunos` int(11) NOT NULL COMMENT 'Quantidade de alunos'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipamento`
--

CREATE TABLE `equipamento` (
  `idEquipamento` int(11) NOT NULL,
  `idArea` int(11) NOT NULL COMMENT 'Id da área associada',
  `nome` varchar(100) NOT NULL COMMENT 'Nome do equipamento',
  `marca` varchar(100) NOT NULL COMMENT 'Marca do equipamento',
  `quantidade` int(11) NOT NULL COMMENT 'Quantidade do equipamento'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `login`
--

CREATE TABLE `login` (
  `idLogin` int(11) NOT NULL,
  `idPessoa` int(11) NOT NULL COMMENT 'ID da pessoa associada',
  `email` varchar(100) NOT NULL COMMENT 'Email do login',
  `senha` varchar(100) NOT NULL COMMENT 'Senha do login',
  `nivelAcesso` enum('admin','user') NOT NULL DEFAULT 'user' COMMENT 'Nível de acesso do usuário'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `login`
--

INSERT INTO `login` (`idLogin`, `idPessoa`, `email`, `senha`, `nivelAcesso`) VALUES
(1, 1, 'admin@gmail.com', '$2b$12$VO8FkHuQ7bWjRSxsCvBD5OU0GPIDwwVA0Q.H3UF9Q7QW3dL6Nc/ha', 'admin');

-- --------------------------------------------------------

--
-- Estrutura para tabela `ocupado`
--

CREATE TABLE `ocupado` (
  `qtdOcupado` int(11) NOT NULL COMMENT 'Quantidade de equipamentos ocupados',
  `idReserva` int(11) NOT NULL COMMENT 'ID de reserva associada',
  `idEquipamento` int(11) NOT NULL COMMENT 'ID do equipamento associado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `pessoa`
--

CREATE TABLE `pessoa` (
  `idPessoa` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL COMMENT 'Nome da pessoa',
  `CPF_CNPJ` varchar(18) NOT NULL COMMENT 'CPF ou CNPJ',
  `nascimento` date NOT NULL COMMENT 'Data de nascimento',
  `telefone` varchar(15) NOT NULL COMMENT 'Telefone de contato',
  `email` varchar(100) NOT NULL COMMENT 'Email da pessoa',
  `cargo` enum('Comum','Suporte','Administrador') NOT NULL COMMENT 'Cargo ou função da pessoa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `pessoa`
--

INSERT INTO `pessoa` (`idPessoa`, `nome`, `CPF_CNPJ`, `nascimento`, `telefone`, `email`, `cargo`) VALUES
(1, 'admin', '123.456.789-05', '2024-11-13', '15 99878983', 'admin@gmail.com', 'Administrador');

-- --------------------------------------------------------

--
-- Estrutura para tabela `reserva`
--

CREATE TABLE `reserva` (
  `idReserva` int(11) NOT NULL,
  `idLogin` int(11) NOT NULL COMMENT 'ID do login associado',
  `idPessoa` int(11) NOT NULL COMMENT 'ID da pessoa associada',
  `idCurso` int(11) NOT NULL COMMENT 'ID do curso associado',
  `idSala` int(11) NOT NULL COMMENT 'ID da sala associada',
  `dia` date NOT NULL COMMENT 'Dia da reserva',
  `hrInicio` time NOT NULL COMMENT 'Horário de início',
  `hrFim` time NOT NULL COMMENT 'Horário de término',
  `chaveDevolvida` tinyint(1) NOT NULL COMMENT 'Se a chave já foi devolvida',
  `observacao` varchar(255) DEFAULT NULL COMMENT 'Observação'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Estrutura para tabela `sala`
--

CREATE TABLE `sala` (
  `idSala` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL COMMENT 'Nome da sala',
  `tipo` varchar(50) NOT NULL COMMENT 'Tipo da sala',
  `predio` varchar(10) NOT NULL COMMENT 'Prédio onde a sala está localizada',
  `equipamentos` varchar(255) NOT NULL COMMENT 'Equipamentos na sala',
  `capacidade` int(11) NOT NULL COMMENT 'Capacidade da sala',
  `observacao` varchar(255) DEFAULT NULL COMMENT 'Observação'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `sala`
--

INSERT INTO `sala` (`idSala`, `nome`, `tipo`, `predio`, `equipamentos`, `capacidade`, `observacao`) VALUES
(1, 'C01', 'Laboratório', 'Prédio 1', '1', 1, 'Nenhuma'),
(2, 'C02', 'Laboratório', 'Prédio 1', '1', 1, ''),
(3, 'C03', 'Laboratório', 'Prédio 1', '1', 1, ''),
(4, 'C04', 'Laboratório', 'Prédio 1', '1', 1, ''),
(5, 'C05', 'Laboratório', 'Prédio 1', '1', 1, ''),
(6, 'C06', 'Laboratório', 'Prédio 1', '1', 1, ''),
(7, 'C07', 'Laboratório', 'Prédio 1', '1', 1, ''),
(8, 'C08', 'Laboratório', 'Prédio 1', '1', 1, ''),
(9, 'C09', 'Laboratório', 'Prédio 1', '1', 1, ''),
(10, 'C10', 'Laboratório', 'Prédio 1', '1', 1, ''),
(11, 'C11', 'Laboratório', 'Prédio 1', '1', 1, ''),
(12, 'C12', 'Laboratório', 'Prédio 1', '1', 1, ''),
(13, 'D01', 'Comum', 'Prédio 1', '1', 1, ''),
(14, 'D02', 'Comum', 'Prédio 1', '1', 1, ''),
(15, 'D03', 'Comum', 'Prédio 1', '1', 1, ''),
(16, 'D04', 'Comum', 'Prédio 1', '1', 1, ''),
(17, 'D05', 'Comum', 'Prédio 1', '1', 1, ''),
(18, 'D06', 'Comum', 'Prédio 1', '1', 1, ''),
(19, 'D07', 'Laboratório', 'Prédio 1', '1', 1, ''),
(20, 'D08', 'Comum', 'Prédio 1', '1', 1, ''),
(21, 'D09', 'Comum', 'Prédio 1', '1', 1, ''),
(22, 'D10', 'Comum', 'Prédio 1', '1', 1, ''),
(23, 'D11', 'Comum', 'Prédio 1', '1', 1, ''),
(24, 'D12', 'Laboratório', 'Prédio 1', '1', 1, ''),
(25, 'D13', 'Laboratório', 'Prédio 1', '1', 1, ''),
(26, 'Auditório', 'Comum', 'Prédio 1', '1', 1, ''),
(27, 'Biblioteca', 'Comum', 'Prédio 2', '1', 1, ''),
(28, 'Hall Auditório', 'Comum', 'Prédio 1', '1', 1, ''),
(29, 'Jardim Pedagógico - Canaletões', 'Área Externa', 'Prédio 2', '1', 1, ''),
(30, 'Jardim Pedagógico - Mandala', 'Área Externa', 'Prédio 2', '1', 1, ''),
(31, 'Jardim Pedagógico - Sala de Aula', 'Área Externa', 'Prédio 2', '1', 1, ''),
(32, 'Arquibancada', 'Área Externa', 'Prédio 2', '1', 1, ''),
(33, 'Área de Convívio', 'Área Externa', 'Prédio 2', '1', 1, ''),
(34, 'H01', 'Laboratório', 'Prédio 2', '1', 1, ''),
(35, 'J01', 'Laboratório', 'Prédio 2', '1', 1, ''),
(36, 'J02', 'Laboratório', 'Prédio 2', '1', 1, ''),
(37, 'J03', 'Laboratório', 'Prédio 2', '1', 1, ''),
(38, 'J04', 'Laboratório', 'Prédio 2', '1', 1, ''),
(39, 'J05', 'Laboratório', 'Prédio 2', '1', 1, ''),
(40, 'J06', 'Laboratório', 'Prédio 2', '1', 1, ''),
(41, 'J07', 'Laboratório', 'Prédio 2', '1', 1, ''),
(42, 'J08', 'Laboratório', 'Prédio 2', '1', 1, ''),
(43, 'K01', 'Laboratório', 'Prédio 2', '1', 1, ''),
(44, 'K02', 'Laboratório', 'Prédio 2', '1', 1, ''),
(45, 'K03', 'Laboratório', 'Prédio 2', '1', 1, ''),
(46, 'K04', 'Laboratório', 'Prédio 2', '1', 1, ''),
(47, 'K05', 'Laboratório', 'Prédio 2', '1', 1, ''),
(48, 'K06', 'Laboratório', 'Prédio 2', '1', 1, ''),
(49, 'K07', 'Laboratório', 'Prédio 2', '1', 1, ''),
(50, 'Passarela - Área de Baixo', 'Área Externa', 'Prédio 2', '1', 1, ''),
(51, 'PET - Ficticio', 'Comum', 'Prédio 2', '1', 1, ''),
(52, 'I01', 'Comum', 'Prédio 2', '1', 1, ''),
(53, 'I02', 'Comum', 'Prédio 2', '1', 1, ''),
(54, 'I03', 'Comum', 'Prédio 2', '1', 1, ''),
(55, 'I04', 'Comum', 'Prédio 2', '1', 1, ''),
(56, 'I05', 'Comum', 'Prédio 2', '1', 1, ''),
(57, 'I06', 'Comum', 'Prédio 2', '1', 1, ''),
(58, 'I07', 'Comum', 'Prédio 2', '1', 1, ''),
(59, 'I08', 'Comum', 'Prédio 2', '1', 1, ''),
(60, 'I09', 'Comum', 'Prédio 2', '1', 1, '');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`),
  ADD UNIQUE KEY `nome` (`nome`);

--
-- Índices de tabela `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`idCurso`),
  ADD KEY `idArea` (`idArea`),
  ADD UNIQUE KEY `oferta` (`oferta`);

--
-- Índices de tabela `equipamento`
--
ALTER TABLE `equipamento`
  ADD PRIMARY KEY (`idEquipamento`),
  ADD KEY `idArea` (`idArea`);

--
-- Índices de tabela `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`idLogin`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `idPessoa` (`idPessoa`);

--
-- Índices de tabela `ocupado`
--
ALTER TABLE `ocupado`
  ADD KEY `idReserva` (`idReserva`),
  ADD KEY `idEquipamento` (`idEquipamento`);

--
-- Índices de tabela `pessoa`
--
ALTER TABLE `pessoa`
  ADD PRIMARY KEY (`idPessoa`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `CPF_CNPJ` (`CPF_CNPJ`);

--
-- Índices de tabela `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`idReserva`),
  ADD KEY `idLogin` (`idLogin`),
  ADD KEY `idPessoa` (`idPessoa`),
  ADD KEY `idCurso` (`idCurso`),
  ADD KEY `idSala` (`idSala`);

--
-- Índices de tabela `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`idSala`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `area`
--
ALTER TABLE `area`
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `curso`
--
ALTER TABLE `curso`
  MODIFY `idCurso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `equipamento`
--
ALTER TABLE `equipamento`
  MODIFY `idEquipamento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `idLogin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `pessoa`
--
ALTER TABLE `pessoa`
  MODIFY `idPessoa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `reserva`
--
ALTER TABLE `reserva`
  MODIFY `idReserva` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `sala`
--
ALTER TABLE `sala`
  MODIFY `idSala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `curso`
--
ALTER TABLE `curso`
  ADD CONSTRAINT `curso_ibfk_1` FOREIGN KEY (`idArea`) REFERENCES `area` (`idArea`) ON DELETE CASCADE;

--
-- Restrições para tabelas `equipamento`
--
ALTER TABLE `equipamento`
  ADD CONSTRAINT `equipamento_ibfk_1` FOREIGN KEY (`idArea`) REFERENCES `area` (`idArea`) ON DELETE CASCADE;

--
-- Restrições para tabelas `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `login_ibfk_1` FOREIGN KEY (`idPessoa`) REFERENCES `pessoa` (`idPessoa`) ON DELETE CASCADE;

--
-- Restrições para tabelas `ocupado`
--
ALTER TABLE `ocupado`
  ADD CONSTRAINT `ocupado_ibfk_1` FOREIGN KEY (`idReserva`) REFERENCES `reserva` (`idReserva`) ON DELETE CASCADE,
  ADD CONSTRAINT `ocupado_ibfk_2` FOREIGN KEY (`idEquipamento`) REFERENCES `equipamento` (`idEquipamento`) ON DELETE CASCADE;

--
-- Restrições para tabelas `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`idLogin`) REFERENCES `login` (`idLogin`) ON DELETE CASCADE,
  ADD CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`idPessoa`) REFERENCES `pessoa` (`idPessoa`) ON DELETE CASCADE,
  ADD CONSTRAINT `reserva_ibfk_3` FOREIGN KEY (`idCurso`) REFERENCES `curso` (`idCurso`) ON DELETE CASCADE,
  ADD CONSTRAINT `reserva_ibfk_4` FOREIGN KEY (`idSala`) REFERENCES `sala` (`idSala`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
