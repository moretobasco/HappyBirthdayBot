

CREATE TABLE users (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    full_name VARCHAR(100) GENERATED ALWAYS AS (first_name || last_name) STORED
)

INSERT INTO corporatemails (email, registered) VALUES
('Alexey.Lisanskiy@advncd.com', FALSE),



INSERT INTO users (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Michael', 'Johnson');



INSERT INTO users (user_id, user_name, birthday, b_day, b_month) VALUES
(1, 'Alice', '1990-01-01', '01', '01'),
(2, 'Bob', '1985-01-02', '02', '01'),
(3, 'Charlie', '1995-01-03', '03', '01'),
(4, 'David', '1988-01-04', '04', '01'),
(5, 'Eve', '1992-01-05', '05', '01'),
(6, 'Frank', '1984-01-06', '06', '01'),
(7, 'Grace', '1997-01-07', '07', '01'),
(8, 'Helen', '1983-01-08', '08', '01'),
(9, 'Ivan', '1991-01-09', '09', '01'),
(10, 'Jane', '1987-01-10', '10', '01'),
(11, 'Kevin', '1994-01-11', '11', '01'),
(12, 'Lily', '1989-01-12', '12', '01'),
(13, 'Mike', '1998-01-13', '13', '01'),
(14, 'Nancy', '1986-01-14', '14', '01'),
(15, 'Olivia', '1993-01-15', '15', '01'),
(16, 'Peter', '1981-01-16', '16', '01'),
(17, 'Quinn', '1996-01-17', '17', '01'),
(18, 'Rachel', '1982-01-18', '18', '01'),
(19, 'Sam', '1980-01-19', '19', '01'),
(20, 'Tom', '1999-01-20', '20', '01'),
(21, 'Ursula', '1985-01-21', '21', '01'),
(22, 'Victor', '1990-01-22', '22', '01'),
(23, 'Wendy', '1988-01-23', '23', '01'),
(24, 'Xavier', '1983-01-24', '24', '01'),
(25, 'Yvonne', '1992-01-25', '25', '01'),
(26, 'Zelda', '1987-01-26', '26', '01'),
(27, 'Adam', '1981-01-27', '27', '01'),
(28, 'Beth', '1995-01-28', '28', '01'),
(29, 'Chris', '1989-01-29', '29', '01'),
(30, 'Dana', '1984-01-30', '30', '01'),
(31, 'Eric', '1996-01-31', '31', '01'),
(32, 'Fiona', '1980-02-01', '01', '02'),
(33, 'George', '1994-02-02', '02', '02'),
(34, 'Hannah', '1986-02-03', '03', '02'),
(35, 'Isaac', '1983-02-04', '04', '02'),
(36, 'Julia', '1990-02-05', '05', '02'),
(37, 'Keith', '1988-02-06', '06', '02'),
(38, 'Lisa', '1999-02-07', '07', '02'),
(39, 'Matthew', '1985-02-08', '08', '02'),
(40, 'Nina', '1993-02-09', '09', '02'),
(41, 'Oscar', '1981-02-10', '10', '02'),
(42, 'Paula', '1997-02-11', '11', '02'),
(43, 'Quentin', '1984-02-12', '12', '02'),
(44, 'Rita', '1992-02-13', '13', '02'),
(45, 'Samantha', '1987-02-14', '14', '02'),
(46, 'Tim', '1980-02-15', '15', '02'),
(47, 'Uma', '1991-02-16', '16', '02'),
(48, 'Vincent', '1989-02-17', '17', '02'),
(49, 'Walter', '1995-02-18', '18', '02'),
(50, 'Xena', '1982-02-19', '19', '02'),
(51, 'Yolanda', '1988-02-20', '20', '02'),
(52, 'Zack', '1993-02-21', '21', '02'),
(53, 'Abigail', '1986-02-22', '22', '02'),
(54, 'Benjamin', '1990-02-23', '23', '02'),
(55, 'Catherine', '1981-02-24', '24', '02'),
(56, 'Daniel', '1996-02-25', '25', '02'),
(57, 'Emily', '1984-02-26', '26', '02'),
(58, 'Felix', '1991-02-27', '27', '02'),
(59, 'Gina', '1987-02-28', '28', '02'),
(60, 'Henry', '1982-03-01', '01', '03'),
(61, 'Irene', '1994-03-02', '02', '03'),
(62, 'Jake', '1989-03-03', '03', '03'),
(63, 'Katie', '1992-03-04', '04', '03'),
(64, 'Liam', '1980-03-05', '05', '03'),
(65, 'Megan', '1985-03-06', '06', '03'),
(66, 'Nathan', '1998-03-07', '07', '03'),
(67, 'Oliver', '1983-03-08', '08', '03'),
(68, 'Pamela', '1995-03-09', '09', '03'),
(69, 'Quincy', '1986-03-10', '10', '03'),
(70, 'Rachel', '1991-03-11', '11', '03'),
(71, 'Steve', '1988-03-12', '12', '03'),
(72, 'Tina', '1980-03-13', '13', '03'),
(73, 'Uriel', '1993-03-14', '14', '03'),
(74, 'Victoria', '1981-03-15', '15', '03'),
(75, 'William', '1990-03-16', '16', '03'),
(76, 'Xander', '1987-03-17', '17', '03'),
(77, 'Yvette', '1994-03-18', '18', '03'),
(78, 'Zara', '1983-03-19', '19', '03'),
(79, 'Aaron', '1999-03-20', '20', '03'),
(80, 'Bella', '1985-03-21', '21', '03'),
(81, 'Charlie', '1991-03-22', '22', '03'),
(82, 'David', '1988-03-23', '23', '03'),
(83, 'Ella', '1996-03-24', '24', '03'),
(84, 'Frank', '1984-03-25', '25', '03'),
(85, 'Gwen', '1992-03-26', '26', '03'),
(86, 'Harry', '1981-03-27', '27', '03'),
(87, 'Ivy', '1995-03-28', '28', '03'),
(88, 'Jack', '1986-03-29', '29', '03'),
(89, 'Kara', '1990-03-30', '30', '03'),
(90, 'Lena', '1983-03-31', '31', '03'),
(91, 'Max', '1980-04-01', '01', '04'),
(92, 'Nora', '1997-04-02', '02', '04'),
(93, 'Owen', '1982-04-03', '03', '04'),
(94, 'Penny', '1989-04-04', '04', '04'),
(95, 'Quinn', '1994-04-05', '05', '04'),
(96, 'Rachel', '1983-04-06', '06', '04'),
(97, 'Sam', '1995-04-07', '07', '04'),
(98, 'Tina', '1980-04-08', '08', '04'),
(99, 'Uma', '1996-04-09', '09', '04'),
(101, 'Aaron', '1990-04-10', '10', '04'),
(102, 'Bella', '1985-04-11', '11', '04'),
(103, 'Cameron', '1992-04-12', '12', '04'),
(104, 'Diana', '1987-04-13', '13', '04'),
(105, 'Ethan', '1991-04-14', '14', '04'),
(106, 'Fiona', '1989-04-15', '15', '04'),
(107, 'George', '1995-04-16', '16', '04'),
(108, 'Holly', '1988-04-17', '17', '04'),
(109, 'Isaac', '1994-04-18', '18', '04'),
(110, 'Jasmine', '1990-04-19', '19', '04'),
(111, 'Kevin', '1991-04-20', '20', '04'),
(112, 'Lena', '1986-04-21', '21', '04'),
(113, 'Michael', '1987-04-22', '22', '04'),
(114, 'Nina', '1995-04-23', '23', '04'),
(115, 'Oscar', '1988-04-24', '24', '04'),
(116, 'Paula', '1993-04-25', '25', '04'),
(117, 'Quincy', '1994-04-26', '26', '04'),
(118, 'Riley', '1989-04-27', '27', '04'),
(119, 'Sarah', '1985-04-28', '28', '04'),
(120, 'Thomas', '1990-04-29', '29', '04'),
(121, 'Uma', '1993-04-30', '30', '04'),
(122, 'Victor', '1988-05-01', '01', '05'),
(123, 'Wendy', '1992-05-02', '02', '05'),
(124, 'Xander', '1986-05-03', '03', '05'),
(125, 'Yvonne', '1991-05-04', '04', '05'),
(126, 'Zara', '1987-05-05', '05', '05'),
(127, 'Alice', '1990-05-06', '06', '05'),
(128, 'Bob', '1989-05-07', '07', '05'),
(129, 'Catherine', '1994-05-08', '08', '05'),
(130, 'Daniel', '1991-05-09', '09', '05'),
(131, 'Eve', '1992-05-10', '10', '05'),
(132, 'Frank', '1985-05-11', '11', '05'),
(133, 'Grace', '1993-05-12', '12', '05'),
(134, 'Henry', '1988-05-13', '13', '05'),
(135, 'Ivy', '1990-05-14', '14', '05'),
(136, 'Jack', '1986-05-15', '15', '05'),
(137, 'Kara', '1995-05-16', '16', '05'),
(138, 'Liam', '1993-05-17', '17', '05'),
(139, 'Mona', '1990-05-18', '18', '05'),
(140, 'Nathan', '1987-05-19', '19', '05'),
(141, 'Olivia', '1992-05-20', '20', '05'),
(142, 'Paul', '1986-05-21', '21', '05'),
(143, 'Quinn', '1993-05-22', '22', '05'),
(144, 'Rachel', '1990-05-23', '23', '05'),
(145, 'Sam', '1989-05-24', '24', '05'),
(146, 'Tina', '1991-05-25', '25', '05'),
(147, 'Ulysses', '1988-05-26', '26', '05'),
(148, 'Vera', '1987-05-27', '27', '05'),
(149, 'Will', '1990-05-28', '28', '05'),
(150, 'Xena', '1993-05-29', '29', '05'),
(151, 'Yara', '1989-05-30', '30', '05'),
(152, 'Zane', '1991-05-31', '31', '05'),
(153, 'Abby', '1992-06-01', '01', '06'),
(154, 'Ben', '1986-06-02', '02', '06'),
(155, 'Chloe', '1995-06-03', '03', '06'),
(156, 'David', '1990-06-04', '04', '06'),
(157, 'Ella', '1988-06-05', '05', '06'),
(158, 'Fred', '1993-06-06', '06', '06'),
(159, 'Gina', '1989-06-07', '07', '06'),
(160, 'Hank', '1994-06-08', '08', '06'),
(161, 'Iris', '1987-06-09', '09', '06'),
(162, 'Jake', '1991-06-10', '10', '06'),
(163, 'Kyla', '1995-06-11', '11', '06'),
(164, 'Leo', '1990-06-12', '12', '06'),
(165, 'Mia', '1992-06-13', '13', '06'),
(166, 'Nick', '1985-06-14', '14', '06'),
(167, 'Olga', '1989-06-15', '15', '06'),
(168, 'Pete', '1993-06-16', '16', '06'),
(169, 'Quincy', '1988-06-17', '17', '06'),
(170, 'Rose', '1991-06-18', '18', '06'),
(171, 'Steve', '1995-06-19', '19', '06'),
(172, 'Tara', '1987-06-20', '20', '06'),
(173, 'Uma', '1994-06-21', '21', '06'),
(174, 'Vince', '1988-06-22', '22', '06'),
(175, 'Wade', '1990-06-23', '23', '06'),
(176, 'Xander', '1991-06-24', '24', '06'),
(177, 'Yolanda', '1995-06-25', '25', '06'),
(178, 'Zach', '1986-06-26', '26', '06'),
(179, 'Amy', '1993-06-27', '27', '06'),
(180, 'Bill', '1990-06-28', '28', '06'),
(181, 'Carmen', '1989-06-29', '29', '06'),
(182, 'Dylan', '1994-06-30', '30', '06');
(183, 'Aaron', '1986-07-01', '01', '07'),
(184, 'Bella', '1993-07-02', '02', '07'),
(185, 'Cameron', '1991-07-03', '03', '07'),
(186, 'Diana', '1988-07-04', '04', '07'),
(187, 'Ethan', '1990-07-05', '05', '07'),
(188, 'Fiona', '1992-07-06', '06', '07'),
(189, 'George', '1989-07-07', '07', '07'),
(190, 'Holly', '1994-07-08', '08', '07'),
(191, 'Isaac', '1987-07-09', '09', '07'),
(192, 'Jasmine', '1990-07-10', '10', '07'),
(193, 'Kevin', '1991-07-11', '11', '07'),
(194, 'Lena', '1989-07-12', '12', '07'),
(195, 'Michael', '1992-07-13', '13', '07'),
(196, 'Nina', '1988-07-14', '14', '07'),
(197, 'Oscar', '1994-07-15', '15', '07'),
(198, 'Paula', '1990-07-16', '16', '07'),
(199, 'Quincy', '1991-07-17', '17', '07'),
(200, 'Riley', '1987-07-18', '18', '07'),
(201, 'Sarah', '1992-07-19', '19', '07'),
(202, 'Thomas', '1989-07-20', '20', '07'),
(203, 'Uma', '1990-07-21', '21', '07'),
(204, 'Victor', '1994-07-22', '22', '07'),
(205, 'Wendy', '1986-07-23', '23', '07'),
(206, 'Xander', '1993-07-24', '24', '07'),
(207, 'Yvonne', '1987-07-25', '25', '07'),
(208, 'Zara', '1991-07-26', '26', '07'),
(209, 'Alice', '1990-07-27', '27', '07'),
(210, 'Bob', '1994-07-28', '28', '07'),
(211, 'Catherine', '1989-07-29', '29', '07'),
(212, 'Daniel', '1993-07-30', '30', '07'),
(213, 'Eve', '1992-07-31', '31', '07'),
(214, 'Frank', '1985-08-01', '01', '08'),
(215, 'Grace', '1990-08-02', '02', '08'),
(216, 'Henry', '1994-08-03', '03', '08'),
(217, 'Ivy', '1986-08-04', '04', '08'),
(218, 'Jack', '1991-08-05', '05', '08'),
(219, 'Kara', '1989-08-06', '06', '08'),
(220, 'Liam', '1993-08-07', '07', '08'),
(221, 'Mona', '1990-08-08', '08', '08'),
(222, 'Nathan', '1985-08-09', '09', '08'),
(223, 'Olivia', '1991-08-10', '10', '08'),
(224, 'Paul', '1994-08-11', '11', '08'),
(225, 'Quinn', '1987-08-12', '12', '08'),
(226, 'Rachel', '1990-08-13', '13', '08'),
(227, 'Sam', '1993-08-14', '14', '08'),
(228, 'Tina', '1992-08-15', '15', '08'),
(229, 'Ulysses', '1988-08-16', '16', '08'),
(230, 'Vera', '1990-08-17', '17', '08'),
(231, 'Will', '1989-08-18', '18', '08'),
(232, 'Xena', '1991-08-19', '19', '08'),
(233, 'Yara', '1986-08-20', '20', '08'),
(234, 'Zane', '1994-08-21', '21', '08'),
(235, 'Abby', '1987-08-22', '22', '08'),
(236, 'Ben', '1990-08-23', '23', '08'),
(237, 'Chloe', '1992-08-24', '24', '08'),
(238, 'David', '1989-08-25', '25', '08'),
(239, 'Ella', '1991-08-26', '26', '08'),
(240, 'Fred', '1994-08-27', '27', '08'),
(241, 'Gina', '1988-08-28', '28', '08'),
(242, 'Hank', '1990-08-29', '29', '08'),
(243, 'Iris', '1993-08-30', '30', '08'),
(244, 'Jake', '1986-08-31', '31', '08'),
(245, 'Kyla', '1991-09-01', '01', '09'),
(246, 'Leo', '1990-09-02', '02', '09'),
(247, 'Mia', '1994-09-03', '03', '09'),
(248, 'Nick', '1989-09-04', '04', '09'),
(249, 'Olga', '1993-09-05', '05', '09'),
(250, 'Pete', '1991-09-06', '06', '09'),
(251, 'Quincy', '1990-09-07', '07', '09'),
(252, 'Rose', '1987-09-08', '08', '09'),
(253, 'Steve', '1994-09-09', '09', '09'),
(254, 'Tara', '1990-09-10', '10', '09'),
(255, 'Uma', '1988-09-11', '11', '09'),
(256, 'Vince', '1993-09-12', '12', '09'),
(257, 'Wade', '1991-09-13', '13', '09'),
(258, 'Xander', '1986-09-14', '14', '09'),
(259, 'Yolanda', '1990-09-15', '15', '09'),
(260, 'Zach', '1992-09-16', '16', '09'),
(261, 'Amy', '1987-09-17', '17', '09'),
(262, 'Bill', '1991-09-18', '18', '09'),
(263, 'Carmen', '1990-09-19', '19', '09'),
(264, 'Dylan', '1994-09-20', '20', '09'),
(265, 'Aaron', '1992-09-21', '21', '09'),
(266, 'Bella', '1989-09-22', '22', '09'),
(267, 'Cameron', '1991-09-23', '23', '09'),
(268, 'Diana', '1993-09-24', '24', '09'),
(269, 'Ethan', '1987-09-25', '25', '09'),
(270, 'Fiona', '1990-09-26', '26', '09'),
(271, 'George', '1992-09-27', '27', '09'),
(272, 'Holly', '1994-09-28', '28', '09'),
(273, 'Isaac', '1988-09-29', '29', '09'),
(274, 'Jasmine', '1990-09-30', '30', '09');
(275, 'Kevin', '1993-10-01', '01', '10'),
(276, 'Lena', '1987-10-02', '02', '10'),
(277, 'Michael', '1991-10-03', '03', '10'),
(278, 'Nina', '1994-10-04', '04', '10'),
(279, 'Oscar', '1990-10-05', '05', '10'),
(280, 'Paula', '1988-10-06', '06', '10'),
(281, 'Quincy', '1993-10-07', '07', '10'),
(282, 'Riley', '1992-10-08', '08', '10'),
(283, 'Sarah', '1989-10-09', '09', '10'),
(284, 'Thomas', '1990-10-10', '10', '10'),
(285, 'Uma', '1987-10-11', '11', '10'),
(286, 'Victor', '1994-10-12', '12', '10'),
(287, 'Wendy', '1991-10-13', '13', '10'),
(288, 'Xander', '1990-10-14', '14', '10'),
(289, 'Yvonne', '1989-10-15', '15', '10'),
(290, 'Zara', '1992-10-16', '16', '10'),
(291, 'Alice', '1994-10-17', '17', '10'),
(292, 'Bob', '1990-10-18', '18', '10'),
(293, 'Catherine', '1987-10-19', '19', '10'),
(294, 'Daniel', '1992-10-20', '20', '10'),
(295, 'Eve', '1990-10-21', '21', '10'),
(296, 'Frank', '1988-10-22', '22', '10'),
(297, 'Grace', '1994-10-23', '23', '10'),
(298, 'Henry', '1991-10-24', '24', '10'),
(299, 'Ivy', '1993-10-25', '25', '10'),
(300, 'Jack', '1989-10-26', '26', '10'),
(301, 'Kara', '1990-10-27', '27', '10'),
(302, 'Liam', '1994-10-28', '28', '10'),
(303, 'Mona', '1987-10-29', '29', '10'),
(304, 'Nathan', '1991-10-30', '30', '10'),
(305, 'Olivia', '1992-10-31', '31', '10'),
(306, 'Paul', '1990-11-01', '01', '11'),
(307, 'Quinn', '1989-11-02', '02', '11'),
(308, 'Rachel', '1993-11-03', '03', '11'),
(309, 'Sam', '1991-11-04', '04', '11'),
(310, 'Tina', '1990-11-05', '05', '11'),
(311, 'Ulysses', '1994-11-06', '06', '11'),
(312, 'Vera', '1987-11-07', '07', '11'),
(313, 'Will', '1992-11-08', '08', '11'),
(314, 'Xena', '1991-11-09', '09', '11'),
(315, 'Yara', '1990-11-10', '10', '11'),
(316, 'Zane', '1993-11-11', '11', '11'),
(317, 'Abby', '1994-11-12', '12', '11'),
(318, 'Ben', '1990-11-13', '13', '11'),
(319, 'Chloe', '1989-11-14', '14', '11'),
(320, 'David', '1991-11-15', '15', '11'),
(321, 'Ella', '1990-11-16', '16', '11'),
(322, 'Fred', '1988-11-17', '17', '11'),
(323, 'Gina', '1994-11-18', '18', '11'),
(324, 'Hank', '1991-11-19', '19', '11'),
(325, 'Iris', '1987-11-20', '20', '11'),
(326, 'Jake', '1990-11-21', '21', '11'),
(327, 'Kyla', '1992-11-22', '22', '11'),
(328, 'Leo', '1989-11-23', '23', '11'),
(329, 'Mia', '1991-11-24', '24', '11'),
(330, 'Nick', '1993-11-25', '25', '11'),
(331, 'Olga', '1990-11-26', '26', '11'),
(332, 'Pete', '1987-11-27', '27', '11'),
(333, 'Quincy', '1994-11-28', '28', '11'),
(334, 'Rose', '1991-11-29', '29', '11'),
(335, 'Steve', '1992-11-30', '30', '11'),
(336, 'Tara', '1989-12-01', '01', '12'),
(337, 'Uma', '1990-12-02', '02', '12'),
(338, 'Vince', '1994-12-03', '03', '12'),
(339, 'Wade', '1991-12-04', '04', '12'),
(340, 'Xander', '1992-12-05', '05', '12'),
(341, 'Yolanda', '1987-12-06', '06', '12'),
(342, 'Zach', '1990-12-07', '07', '12'),
(343, 'Amy', '1991-12-08', '08', '12'),
(344, 'Bill', '1994-12-09', '09', '12'),
(345, 'Carmen', '1990-12-10', '10', '12'),
(346, 'Dylan', '1988-12-11', '11', '12'),
(347, 'Aaron', '1991-12-12', '12', '12'),
(348, 'Bella', '1992-12-13', '13', '12'),
(349, 'Cameron', '1993-12-14', '14', '12'),
(350, 'Diana', '1987-12-15', '15', '12'),
(351, 'Ethan', '1990-12-16', '16', '12'),
(352, 'Fiona', '1991-12-17', '17', '12'),
(353, 'George', '1994-12-18', '18', '12'),
(354, 'Holly', '1989-12-19', '19', '12'),
(355, 'Isaac', '1992-12-20', '20', '12'),
(356, 'Jasmine', '1990-12-21', '21', '12'),
(357, 'Kevin', '1988-12-22', '22', '12'),
(358, 'Lena', '1991-12-23', '23', '12'),
(359, 'Michael', '1992-12-24', '24', '12'),
(360, 'Nina', '1989-12-25', '25', '12'),
(361, 'Oscar', '1994-12-26', '26', '12'),
(362, 'Paula', '1990-12-27', '27', '12'),
(363, 'Quincy', '1991-12-28', '28', '12'),
(364, 'Riley', '1992-12-29', '29', '12'),
(365, 'Sarah', '1987-12-30', '30', '12'),
(366, 'Thomas', '1990-12-31', '31', '12');















