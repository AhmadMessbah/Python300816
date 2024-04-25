create table lesson_tbl(
    id int primary key auto_increment,
    number nvarchar(11) not null,
    operator nvarchar(20) not null,
    price nvarchar(20) not null,
    owner nvarchar(40) not null
);
