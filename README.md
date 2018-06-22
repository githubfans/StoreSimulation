DROP TABLE IF EXISTS `Seller`;
CREATE TABLE Seller (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    dateadd datetime,
    in_use CHAR(1) NOT NULL DEFAULT 'n'
);
DROP TABLE IF EXISTS `Seller_Timeline`;
CREATE TABLE Seller_Timeline (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    idSeller INT(10) NOT NULL,
    timeline TEXT NOT NULL,
    dateadd datetime
);
DROP TABLE IF EXISTS `Users`;
CREATE TABLE Users (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    dateadd datetime,
    in_use CHAR(1) NOT NULL DEFAULT 'n'
);
DROP TABLE IF EXISTS `Users_Timeline`;
CREATE TABLE Users_Timeline (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    idUser INT(10) NOT NULL,
    timeline TEXT NOT NULL,
    dateadd datetime
);
DROP TABLE IF EXISTS `Transaction`;
CREATE TABLE Transaction (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    idUser INT(10) NOT NULL,
    idSeller INT(10) NOT NULL,
    idSession VARCHAR(40) NOT NULL,
    description TEXT NOT NULL,
    dateadd datetime,
    numItems INT(10) NOT NULL DEFAULT 0,
    totalprice INT(10) NOT NULL DEFAULT 0
);
DROP TABLE IF EXISTS `SessionOrders`;
CREATE TABLE SessionOrders (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    idProduct INT(10) NOT NULL,
    idUser     INT(10) NOT NULL,
    sessioncode VARCHAR(10) NOT NULL,
    dateadd datetime,
    numItems INT(10) NOT NULL DEFAULT 0,
    price INT(10) NOT NULL DEFAULT 0
);
DROP TABLE IF EXISTS `Products`;
CREATE TABLE Products (
    id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    idSeller INT(10) NOT NULL,
    title VARCHAR(30) NOT NULL,
    stock INT(4) NOT NULL,
    description TEXT NOT NULL,
    dateadd datetime,
    in_use CHAR(1) NOT NULL DEFAULT 'n',
    price INT(10) NOT NULL DEFAULT 0
);

use demotrx; select title, stock from Products where 1 and stock<=10 order by stock limit 0,10 ; select sum(stock) from Products; select MAX(id), MIN(id), TIMEDIFF(MAX(dateadd), MIN(dateadd)) as timef, unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd)) as secs, MAX(id)/(unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd))) as trx_in_1sec, MAX(id)/((unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd)))/60) as trx_in_1minute from Transaction; select MAX(dateadd), MIN(dateadd), sum(numItems) items,unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd)) as secs, SUM(numItems)/(unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd))) as items_in_sec, SUM(numItems)/(unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd)))*60 as items_in_min  from SessionOrders; SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'demotrx'; show status where variable_name like 'connections%' or variable_name like 'thread%' or variable_name like 'bytes%' or variable_name like 'que%' or variable_name like 'com_sel%';
