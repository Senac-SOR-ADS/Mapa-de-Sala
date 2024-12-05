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
  `idArea` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL UNIQUE COMMENT 'Nome da área'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `area`
--

INSERT INTO `area`(`idArea`, `nome`) VALUES
(1, 'Tecnologia da Informação'),
(2, 'Beleza e Estética'),
(3, 'Bem-Estar'),
(4, 'Comunicação e Marketing'),
(5, 'Desenvolvimento Social'),
(6, 'Design'),
(7, 'Educação'),
(8, 'Gastronomia'),
(9, 'Gestão e Negócios'),
(10, 'Idiomas'),
(11, 'Moda'),
(12, 'Saúde'),
(13, 'Ensino Médio'),
(14, 'Artes'),
(15, 'Radiologia'),
(19, 'Desenvolvimento de Sistemas'),
(20, 'Pirotecnia'),
(21, 'Pirotecnia Profissional'),
(22, 'Pirotecnia Profissional2'),
(23, 'Pirotecnia Profissional3'),
(24, 'Medicina'),
(27, 'Jogos'),
(33, 'Musicas'),
(34, 'Relojoaria');

-- --------------------------------------------------------

--
-- Estrutura para tabela `curso`
--

CREATE TABLE `curso` (
  `idCurso` int(11) NOT NULL,
  `idArea` int(11) NOT NULL COMMENT 'ID da área associada',
  `nome` varchar(100) NOT NULL COMMENT 'Nome do curso',
  `oferta` varchar(50) NOT NULL COMMENT 'Oferta do curso',
  `periodo` varchar(50) NOT NULL COMMENT 'Período do curso',
  `cargaHoraria` int(11) NOT NULL COMMENT 'Carga horária do curso',
  `horasDia` time NOT NULL COMMENT 'Horas diárias de aula',
  `qtdAlunos` int(11) NOT NULL COMMENT 'Quantidade de alunos'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `curso`
--

INSERT INTO `curso` (`idCurso`, `idArea`, `nome`, `oferta`, `periodo`, `cargaHoraria`, `horasDia`, `qtdAlunos`) VALUES
(1, 1, 'Power BI', '245685', 'Manhã', 121013, '04:00:00', 17),
(2, 3, 'Reiki', '487563', 'Tarde', 231830, '02:00:00', 9),
(3, 4, 'Documentário', '478651', 'Manhã', 0, '04:00:00', 7),
(4, 8, 'Doces Finos', '532148', 'Noite', 24, '02:00:00', 25),
(5, 9, 'Gestão Fiscal', '856432', 'Tarde', 0, '04:00:00', 30),
(6, 2, 'Alongamento de Cílios', '214589', 'Manhã', 0, '02:00:00', 12),
(7, 12, 'Atendente de Farmacia', '547893', 'Tarde', 58, '04:00:00', 24),
(8, 10, 'Libras', '2478947', 'Tarde', 120, '04:00:00', 17),
(9, 14, 'Ceramica', '457863', 'Noite', 24, '02:00:00', 13),
(10, 33, 'piano', '40028', 'Manhã', 123, '04:00:00', 21),
(11, 19, 'Desenvolvimento de Software', '707070', 'Noite', 1200, '04:00:00', 24),
(12, 1, '', '', 'Manhã', 0, '00:00:00', 0);

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
(11, 'j01', 'labolatorio de informatica', '2', '30', 30, 'ar-condicionado quebrado'),
(12, 'cozinha', 'cozinha industrial', '1', '2fogao industrial, 20mesas, 30 cadeiras', 40, ''),
(13, 'h03', 'Sala de idiomas', '2', '30computadores, 30 cadeiras30', 30, '10 computadores em manutenção'),
(14, 'jardim', 'area externa', '2', 'mesas grandes 2, 4 bancos grandes', 0, 'guarda sol danificcados'),
(15, 'sala q3', 'Studio de som', '1', 'teclado, microfone, abafador de audio', 15, ''),
(16, 'Sala de hardware', 'lab de infraestrutura', '2', 'hack de roteadores, painel de controles, cabeamento de internet, peças de computadores', 25, 'painel de controles queimados'),
(17, 'Sala ensino meido E1', 'sala convencional ensino medio', '1', '13 notebooks, uma lousa digital', 35, ''),
(18, 'lab quimica', 'laboratorio', '2', 'produtos quimicos, esqueleto', 20, 'Produtos perigosos, uso de EPI obrigatorio'),
(19, 'Estetica', 'lab de Estetica', '2', 'pinças, maquiagem, maca', 18, ''),
(20, 'informatica', 'sala de informatica', '1', '25 computadores', 25, 'Somente 15 computadores funcionando'),
(21, 'nome', 'tipo', 'predio', 'equipamentos', 0, 'observacao'),
(22, 'j02', 'Laboratório', 'Prédio 2', '20 computadores', 30, 'Nenhuma aparente'),
(23, 'j02', 'Laboratório', 'Prédio 2', '20 computadores', 30, 'Nenhuma aparente'),
(24, 'j02', 'Laboratório', 'Prédio 1', '20 computadores', 30, 'Nenhuma aparente'),
(25, 'j02', 'Laboratório', 'Prédio 2', '20 computadores', 30, 'Nenhuma'),
(26, 'jardim externo', 'Jardinagem', 'Prédio 1', '5 sacos de adubo, 10 pás', 50, ''),
(27, 'j4', 'Laboratório', 'Prédio 1', '20 computadores, monitores, mouses e teclados', 20, 'Nenhuma'),
(28, 'J03', 'Laboratório', 'Prédio 2', 'teste', 24, 'Nenhuma'),
(29, 'J05', 'Laboratório', 'Prédio 2', '30 mesas e cadeiras', 30, 'Nenhuma'),
(30, 'J06', 'Laboratório', 'Prédio 1', '15 Computadores', 15, 'Uma cadeira faltando');

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
  `email` varchar(100) NOT NULL UNIQUE COMMENT 'Email da pessoa',
  `cargo` ENUM('Comum', 'Apoio', 'Patrimonio', 'Administrador') NOT NULL COMMENT 'Cargo ou função da pessoa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `pessoa`
--

INSERT INTO `pessoa` (`idPessoa`, `nome`, `CPF_CNPJ`, `nascimento`, `telefone`, `email`, `cargo`) VALUES
(1, 'Enzo Silva Carvalho', '663.300.190-88', '2000-08-15', '(61) 3615-2089', 'emailgenerico@gmail.com', 'Apoio'),
(2, 'Laís Malu Rebeca da Paz', '192.458.327-59', '1981-08-20', '(46) 2578-6303', 'potoasdfeafafemdfmakfmskmfkmfkamamd@gmail.com', 'Patrimônio'),
(3, 'Enzo Diogo Martin Silva', '931.825.487-35', '1998-07-04', '(79) 3963-7319', 'fdsfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsd@gmail.com', 'Limpeza'),
(4, 'Renato Bernardo Yuri das Neves', '727.882.631-47', '1987-03-06', '(71) 3860-2221', 'emailqualquer@gmail.com', 'Docente'),
(5, 'Elisa Mariane Adriana Assis', '44.196.017/0001-31', '1960-02-01', '(63) 2801-0368', 'elisa-assis95@amoreencantos.com', 'Chefe'),
(6, 'Marcelo Vinicius Tiago Freitas', '054.675.039-79', '1992-03-17', '(68) 3937-9429', 'marcelo-freitas77@iclaud.com', 'Diretor'),
(7, 'Marcela Alessandra Gomes', '284.319.150-56', '2001-02-09', '(42) 3667-9065', 'marcela_alessandra_gomes@callan.com.br', 'Manutenção'),
(8, 'Maria Isabelly Jéssica Nascimento', '71.386.002/0001-09', '1992-01-19', '(44) 2533-0657', 'maria_isabelly_nascimento@oticascarol.com.br', 'Apoio'),
(9, 'Otavio', '533.390.123-69', '1973-04-01', '(27) 2579-5552', 'otavio@g.com', 'Patrimônio'),
(10, 'Gabriel', '28.653.414/0001-39', '1972-02-16', '(95) 3631-8354', 'gabriel@g.com', 'Patrimônio'),
(11, 'Ricardo', '123.123.123-90', '2006-10-19', '(15) 99120-6869', 'richard@g.com', 'Gerente Master'),
(12, 'Bruno Rodrigues', '123.456.789-00', '2006-10-19', '(15) 99120-6869', 'brunor@gmail.com', 'Gerente Master'),
(13, 'Nickolas', '123.456.789-00', '2006-10-19', '(15) 99120-6869', 'nickolas@gmail.com', 'Gerente Master'),
(14, 'Bruno Mendes', '123.456.789-00', '2006-10-19', '(15) 99120-6869', 'brunom@gmail.com', 'Gerente Master'),
(15, 'Samuel', '123.456.789-00', '2006-10-19', '(15) 99120-6869', 'samuel@gmail.com', 'Gerente Master'),
(16, 'Jeff', '123.456.789-00', '2006-10-19', '(15) 99120-6869', 'jeff@gmail.com', 'Gerente Master'),
(27, 'samuel', '12312312312', '0000-00-00', '19/10/2006', 'gerente pro master fodão', '15991206868'),
(28, 'otavio', '12312312312', '0000-00-00', '15991150990', 'o@g.c', 'gerente pro master fodão 2'),
(29, 'gabriel', '12312312312', '0000-00-00', '15991102992', 'g@g.c', 'gerente pro master fodão III'),
(30, 'asdf', '12312312312', '0000-00-00', '15 9999 0000', 'piriripororo@g.com', 'Gerente pro master'),
(31, 'Samuel', '12345678900', '2006-10-19', '15 9999 0000', 's@g.c', 'gerente pro master fodão V'),
(32, 'asdf', 'asdf', '2000-01-01', '123412341234', 'asdf@g.c', 'Comum'),
(33, 'asdfasdf', 'asdfasdfasdf', '2019-01-01', '18 99999 0000', 'asfadfasdfadsf@g.c', 'Apoio'),
(34, 'asfadfas', 'afadfaf', '2019-01-01', '141441441431433', 'afasaafdasf@g.com', 'Apoio'),
(35, 'dfasfadf', 'asfasdfasdf', '2000-01-09', '114415465637367', 'asfasdfasdf', 'Comum'),
(36, 'asdfadsfa', 'asdfasfasd', '2000-01-01', '4141414', 'asfadfa', 'Patrimonio'),
(37, 'aaaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaa', '2000-01-01', '1111111111111', 'aaaaaaaaaaaaa@g.c', 'Patrimonio'),
(38, 'bbbbbbbbbbbbb', 'bbbbbbbbbb', '2000-01-01', 'bbbbbbbbbb', 'bbbbbbbbb', 'Administrador'),
(39, 'cccccccccc', 'cccccccccc', '2000-01-01', 'cccccccc', 'cccccccccc', 'Apoio'),
(40, 'dddddddd', 'dddddd', '2000-01-01', 'dddddddddddd', 'ddddd', 'Apoio'),
(41, 'hell yeah', '123 456 789 00', '2001-09-11', '15 99999 0000', 'henricky@g.c', 'Administrador');

-- --------------------------------------------------------
--
-- Estrutura para tabela `login`
--

CREATE TABLE `login` (
  `idLogin` int(11) NOT NULL,
  `idPessoa` int(11) NOT NULL COMMENT 'ID da pessoa associada',
  `email` varchar(100) NOT NULL UNIQUE COMMENT 'Email do login',
  `senha` varchar(100) NOT NULL COMMENT 'Senha do login',
  `nivelAcesso` ENUM('admin', 'user') NOT NULL DEFAULT 'user' COMMENT 'Nível de acesso do usuário'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Despejando dados para a tabela `login`
--

INSERT INTO `login` (`idLogin`, `idPessoa`, `email`, `senha`, `nivelAcesso`) VALUES
(1, 1, 'email@gmail.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(5, 2, 'potoasdfeafafemdfmakfmskmfkmfkamamd@gmail.com', 'lais123', 'admin'),
(6, 8, 'maria_isabelly_nascimento@oticascarol.com.br', 'marmaria123', 'user'),
(7, 6, 'marcelo-freitas77@iclaud.com', 'marcelo123', 'user'),
(8, 3, 'enzo@gmail.com', 'enzo', 'admin'),
(9, 9, 'otavio@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(10, 10, 'gabriel@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(11, 11, 'richard@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(12, 12, 'brunor@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(13, 13, 'nickolas@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(14, 14, 'brunom@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(15, 15, 'samuel@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin'),
(16, 16, 'jeff@g.com', '$2b$12$I0EQ29vq2sUG1IgX6HbIW.80QciN/TM.EWtZX9jX8O2qg0O2C1sre', 'admin');

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
(27, 1, 3, 5, 15, '2024-09-20', '09:00:00', '10:00:00', 1, NULL);

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

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`idArea`);

--
-- Índices de tabela `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`idCurso`),
  ADD KEY `area_curso` (`idArea`);

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
  ADD PRIMARY KEY (`idPessoa`);

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
  MODIFY `idArea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de tabela `curso`
--
ALTER TABLE `curso`
  MODIFY `idCurso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `equipamento`
--
ALTER TABLE `equipamento`
  MODIFY `idEquipamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `idLogin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de tabela `pessoa`
--
ALTER TABLE `pessoa`
  MODIFY `idPessoa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de tabela `reserva`
--
ALTER TABLE `reserva`
  MODIFY `idReserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de tabela `sala`
--
ALTER TABLE `sala`
  MODIFY `idSala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

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
