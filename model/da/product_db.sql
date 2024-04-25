create database mft1;

create table product_tbl(
    pro_id int primary key auto_increment,
    pro_name nvarchar(30) not null,
    pro_brand nvarchar(30) not null,
    pro_serial int not null,
    pro_buyprice float);
