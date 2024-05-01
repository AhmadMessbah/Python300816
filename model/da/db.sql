create database test;

create table person_tbl
(
    id     int primary key auto_increment,
    name   nvarchar(30) not null,
    family nvarchar(30) not null
);

create table lesson_tbl
(
    id        int primary key auto_increment,
    name      nvarchar(30) not null,
    grade     nvarchar(15) not null,
    teacher   nvarchar(30) not null,
    start_day datetime
);

create table product_tbl
(
    id        int primary key auto_increment,
    name      nvarchar(30) not null,
    brand     nvarchar(30) not null,
    serial    nvarchar(20) not null,
    buy_price float
);

create table driving_license_tbl (
    id int primary key auto_increment,
    serial_number varchar(255),
    date timestamp,
    city varchar(255),
    expire_date timestamp
);