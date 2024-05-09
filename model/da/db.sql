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
    start_day date
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
    description nvarchar(100) not null,
    person_id int,
    FOREIGN KEY (person_id) REFERENCES person_tbl(id)
);

create table mft.sim_card_tbl(
    id int primary key auto_increment,
    number nvarchar(11) not null unique ,
    operator nvarchar(20) not null,
    price int not null,
    owner_id int,
    FOREIGN KEY (owner_id) REFERENCES mft.user_tbl(id)
);

create view mft.sim_card_count as
select owner_id, count(owner_id) as count_sim_card from mft.sim_card_tbl
group by owner_id;

-- MilitaryRecord
create table military_tbl
(
    id            int primary key auto_increment,
    serial_number varchar(11) not null,
    city          varchar(30) not null,
    organ         varchar(30) not null,
    start_date    date not null,
    end_date      date not null
);

# User
create table user_tbl(
    id int primary key auto_increment,
    username nvarchar(30) not null,
    password nvarchar(30) not null,
    status tinyint not null ,
    locked tinyint not null ,
    person_id int,
    FOREIGN KEY (person_id) REFERENCES person_tbl(id)
);



create table driving_license_tbl (
    id int primary key auto_increment,
    serial_number varchar(255),
    date timestamp,
    city varchar(255),
    expire_date timestamp
);

create table medical_record(
    id int primary key auto_increment,
    disease nvarchar(20) not null ,
    medicine nvarchar(20) not null ,
    datee date,
    doctor nvarchar(20),
    status bool not null
);
