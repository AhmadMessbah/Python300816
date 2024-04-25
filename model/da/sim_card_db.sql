create table sim_card_tbl(
    id int primary key auto_increment,
    number nvarchar(11) not null,
    operator nvarchar(20) not null,
    price int not null,
    owner nvarchar(40) not null
);
