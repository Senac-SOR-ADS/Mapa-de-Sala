-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28/08/2024 às 16:53
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
-- Banco de dados: `teste`
CREATE DATABASE IF NOT EXISTS `teste`
COLLATE 'utf8_bin';
USE `teste`;

--

-- --------------------------------------------------------

--
-- Estrutura para tabela `area`
--

CREATE TABLE `area` (
  `idArea` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `area`
--

INSERT INTO `area` (`idArea`, `nome`) VALUES
(1, 'Tecnologia da Informação'),
(2, 'Beleza e Estética'),
(3, 'Bem-Estar'),
(4, 'Comunicação e Marketing'),
(5, 'Desenvolvimento Social'),
(6, 'Design'),
(7, 'Educação'),
(8, 'Gastronomia'),
(9, 'Gestão e Negócios'),
(10, 'idiomas'),
(11, 'Moda'),
(12, 'Saúde');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cursos`
--

CREATE TABLE `curso` (
  `idCurso` int(11) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `oferta` varchar(50) NOT NULL,
  `periodo` varchar(50) NOT NULL,
  `cargaHoraria` int(11) NOT NULL,
  `horasDia` time NOT NULL,
  `qtdAlunos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `cursos`
--

INSERT INTO `curso` (`idCurso`, `idArea`, `nome`, `oferta`, `periodo`, `cargaHoraria`, `horasDia`, `qtdAlunos`) VALUES
(1, 1, 'Power BI', '245685', 'Manhã', 1200, '03:30:00', 17),
(2, 3, 'Reiki', '487563', 'Tarde', 1080, '00:00:02', 9),
(3, 4, 'Documentário', '478651', 'Manhã', 72, '00:00:04', 7),
(4, 8, 'Doces Finos', '532148', 'Noite', 24, '00:00:02', 25),
(5, 9, 'Gestão Fiscal', '856432', 'Tarde', 46, '00:00:04', 30),
(6, 2, 'Alongamento de Cílios', '214589', 'Manhã', 65, '00:00:02', 12),
(7, 12, 'Atendente de Farmacia', '547893', 'Tarde', 58, '00:00:04', 24);

-- --------------------------------------------------------

--
-- Estrutura para tabela `equipamentos`
--

CREATE TABLE `equipamento` (
  `idEquipamento` int(11) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `quantidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `equipamentos`
--

INSERT INTO `equipamento` (`idEquipamento`, `idArea`, `nome`, `marca`, `quantidade`) VALUES
(1, 3, 'Maca', 'seila', 7),
(2, 5, 'cadeira', 'hyperX', 4),
(3, 8, 'Concha', 'Eletrolux', 40),
(4, 11, 'Manequim', 'Riachuelo', 9),
(5, 1, 'Mouse', 'Dell', 20);

-- --------------------------------------------------------

--
-- Estrutura para tabela `login`
--

CREATE TABLE `login` (
  `idLogin` int(11) NOT NULL,
  `idPessoa` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `login`
--

INSERT INTO `login` (`idLogin`, `idPessoa`, `email`, `senha`) VALUES
(1, 5, 'elisa-assis95@amoreencantos.com', 'senha123'),
(2, 1, 'emailgenerico@gmail.com', 'senha456'),
(3, 8, 'maria_isabelly_nascimento@oticascarol.com.br', 'senha101112');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pessoas`
--

CREATE TABLE `pessoa` (
  `idPessoa` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `CPF_CNPJ` varchar(18) NOT NULL,
  `nascimento` date NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `cargo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `pessoas`
--

INSERT INTO `pessoa` (`idPessoa`, `nome`, `CPF_CNPJ`, `nascimento`, `telefone`, `email`, `cargo`) VALUES
(1, 'Gabriel Alcantara Dias Prestes', '663.300.190-88', '2000-08-15', '(61) 3615-2089', 'emailgenerico@gmail.com', 'Apoio'),
(2, 'Laís Malu Rebeca da Paz', '192.458.327-59', '1981-08-20', '(46) 2578-6303', 'potoasdfeafafemdfmakfmskmfkmfkamamd@gmail.com', 'Patrimônio'),
(3, 'Enzo Diogo Martin Silva', '931.825.487-35', '1998-07-04', '(79) 3963-7319', 'fdsfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsd@gmail.com', 'Limpeza'),
(4, 'Renato Bernardo Yuri das Neves', '727.882.631-47', '1987-03-06', '(71) 3860-2221', 'fdsfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsd@gmail.com', 'Docente'),
(5, 'Elisa Mariane Adriana Assis', '44.196.017/0001-31', '1960-02-01', '(63) 2801-0368', 'elisa-assis95@amoreencantos.com', 'Chefe'),
(6, 'Marcelo Vinicius Tiago Freitas', '054.675.039-79', '1992-03-17', '(68) 3937-9429', 'marcelo-freitas77@iclaud.com', 'Diretor'),
(7, 'Marcela Alessandra Gomes', '284.319.150-56', '2001-02-09', '(42) 3667-9065', 'marcela_alessandra_gomes@callan.com.br', 'Manutenção'),
(8, 'Maria Isabelly Jéssica Nascimento', '71.386.002/0001-09', '1992-01-19', '(44) 2533-0657', 'maria_isabelly_nascimento@oticascarol.com.br', 'Apoio'),
(9, 'Marcelo Kauê Lorenzo Lima', '533.390.123-69', '1973-04-01', '(27) 2579-5552', 'marcelo_kaue_lima@me.com.br', 'Jardineiro'),
(10, 'Raimundo Ricardo Anderson Caldeira', '28.653.414/0001-39', '1972-02-16', '(95) 3631-8354', 'raimundo_ricardo_caldeira@outlook.com', 'Patrimônio');

-- --------------------------------------------------------

--
-- Estrutura para tabela `reserva`
--

CREATE TABLE `reserva` (
  `idReserva` int(11) NOT NULL,
  `idEquipamento` int(11) DEFAULT NULL,
  `idLogin` int(11) NOT NULL,
  `idPessoa` int(11) NOT NULL,
  `idCurso` int(11) NOT NULL,
  `idSala` int(11) NOT NULL,
  `dia` date NOT NULL,
  `hrInicio` time NOT NULL,
  `hrFim` time NOT NULL,
  `observacao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `reserva`
--

INSERT INTO `reserva` (`idReserva`, `idEquipamento`, `idLogin`, `idPessoa`, `idCurso`, `idSala`, `dia`, `hrInicio`, `hrFim`, `observacao`) VALUES
(1, 3, 1, 4, 6, 2, '2024-09-02', '08:00:00', '12:00:00', NULL),
(4, NULL, 3, 5, 4, 9, '2024-08-29', '19:00:00', '22:30:00', NULL),
(5, 3, 2, 7, 4, 2, '2024-08-29', '13:00:00', '17:00:00', 'Uma boca de um fogão quebrado');

-- --------------------------------------------------------

--
-- Estrutura para tabela `sala`
--

CREATE TABLE `sala` (
  `idSala` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `predio` varchar(10) NOT NULL,
  `equipamentos` varchar(255) NOT NULL,
  `capacidade` int(11) NOT NULL,
  `observacao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `sala`
--

INSERT INTO `sala` (`idSala`, `nome`, `tipo`, `predio`, `equipamentos`, `capacidade`, `observacao`) VALUES
(1, 'j01', 'labolatorio de informatica', '2', '30', 30, 'ar-condicionado quebrado'),
(2, 'cozinha', 'cozinha industrial', '1', '2fogao industrial, 20mesas, 30 cadeiras', 40, ''),
(3, 'h03', 'Sala de idiomas', '2', '30computadores, 30 cadeiras30', 30, '10 computadores em manutenção'),
(4, 'jardim', 'area externa', '2', 'mesas grandes 2, 4 bancos grandes', 0, 'guarda sol danificcados'),
(5, 'sala q3', 'Studio de som', '1', 'teclado, microfone, abafador de audio', 15, ''),
(6, 'Sala de hardware', 'lab de infraestrutura', '2', 'hack de roteadores, painel de controles, cabeamento de internet, peças de computadores', 25, 'painel de controles queimados'),
(7, 'Sala ensino meido E1', 'sala convencional ensino medio', '1', '13 notebooks, uma lousa digital', 35, ''),
(8, 'lab quimica', 'laboratorio', '2', 'produtos quimicos, esqueleto', 20, 'Produtos perigosos, uso de EPI obrigatorio'),
(9, 'Estetica', 'lab de Estetica', '2', 'pinças, maquiagem, maca', 18, ''),
(10, 'informatica', 'sala de informatica', '1', '25 computadores', 25, 'Somente 15 computadores funcionando');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`);

--
-- Índices de tabela `cursos`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`idCurso`),
  ADD KEY `area_curso` (`idArea`);

--
-- Índices de tabela `equipamentos`
--
ALTER TABLE `equipamento`
  ADD PRIMARY KEY (`idEquipamento`),
  ADD KEY `area_equipamento` (`idArea`);

--
-- Índices de tabela `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`idLogin`),
  ADD KEY `pessoa_login` (`idPessoa`);

--
-- Índices de tabela `pessoas`
--
ALTER TABLE `pessoa`
  ADD PRIMARY KEY (`idPessoa`);

--
-- Índices de tabela `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`idReserva`),
  ADD KEY `equipamento_reserva` (`idEquipamento`),
  ADD KEY `pessoa_reserva` (`idPessoa`),
  ADD KEY `curso_reserva` (`idCurso`),
  ADD KEY `sala_reserva` (`idSala`),
  ADD KEY `login_reserva` (`idLogin`);

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
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `cursos`
--
ALTER TABLE `curso`
  MODIFY `idCurso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `equipamentos`
--
ALTER TABLE `equipamento`
  MODIFY `idEquipamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `idLogin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `pessoas`
--
ALTER TABLE `pessoa`
  MODIFY `idPessoa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `reserva`
--
ALTER TABLE `reserva`
  MODIFY `idReserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `sala`
--
ALTER TABLE `sala`
  MODIFY `idSala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `cursos`
--
ALTER TABLE `curso`
  ADD CONSTRAINT `area_curso` FOREIGN KEY (`idArea`) REFERENCES `area` (`idArea`);

--
-- Restrições para tabelas `equipamentos`
--
ALTER TABLE `equipamento`
  ADD CONSTRAINT `area_equipamento` FOREIGN KEY (`idArea`) REFERENCES `area` (`idArea`);

--
-- Restrições para tabelas `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `pessoa_login` FOREIGN KEY (`idPessoa`) REFERENCES `pessoa` (`idPessoa`);

--
-- Restrições para tabelas `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `curso_reserva` FOREIGN KEY (`idCurso`) REFERENCES `curso` (`idCurso`),
  ADD CONSTRAINT `equipamento_reserva` FOREIGN KEY (`idEquipamento`) REFERENCES `equipamento` (`idEquipamento`),
  ADD CONSTRAINT `login_reserva` FOREIGN KEY (`idLogin`) REFERENCES `login` (`idLogin`),
  ADD CONSTRAINT `pessoa_reserva` FOREIGN KEY (`idPessoa`) REFERENCES `pessoa` (`idPessoa`),
  ADD CONSTRAINT `sala_reserva` FOREIGN KEY (`idSala`) REFERENCES `sala` (`idSala`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
