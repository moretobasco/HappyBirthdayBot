-- Вставка данных
INSERT INTO users (user_id, user_name, birthday) VALUES
(1, 'Alice', '1990-05-15'),
(2, 'Bob', '1985-10-22'),
(3, 'Charlie', '1995-03-08'),
(4, 'David', '1988-12-17'),
(5, 'Eve', '1992-07-03'),
(6, 'Frank', '1984-09-28'),
(7, 'Grace', '1997-11-12'),
(8, 'Helen', '1983-06-30'),
(9, 'Ivan', '1991-04-19'),
(10, 'Jane', '1987-08-05'),
(11, 'Kevin', '1994-01-24'),
(12, 'Lily', '1989-02-11'),
(13, 'Mike', '1998-06-18'),
(14, 'Nancy', '1986-03-27'),
(15, 'Olivia', '1993-10-09'),
(16, 'Peter', '1981-07-14'),
(17, 'Quinn', '1996-04-02'),
(18, 'Rachel', '1982-12-21'),
(19, 'Sam', '1980-08-17'),
(20, 'Tom', '1999-02-03'),
(21, 'Ursula', '1985-05-20'),
(22, 'Victor', '1990-11-28'),
(23, 'Wendy', '1988-09-06'),
(24, 'Xavier', '1983-04-13'),
(25, 'Yvonne', '1992-01-31'),
(26, 'Zelda', '1987-08-08'),
(27, 'Adam', '1981-12-25'),
(28, 'Beth', '1995-07-02'),
(29, 'Chris', '1989-03-19'),
(30, 'Dana', '1984-10-26'),
(31, 'Eric', '1996-08-14'),
(32, 'Fiona', '1980-04-03'),
(33, 'George', '1994-09-21'),
(34, 'Hannah', '1986-01-18'),
(35, 'Isaac', '1983-11-05'),
(36, 'Julia', '1990-06-22'),
(37, 'Keith', '1988-03-11'),
(38, 'Lisa', '1999-05-28'),
(39, 'Matthew', '1985-02-15'),
(40, 'Nina', '1993-10-02'),
(41, 'Oscar', '1981-07-19'),
(42, 'Paula', '1997-12-16'),
(43, 'Quentin', '1984-09-23'),
(44, 'Rita', '1992-11-10'),
(45, 'Samantha', '1987-06-27'),
(46, 'Tim', '1980-08-04'),
(47, 'Uma', '1991-03-01'),
(48, 'Vincent', '1989-12-08'),
(49, 'Walter', '1995-02-25'),
(50, 'Xena', '1982-10-13'),
(51, 'Yolanda', '1988-05-30'),
(52, 'Zack', '1993-01-17'),
(53, 'Abigail', '1986-04-04'),
(54, 'Benjamin', '1990-11-21'),
(55, 'Catherine', '1981-09-08'),
(56, 'Daniel', '1996-07-16'),
(57, 'Emily', '1984-02-02'),
(58, 'Felix', '1991-04-20'),
(59, 'Gina', '1987-12-07'),
(60, 'Henry', '1982-06-24'),
(61, 'Irene', '1994-03-13'),
(62, 'Jake', '1989-10-30'),
(63, 'Katie', '1992-08-17'),
(64, 'Liam', '1980-05-04'),
(65, 'Megan', '1985-01-21'),
(66, 'Nathan', '1998-09-27'),
(67, 'Oliver', '1983-11-14'),
(68, 'Pamela', '1995-06-01'),
(69, 'Quincy', '1986-02-18'),
(70, 'Rachel', '1991-12-06'),
(71, 'Steve', '1988-07-23'),
(72, 'Tina', '1980-10-10'),
(73, 'Uriel', '1993-07-28'),
(74, 'Victoria', '1981-04-15'),
(75, 'William', '1990-02-01'),
(76, 'Xander', '1987-09-19'),
(77, 'Yvette', '1994-05-08'),
(78, 'Zara', '1983-12-25'),
(79, 'Aaron', '1999-08-11'),
(80, 'Bella', '1985-03-30'),
(81, 'Charlie', '1991-01-16'),
(82, 'David', '1988-10-03'),
(83, 'Ella', '1996-07-20'),
(84, 'Frank', '1984-04-06'),
(85, 'Gwen', '1992-12-23'),
(86, 'Harry', '1981-10-11'),
(87, 'Ivy', '1995-02-28'),
(88, 'Jack', '1986-11-15'),
(89, 'Kara', '1990-09-03'),
(90, 'Lena', '1983-06-20'),
(91, 'Max', '1980-03-08'),
(92, 'Nora', '1997-10-26'),
(93, 'Owen', '1982-08-12'),
(94, 'Penny', '1989-05-29'),
(95, 'Quinn', '1994-01-15'),
(96, 'Riley', '1987-07-02'),
(97, 'Sara', '1991-04-20'),
(98, 'Tommy', '1985-12-07'),
(99, 'Ulysses', '1999-09-24'),
(100, 'Vera', '1981-06-10');

SELECT *,
EXTRACT(YEAR FROM birthday) :: INTEGER,
MAKE_INTERVAL(EXTRACT(YEAR FROM CURRENT_DATE) :: INTEGER-EXTRACT(YEAR FROM birthday) :: INTEGER),
(birthday+MAKE_INTERVAL(EXTRACT(YEAR FROM CURRENT_DATE) :: INTEGER-EXTRACT(YEAR FROM birthday) :: INTEGER)) :: DATE AS curr_year_birthday,
(birthday+MAKE_INTERVAL(EXTRACT(YEAR FROM CURRENT_DATE) :: INTEGER-EXTRACT(YEAR FROM birthday) :: INTEGER)) :: DATE - CURRENT_DATE AS diff
FROM users
SELECT now() - INTERVAL '6 months 2 hours 30 minutes'



SELECT birthday, concat(
		extract(year from current_date),
		extract(month from birthday),
		extract(day from birthday)),
		extract(year from current_date),
		extract(month from birthday),
		extract(day from birthday) :: text,
		date(birthday + (EXTRACT(YEAR FROM current_date)-EXTRACT(YEAR FROM birthday) || ' years')::interval)
FROM users


select cast(concat(cast(extract('year' from current_date) as varchar), '05', '05') as date)


INSERT INTO users (user_id, user_name, b_day, b_month) VALUES
(1, 'Alice', '15', '05'),
(2, 'Bob', '22', '10'),
(3, 'Charlie', '08', '03'),
(4, 'David', '17', '12'),
(5, 'Eve', '03', '07'),
(6, 'Frank', '28', '09'),
(7, 'Grace', '12', '11'),
(8, 'Helen', '30', '06'),
(9, 'Ivan', '19', '04'),
(10, 'Jane', '05', '08'),
(11, 'Kevin', '24', '01'),
(12, 'Lily', '11', '02'),
(13, 'Mike', '18', '06'),
(14, 'Nancy', '27', '03'),
(15, 'Olivia', '09', '10'),
(16, 'Peter', '14', '07'),
(17, 'Quinn', '02', '04'),
(18, 'Rachel', '21', '12'),
(19, 'Sam', '17', '08'),
(20, 'Tom', '03', '02'),
(21, 'Ursula', '20', '05'),
(22, 'Victor', '28', '11'),
(23, 'Wendy', '06', '09'),
(24, 'Xavier', '13', '04'),
(25, 'Yvonne', '31', '01'),
(26, 'Zelda', '08', '08'),
(27, 'Adam', '25', '12'),
(28, 'Beth', '02', '07'),
(29, 'Chris', '19', '03'),
(30, 'Dana', '26', '10'),
(31, 'Eric', '14', '08'),
(32, 'Fiona', '03', '04'),
(33, 'George', '21', '09'),
(34, 'Hannah', '18', '01'),
(35, 'Isaac', '05', '11'),
(36, 'Julia', '22', '06'),
(37, 'Keith', '11', '03'),
(38, 'Lisa', '28', '05'),
(39, 'Matthew', '15', '02'),
(40, 'Nina', '02', '10'),
(41, 'Oscar', '19', '07'),
(42, 'Paula', '16', '12'),
(43, 'Quentin', '23', '09'),
(44, 'Rita', '10', '11'),
(45, 'Samantha', '27', '06'),
(46, 'Tim', '04', '08'),
(47, 'Uma', '01', '03'),
(48, 'Vincent', '08', '12'),
(49, 'Walter', '25', '02'),
(50, 'Xena', '13', '10'),
(51, 'Yolanda', '30', '05'),
(52, 'Zack', '17', '01'),
(53, 'Abigail', '04', '04'),
(54, 'Benjamin', '21', '11'),
(55, 'Catherine', '08', '09'),
(56, 'Daniel', '16', '07'),
(57, 'Emily', '02', '02'),
(58, 'Felix', '20', '04'),
(59, 'Gina', '07', '12'),
(60, 'Henry', '24', '06'),
(61, 'Irene', '13', '03'),
(62, 'Jake', '30', '10'),
(63, 'Katie', '17', '08'),
(64, 'Liam', '04', '05'),
(65, 'Megan', '21', '01'),
(66, 'Nathan', '27', '09'),
(67, 'Oliver', '14', '11'),
(68, 'Pamela', '01', '06'),
(69, 'Quincy', '18', '02'),
(70, 'Rachel', '06', '12'),
(71, 'Steve', '23', '07'),
(72, 'Tina', '10', '10'),
(73, 'Uriel', '28', '07'),
(74, 'Victoria', '15', '04'),
(75, 'William', '01', '02'),
(76, 'Xander', '19', '09'),
(77, 'Yvette', '08', '05'),
(78, 'Zara', '25', '01'),
(79, 'Aaron', '11', '08'),
(80, 'Bella', '30', '03'),
(81, 'Charlie', '16', '01'),
(82, 'David', '03', '10'),
(83, 'Ella', '20', '07'),
(84, 'Frank', '06', '04'),
(85, 'Gwen', '23', '12'),
(86, 'Harry', '11', '10'),
(87, 'Ivy', '28', '02'),
(88, 'Jack', '15', '11'),
(89, 'Kara', '03', '09'),
(90, 'Lena', '20', '06'),
(91, 'Max', '08', '03'),
(92, 'Nora', '26', '10'),
(93, 'Owen', '12', '08'),
(94, 'Penny', '29', '05'),
(95, 'Quinn', '15', '01'),
(96, 'Riley', '02', '07'),
(97, 'Sara', '20', '04'),
(98, 'Tommy', '07', '12'),
(99, 'Ulysses', '24', '09'),
(100, 'Vera', '10', '06');


INSERT INTO users (user_id, user_name, birthday, b_day, b_month) VALUES
(1, 'Alice', '1990-05-15', '15', '05'),
(2, 'Bob', '1985-10-22', '22', '10'),
(3, 'Charlie', '1995-03-08', '08', '03'),
(4, 'David', '1988-12-17', '17', '12'),
(5, 'Eve', '1992-07-03', '03', '07'),
(6, 'Frank', '1984-09-28', '28', '09'),
(7, 'Grace', '1997-11-12', '12', '11'),
(8, 'Helen', '1983-06-30', '30', '06'),
(9, 'Ivan', '1991-04-19', '19', '04'),
(10, 'Jane', '1987-08-05', '05', '08'),
(11, 'Kevin', '1994-01-24', '24', '01'),
(12, 'Lily', '1989-02-11', '11', '02'),
(13, 'Mike', '1998-06-18', '18', '06'),
(14, 'Nancy', '1986-03-27', '27', '03'),
(15, 'Olivia', '1993-10-09', '09', '10'),
(16, 'Peter', '1981-07-14', '14', '07'),
(17, 'Quinn', '1996-04-02', '02', '04'),
(18, 'Rachel', '1982-12-21', '21', '12'),
(19, 'Sam', '1980-08-17', '17', '08'),
(20, 'Tom', '1999-02-03', '03', '02'),
(21, 'Ursula', '1985-05-20', '20', '05'),
(22, 'Victor', '1990-11-28', '28', '11'),
(23, 'Wendy', '1988-09-06', '06', '09'),
(24, 'Xavier', '1983-04-13', '13', '04'),
(25, 'Yvonne', '1992-01-31', '31', '01'),
(26, 'Zelda', '1987-08-08', '08', '08'),
(27, 'Adam', '1981-12-25', '25', '12'),
(28, 'Beth', '1995-07-02', '02', '07'),
(29, 'Chris', '1989-03-19', '19', '03'),
(30, 'Dana', '1984-10-26', '26', '10'),
(31, 'Eric', '1996-08-14', '14', '08'),
(32, 'Fiona', '1980-04-03', '03', '04'),
(33, 'George', '1994-09-21', '21', '09'),
(34, 'Hannah', '1986-01-18', '18', '01'),
(35, 'Isaac', '1983-11-05', '05', '11'),
(36, 'Julia', '1990-06-22', '22', '06'),
(37, 'Keith', '1988-03-11', '11', '03'),
(38, 'Lisa', '1999-05-28', '28', '05'),
(39, 'Matthew', '1985-02-15', '15', '02'),
(40, 'Nina', '1993-10-02', '02', '10'),
(41, 'Oscar', '1981-07-19', '19', '07'),
(42, 'Paula', '1997-12-16', '16', '12'),
(43, 'Quentin', '1984-09-23', '23', '09'),
(44, 'Rita', '1992-11-10', '10', '11'),
(45, 'Samantha', '1987-06-27', '27', '06'),
(46, 'Tim', '1980-08-04', '04', '08'),
(47, 'Uma', '1991-03-01', '01', '03'),
(48, 'Vincent', '1989-12-08', '08', '12'),
(49, 'Walter', '1995-02-25', '25', '02'),
(50, 'Xena', '1982-10-13', '13', '10'),
(51, 'Yolanda', '1988-05-30', '30', '05'),
(52, 'Zack', '1993-01-17', '17', '01'),
(53, 'Abigail', '1986-04-04', '04', '04'),
(54, 'Benjamin', '1990-11-21', '21', '11'),
(55, 'Catherine', '1981-09-08', '08', '09'),
(56, 'Daniel', '1996-07-16', '16', '07'),
(57, 'Emily', '1984-02-02', '02', '02'),
(58, 'Felix', '1991-04-20', '20', '04'),
(59, 'Gina', '1987-12-07', '07', '12'),
(60, 'Henry', '1982-06-24', '24', '06'),
(61, 'Irene', '1994-03-13', '13', '03'),
(62, 'Jake', '1989-10-30', '30', '10'),
(63, 'Katie', '1992-08-17', '17', '08'),
(64, 'Liam', '1980-05-04', '04', '05'),
(65, 'Megan', '1985-01-21', '21', '01'),
(66, 'Nathan', '1998-09-27', '27', '09'),
(67, 'Oliver', '1983-11-14', '14', '11'),
(68, 'Pamela', '1995-06-01', '01', '06'),
(69, 'Quincy', '1986-02-18', '18', '02'),
(70, 'Rachel', '1991-12-06', '06', '12'),
(71, 'Steve', '1988-07-23', '23', '07'),
(72, 'Tina', '1980-10-10', '10', '10'),
(73, 'Uriel', '1993-07-28', '28', '07'),
(74, 'Victoria', '1981-04-15', '15', '04'),
(75, 'William', '1990-02-01', '01', '02'),
(76, 'Xander', '1987-09-19', '19', '09'),
(77, 'Yvette', '1994-05-08', '08', '05'),
(78, 'Zara', '1983-12-25', '25', '12'),
(79, 'Aaron', '1999-08-11', '11', '08'),
(80, 'Bella', '1985-03-30', '30', '03'),
(81, 'Charlie', '1991-01-16', '16', '01'),
(82, 'David', '1988-10-03', '03', '10'),
(83, 'Ella', '1996-07-20', '20', '07'),
(84, 'Frank', '1984-04-06', '06', '04'),
(85, 'Gwen', '1992-12-23', '23', '12'),
(86, 'Harry', '1981-10-11', '11', '10'),
(87, 'Ivy', '1995-02-28', '28', '02'),
(88, 'Jack', '1986-11-15', '15', '11'),
(89, 'Kara', '1990-09-03', '03', '09'),
(90, 'Lena', '1983-06-20', '20', '06'),
(91, 'Max', '1980-03-08', '08', '03'),
(92, 'Nora', '1997-10-26', '26', '10'),
(93, 'Owen', '1982-08-12', '12', '08'),
(94, 'Penny', '1989-05-29', '29', '05'),
(95, 'Quinn', '1994-01-15', '15', '01'),
(96, 'Riley', '1987-07-02', '02', '07'),
(97, 'Sara', '1991-04-20', '20', '04'),
(98, 'Tommy', '1985-12-07', '07', '12'),
(99, 'Ulysses', '1999-09-24', '24', '09'),
(100, 'Vera', '1981-06-10', '10', '06');



CREATE TABLE users (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    full_name VARCHAR(100) GENERATED ALWAYS AS (first_name || last_name) STORED
)

INSERT INTO users (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Michael', 'Johnson');


