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

# FinancialDoc
create table FinancialDoc_tbl(
    id int primary key auto_increment,
    amount decimal(15,2) not null,
    date_time datetime not null,
    doc_type nvarchar(8) not null,
    description nvarchar(100) not null
);

# SimCard
create table sim_card_tbl(
    id int primary key auto_increment,
    number nvarchar(11) not null,
    operator nvarchar(20) not null,
    price int not null,
    owner nvarchar(40) not null
);

-- MilitaryRecord
create table military_tbl
(
    id         int primary key auto_increment,
    serial_num int,
    start_date datetime,
    end_date   datetime,
    city       nvarchar(30) not null,
    organ      nvarchar(30) not null
);

# User
create table user_tbl(
    id int primary key auto_increment,
    username nvarchar(30) not null,
    password nvarchar(30) not null,
    status tinyint not null ,
    locked tinyint not null
);



create table driving_license_tbl (
    id int primary key auto_increment,
    serial_number varchar(255),
    date timestamp,
    city varchar(255),
    expire_date timestamp
);