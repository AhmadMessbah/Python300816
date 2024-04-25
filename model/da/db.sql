create database mft;

-- Person
create table person_tbl
(
    id     int primary key auto_increment,
    name   nvarchar(30) not null,
    family nvarchar(30) not null
);

-- Lesson
create table lesson_tbl
(
    id        int primary key auto_increment,
    name      nvarchar(30) not null,
    grade     nvarchar(15) not null,
    teacher   nvarchar(30) not null,
    start_day datetime
);

-- Product
create table product_tbl
(
    id        int primary key auto_increment,
    name      nvarchar(30) not null,
    brand     nvarchar(30) not null,
    serial    nvarchar(20) not null,
    buy_price float
);
