create database mft;

create table user_tbl(
    id int primary key auto_increment,
    username nvarchar(30) not null,
    password nvarchar(30) not null,
    status tinyint not null ,
    locked tinyint not null
);