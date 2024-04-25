create database mft;

create table person_tbl(
    id int primary key auto_increment,
    name nvarchar(30) not null,
    family nvarchar(30) not null
);