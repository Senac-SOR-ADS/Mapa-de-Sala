-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 14/02/2025 às 12:30
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
--
CREATE DATABASE IF NOT EXISTS `teste`
COLLATE 'utf8_bin';
USE `teste`;
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
(14, 'Artes'),
(2, 'Beleza e Estética'),
(3, 'Bem-Estar'),
(95, 'Cinema'),
(4, 'Comunicação e Marketing'),
(5, 'Desenvolvimento Social'),
(19, 'Desenvolvimento de Sistemas'),
(6, 'Design'),
(7, 'Educação'),
(13, 'Ensino Médio'),
(8, 'Gastronomia'),
(9, 'Gestão e Negócios'),
(10, 'Idiomas'),
(27, 'Jogos'),
(24, 'Medicina'),
(11, 'Moda'),
(33, 'Musicas'),
(20, 'Pirotecnia'),
(21, 'Pirotecnia Profissional'),
(22, 'Pirotecnia Profissional2'),
(23, 'Pirotecnia Profissional3'),
(15, 'Radiologia'),
(34, 'Relojoaria'),
(12, 'Saúde1'),
(1, 'Tecnologia da Informação'),
(81, 'abluablueablue'),
(93, 'dddas'),
(92, 'dddd'),
(83, 'operador de trator1'),
(96, 'teste asasa d'),
(94, 'teste3'),
(82, 'testeteste1');

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

--
-- Despejando dados para a tabela `curso`
--

INSERT INTO `curso` (`idCurso`, `idArea`, `nome`, `oferta`, `periodo`, `cargaHoraria`, `horasDia`, `qtdAlunos`) VALUES
(1, 14, 'Power BI', '245685', 'Tarde', 400, '04:00:00', 10),
(2, 14, 'Reiki', '487563', 'Tarde', 200, '04:00:00', 13),
(3, 95, 'Documentário', '478651', 'Tarde', 200, '00:00:03', 20),
(4, 8, 'Doces Finos', '532148', 'Noite', 24, '02:00:00', 25),
(5, 9, 'Gestão Fiscal', '856432', 'Tarde', 0, '04:00:00', 30),
(6, 2, 'Alongamento de Cílios', '214589', 'Tarde', 300, '00:00:04', 15),
(7, 12, 'Atendente de Farmacia', '547893', 'Tarde', 58, '04:00:00', 24),
(8, 10, 'Libras', '2478947', 'Tarde', 120, '04:00:00', 17),
(9, 14, 'Ceramica', '457863', 'Noite', 24, '11:20:00', 13),
(10, 33, 'piano', '40028', 'Manha', 123, '04:00:00', 21),
(11, 19, 'Desenvolvimento de Software', '707070', 'Noite', 1200, '04:00:00', 24),
(43, 20, 'Pirotecnia Amadora', '123141', 'Manha', 600, '04:00:00', 30),
(45, 95, 'Fotografia Cinematográfica', '223442', 'Noite', 1000, '00:00:04', 12),
(46, 19, 'React Master', '123', 'Manha', 900, '02:00:00', 24),
(47, 14, 'Mestre do Python', '10', 'Manha', 2000, '08:00:00', 10),
(49, 20, 'Tortuga O\Zil', '1111', 'Noite', 600, '01:00:00', 10);

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

--
-- Despejando dados para a tabela `equipamento`
--

INSERT INTO `equipamento` (`idEquipamento`, `idArea`, `nome`, `marca`, `quantidade`) VALUES
(1, 3, 'Maca', 'seila', 7),
(2, 5, 'cadeira', 'hyperX', 4),
(3, 8, 'Concha', 'Eletrolux', 40),
(4, 11, 'Manequim', 'Riachuelo', 9),
(5, 1, 'Mouse', 'Dell', 20),
(20, 1, 'Monitor', 'Dell', 10),
(21, 8, 'Panela de Pressão', 'Eletrolux', 20);

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
(1, 1, 'emailgenerico@gmail.com', '$2b$12$TeDXdI2df2gEeyBLHokhieNpDaOu5d/.DiDGba3UG0xMlkFpYKNSy', 'user'),
(5, 2, 'potoasdfeafafemdfmakfmskmfkmfkamamd@gmail.com', 'lais123', 'admin'),
(6, 8, 'maria_isabelly_nascimento@oticascarol.com.br', '812394', 'user'),
(7, 6, 'marcelo-freitas77@iclaud.com', 'marcelo123', 'user'),
(8, 3, 'enzo@gmail.com', 'enzo', 'admin'),
(9, 9, 'otavio@g.com', '$2b$12$dhPYm9IF3MoSr98ETiDhju7OBjbxFePcSjzk9ZQYVv7.5j/aZDLtG', 'admin'),
(10, 10, 'gabriel@g.com', '$2b$12$tr7tB8lt/7B3k1pAePn7xuuI4JTSMEXwPEkrMUfPTPtOO9kZ0eCOe', 'admin'),
(11, 11, 'surik@g.com', '$2b$12$cLiPvOKDdMe5aXvX3U1Vo.Qg2lsxber43UEcRmf06DlN6.5hGdI/2', 'admin'),
(12, 12, 'brunor@g.com', '$2b$12$FovfQZcr3uOVgAaaIcVNFeqBDFpklnt630sRAGzFpHY./Q4je1CRa', 'admin'),
(13, 13, 'nickolas@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(14, 14, 'brunom@g.com', '$2b$12$CERaRii.yNr65NHv.Xj34eDi27DpZe728MkR/UjUWXyLgDelYLkv6', 'admin'),
(15, 15, 'samuel@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(16, 16, 'jeff@g.com', '$2b$12$J8rS/h0FuxWTmC6vsfYo9.f2DaqiYhUnyX4bqCzHXdSGRKlvlLZBO', 'admin'),
(24, 69, 'otaviootavi@g.com', '$2b$12$AHC4eij9L5HsCzzk/exo8OCCMa3WOQuzd2k1yLA8FUzPhwCNBc4eO', 'user'),
(25, 70, 'daniele.gandrade@sp.senac.br', '$2b$12$NPIBEMo90pYnO0eyEC/iGe7llIvcvch8YC0uZHPRWtGY4QIYS0qRq', 'user'),
(26, 71, 'uhaua@d.com', '$2b$12$J8rS/h0FuxWTmC6vsfYo9.f2DaqiYhUnyX4bqCzHXdSGRKlvlLZBO', 'user'),
(27, 72, '4564@g.com', '$2b$12$z9u2pymx/CCTsWOrNM/NC.87ka99S6CCe3fVAWcku5L5/XH7o/S3a', 'user'),
(28, 73, '545@g.com', '$2b$12$xiNdlX6Db.U4OKPGwNhqqO5vO4ypEyaaGQa6rkFfZePuumrV/6Jhu', 'user'),
(29, 74, '5465@g.com', '$2b$12$ELPgR2jOQIgwxfcS7Hfau.1RgjUKwd2pzKPE5nunoAIh1BxKkVx.6', 'user'),
(30, 75, 'hh@d.com', '$2b$12$HVEnpguShI3dyXZCbS.6fOa.a7zTWV.tg6QcOFq72ZYLctnzZimE2', 'user'),
(31, 76, 'hhh@gg.com', '$2b$12$lLyn/OuG/2K/6zjASy2lherMStSfF8gKW3qvHlvWtdaj19LaLf2g.', 'admin'),
(33, 78, 'hh@hh.com', '$2b$12$DLcHoswfZsrq.qhLkd7aT.qPGPf2FtNCejnPb0m8ptnaelacPFqPq', 'admin'),
(34, 79, 'luciano@java.com', '$2b$12$Acz71TcWtyrN7mZZatufZ.3q8Dr3CVRYdGo5IrIy4J3yQniYUeQle', 'admin'),
(35, 80, '4654@g.com', '$2b$12$BSP9C.p8IvWaIiTvfW2JNeAIOQRa7kFji0EEEMeD0kCDJIfB7n0AS', 'user'),
(37, 82, 'beltrano@g.com', '$2b$12$yZYfRxtRB1q8kXk4GQOFueiswueop.VqP02Jtkz6Yd1lf42RxwN3G', 'admin'),
(38, 83, 'teste@teste.teste', '$2b$12$1eqImJuoXV1tA0KzSvQbMObpx6ueO9yrcIT0kO6crQk.a4jV2dJBe', 'user');

-- --------------------------------------------------------

--
-- Estrutura para tabela `ocupado`
--

CREATE TABLE `ocupado` (
  `qtdOcupado` int(11) NOT NULL COMMENT 'Quantidade de equipamentos ocupados',
  `idReserva` int(11) NOT NULL COMMENT 'ID de reserva associada',
  `idEquipamento` int(11) NOT NULL COMMENT 'ID do equipamento associado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `ocupado`
--

INSERT INTO `ocupado` (`qtdOcupado`, `idReserva`, `idEquipamento`) VALUES
(2, 6, 2),
(10, 6, 5),
(10, 6, 5),
(5, 11, 5),
(5, 7, 2),
(1, 7, 2),
(10, 18, 4),
(2, 19, 3);

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
(1, 'Enzo Silva Carvalho', '663.300.190-69', '2024-12-09', '(61) 3615-2080', 'emailgenerico@gmail.com', 'Administrador'),
(2, 'Laís Malu Rebeca da Paz', '192.458.327-59', '1981-08-20', '(46) 2578-6303', 'potoasdfeafafemdfmakfmskmfkmfkamamd@gmail.com', 'Comum'),
(3, 'Enzo Diogo Martin Silva', '931.825.487-35', '1998-07-04', '(79) 3963-7319', 'fdsfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsd@gmail.com', 'Suporte'),
(4, 'Renato Bernardo Yuri das Neves', '727.882.631-47', '1987-03-06', '(71) 3860-2221', 'emailqualquer@gmail.com', 'Administrador'),
(5, 'Elisa Mariane Adriana Assis', '44.196.017/0001-31', '1960-02-01', '(63) 2801-0368', 'elisa-assis95@amoreencantos.com', 'Suporte'),
(6, 'Marcelo Vinicius Tiago Freitas', '054.675.039-79', '1992-03-17', '(68) 3937-9429', 'marcelo-freitas77@iclaud.com', 'Comum'),
(7, 'Marcela Alessandra Gomes', '284.319.150-56', '2001-02-09', '(42) 3667-9065', 'marcela_alessandra_gomes@callan.com.br', 'Suporte'),
(8, 'Maria Isabelly Jéssica Nascimento', '71.386.002/0001-09', '1992-01-19', '(44) 2533-0657', 'maria_isabelly_nascimento@oticascarol.com.br', 'Suporte'),
(9, 'Otavio', '533.390.123-69', '1973-04-01', '(27) 2579-5552', 'otavio@g.com', 'Administrador'),
(10, 'Gabriel', '28.653.414/0001-39', '1972-02-16', '(95) 3631-8354', 'gabriel@g.com', 'Suporte'),
(11, 'Ricardo', '123.123.123-90', '2006-10-19', '(15) 99120-6869', 'richard@g.com', 'Comum'),
(12, 'Bruno Rodrigues', '123.456.789-00', '2006-10-19', '(15) 99120-6869', 'brunor@gmail.com', 'Comum'),
(13, 'Nickolas', '123.456.789-01', '2006-10-19', '(15) 99120-6869', 'nickolas@gmail.com', 'Comum'),
(14, 'Bruno Mendes', '123.456.789-02', '2006-10-19', '15991206869', 'brunom@gmail.com', 'Administrador'),
(15, 'Samuel', '123.456.789-03', '2006-10-19', '(15) 99120-6869', 'samuel@gmail.com', 'Suporte'),
(16, 'Jeff', '123.456.789-04', '2006-10-19', '(15) 99120-6869', 'jeff@gmail.com', 'Suporte'),
(69, 'Otavioteste', '123.456.789-05', '2024-12-02', '40028922', 'otaviootavi@g.com', 'Suporte'),
(70, 'Daniele Gutierrez', '123.456.789-24', '2024-12-02', '11940318617', 'daniele.gandrade@sp.senac.br', 'Suporte'),
(71, 'Bruno Test', '546.465.464-09', '2024-12-06', '22222222222', 'uhaua@d.com', 'Suporte'),
(72, 'Testsssssss', '645.645.645-64', '2024-12-06', '111111111111', '4564@g.com', 'Comum'),
(73, 'Hhuahua', '456.465.456-65', '2024-12-06', '546546', '545@g.com', 'Comum'),
(74, 'Qqqq', '546.456.492-94', '2024-12-06', '56456456', '5465@g.com', 'Comum'),
(75, 'Bruno', '123.456.789-14', '2024-12-06', '1599999999', 'hh@d.com', 'Comum'),
(76, 'Brunokkk', '112.313.213-11', '2000-12-22', '15222222222', 'hhh@gg.com', 'Administrador'),
(78, 'Testttttt', '322.132.323-39', '2024-12-06', '1321321', 'hh@hh.com', 'Administrador'),
(79, 'Luciano Da Silva Sauro', '123.456.782-00', '2024-12-06', '15999999999', 'luciano@java.com', 'Administrador'),
(80, 'Bbbb', '456.465.481-94', '2024-12-06', '56456456', '4654@g.com', 'Comum'),
(82, 'Fulano Da Silva', '123.456.789-84', '2024-12-16', '123456789', 'fulano@g.com', 'Comum'),
(83, 'Teste', '123.456.789-95', '2024-12-03', '123456879', 'teste@teste.teste', 'Suporte');

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

--
-- Despejando dados para a tabela `reserva`
--

INSERT INTO `reserva` (`idReserva`, `idLogin`, `idPessoa`, `idCurso`, `idSala`, `dia`, `hrInicio`, `hrFim`, `chaveDevolvida`, `observacao`) VALUES
(6, 1, 1, 7, 18, '2024-09-15', '08:00:00', '12:00:00', 1, NULL),
(7, 5, 5, 6, 19, '2024-09-11', '10:00:00', '17:00:00', 1, NULL),
(8, 7, 1, 3, 20, '2024-10-15', '17:00:00', '22:30:00', 1, NULL),
(11, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 1, 'Nenhuma'),
(13, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(14, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(15, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(16, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(17, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(18, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(19, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(20, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(21, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(22, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(23, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(24, 1, 3, 2, 15, '2024-09-20', '08:00:00', '12:00:00', 0, 'Nenhuma'),
(25, 1, 3, 5, 11, '2024-09-15', '08:00:00', '12:00:00', 1, NULL),
(26, 1, 3, 5, 11, '2024-09-15', '09:00:00', '11:00:00', 1, NULL),
(27, 1, 3, 5, 15, '2024-09-20', '09:00:00', '10:00:00', 1, NULL),
(29, 8, 1, 1, 11, '2024-11-26', '00:00:00', '00:00:00', 0, ''),
(30, 8, 1, 1, 11, '2024-11-27', '00:00:00', '00:00:00', 0, ''),
(31, 8, 1, 1, 11, '2024-11-28', '00:00:00', '00:00:00', 0, ''),
(32, 8, 1, 1, 11, '2024-11-29', '00:00:00', '00:00:00', 0, ''),
(33, 8, 1, 1, 11, '2024-11-30', '00:00:00', '00:00:00', 0, ''),
(34, 8, 1, 1, 11, '2024-12-02', '00:00:00', '00:00:00', 0, ''),
(35, 8, 1, 1, 11, '2024-12-03', '00:00:00', '00:00:00', 0, ''),
(36, 8, 1, 1, 11, '2024-12-04', '00:00:00', '00:00:00', 0, ''),
(37, 8, 1, 1, 11, '2024-12-05', '00:00:00', '00:00:00', 0, ''),
(38, 8, 1, 1, 11, '2024-12-06', '00:00:00', '00:00:00', 0, ''),
(39, 8, 1, 1, 11, '2024-11-29', '01:00:00', '02:00:00', 0, ''),
(40, 8, 1, 1, 11, '2024-11-29', '00:00:00', '00:00:00', 0, ''),
(41, 8, 70, 1, 13, '2024-12-02', '00:00:00', '00:00:00', 0, 'Feliz em ter um mapa novo!'),
(42, 8, 1, 1, 11, '2024-12-04', '04:00:00', '08:00:00', 0, ''),
(43, 8, 1, 1, 11, '2024-12-04', '17:00:00', '21:00:00', 0, ''),
(46, 10, 1, 1, 11, '2024-12-09', '08:00:00', '12:00:00', 0, ''),
(47, 10, 1, 1, 11, '2024-12-10', '08:00:00', '12:00:00', 0, ''),
(48, 9, 1, 4, 28, '2024-12-09', '19:00:00', '21:00:00', 0, ''),
(49, 10, 1, 1, 11, '2025-01-20', '19:00:00', '19:00:00', 0, ''),
(50, 10, 1, 1, 11, '2025-01-21', '19:00:00', '19:00:00', 0, ''),
(51, 15, 1, 1, 11, '2025-01-21', '13:30:00', '13:30:00', 0, ''),
(52, 10, 1, 4, 11, '2025-01-21', '19:00:00', '21:00:00', 0, ''),
(53, 9, 1, 4, 11, '2025-01-22', '19:00:00', '21:00:00', 0, ''),
(54, 10, 1, 1, 11, '2025-01-24', '13:30:00', '17:30:00', 0, ''),
(55, 10, 1, 2, 11, '2025-01-27', '13:30:00', '17:30:00', 0, ''),
(56, 10, 1, 4, 11, '2025-01-28', '19:00:00', '21:00:00', 0, ''),
(57, 10, 1, 4, 11, '2025-01-28', '13:30:00', '15:30:00', 0, ''),
(58, 11, 1, 1, 11, '2025-02-10', '13:30:00', '17:30:00', 0, '');

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
(11, 'j01', 'Laboratório', 'Prédio 1', '24', 24, 'ar-condicionado quebrado1'),
(12, 'cozinha', 'cozinha industrial', 'Prédio 2', '2fogao industrial, 20mesas, 30 cadeiras', 38, 'Teste'),
(13, 'h03', 'Comum', 'Prédio 2', '30computadores, 30 cadeiras30', 0, 'bla bla bla'),
(14, 'jardim', 'Comum', 'Prédio 1', 'mesas grandes 2 teste', 99, 'guarda sol danificcados  xsss'),
(15, 'sala q3', 'Studio de som', '1', 'teclado, microfone, abafador de audio', 15, 'test'),
(16, 'Sala de hardware', 'lab de infraestrutura', '2aaaaa', 'hack de roteadores, painel de controles, cabeamento de internet, peças de computadores', 25, 'painel de controles queimados'),
(17, 'Sala ensino meido E1', 'sala convencional ensino medio', '1', '13 notebooks, uma lousa digital', 35, ''),
(18, 'lab quimica', 'laboratorio', '2', 'produtos quimicos, esqueleto', 20, 'ssssssss'),
(19, 'Estetica', 'lab de Estetica', '2', 'pinças, maquiagem, maca', 18, ''),
(20, 'informatica', 'Laboratório', 'Prédio 1', '35 computadores', 30, 'Somente 30 computadores funcionando'),
(21, 'nome', 'Laboratório', 'Prédio 2', 'Nenhum', 30, 'Nenhuma'),
(22, 'j02', 'Laboratório', 'Prédio 2', '20 computadores', 30, 'Nenhuma aparente'),
(23, 'j02', 'Laboratório', 'Prédio 2', '20 computadores', 30, 'Nenhuma aparente'),
(24, 'j02', 'Laboratório', 'Prédio 1', '20 computadores', 30, 'Nenhuma aparente'),
(25, 'j02', 'Laboratório', 'Prédio 2', '20 computadores', 30, 'Nenhuma'),
(26, 'jardim externo', 'Jardinagem', 'Prédio 1', '5 sacos de adubo, 10 pás', 50, ''),
(27, 'j4', 'Laboratório', 'Prédio 1', '20 computadores, monitores, mouses e teclados', 20, 'Nenhuma'),
(28, 'J03', 'Laboratório', 'Prédio 2', 'teste', 24, 'Nenhuma'),
(29, 'J05', 'Laboratório', 'Prédio 2', '30 mesas e cadeiras', 30, 'Nenhuma'),
(30, 'J06', 'Comum', 'Prédio 2', '15 Computadores testttt', 15, 'Uma cadeira faltando'),
(31, 'testttt', 'Biblioteca', 'Prédio 2', 'test', 55, '666'),
(32, 'teste', 'Laboratorio', 'Prédio 1', 'test', 30, '333'),
(33, 'j050', 'Comum', 'Prédio 1', '10 Equipamentos', 30, 'nenhuma'),
(34, 'j050', 'Comum', 'Prédio 1', '10 Equipamentos', 30, 'nenhuma');

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
  ADD KEY `area_curso` (`idArea`),
  ADD UNIQUE KEY `oferta` (`oferta`);

--
-- Índices de tabela `equipamento`
--
ALTER TABLE `equipamento`
  ADD PRIMARY KEY (`idEquipamento`),
  ADD KEY `area_equipamento` (`idArea`);

--
-- Índices de tabela `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`idLogin`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `pessoa_login` (`idPessoa`);

--
-- Índices de tabela `ocupado`
--
ALTER TABLE `ocupado`
  ADD KEY `reserva_teste` (`idReserva`),
  ADD KEY `equipamento_teste` (`idEquipamento`);

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
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT de tabela `curso`
--
ALTER TABLE `curso`
  MODIFY `idCurso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de tabela `equipamento`
--
ALTER TABLE `equipamento`
  MODIFY `idEquipamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `idLogin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de tabela `pessoa`
--
ALTER TABLE `pessoa`
  MODIFY `idPessoa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT de tabela `reserva`
--
ALTER TABLE `reserva`
  MODIFY `idReserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT de tabela `sala`
--
ALTER TABLE `sala`
  MODIFY `idSala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `curso`
--
ALTER TABLE `curso`
  ADD CONSTRAINT `area_curso` FOREIGN KEY (`idArea`) REFERENCES `area` (`idArea`) ON DELETE CASCADE;

--
-- Restrições para tabelas `equipamento`
--
ALTER TABLE `equipamento`
  ADD CONSTRAINT `area_equipamento` FOREIGN KEY (`idArea`) REFERENCES `area` (`idArea`) ON DELETE CASCADE;

--
-- Restrições para tabelas `login`
--
ALTER TABLE `login`
  ADD CONSTRAINT `pessoa_login` FOREIGN KEY (`idPessoa`) REFERENCES `pessoa` (`idPessoa`) ON DELETE CASCADE;

--
-- Restrições para tabelas `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `curso_reserva` FOREIGN KEY (`idCurso`) REFERENCES `curso` (`idCurso`) ON DELETE CASCADE,
  ADD CONSTRAINT `login_reserva` FOREIGN KEY (`idLogin`) REFERENCES `login` (`idLogin`) ON DELETE CASCADE,
  ADD CONSTRAINT `pessoa_reserva` FOREIGN KEY (`idPessoa`) REFERENCES `pessoa` (`idPessoa`) ON DELETE CASCADE,
  ADD CONSTRAINT `sala_reserva` FOREIGN KEY (`idSala`) REFERENCES `sala` (`idSala`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
