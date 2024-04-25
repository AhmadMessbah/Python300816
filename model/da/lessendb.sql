create table lesson_tbl(
    id int primary key auto_increment,
    name nvarchar(30) not null,
    grade nvarchar(15) not null,
    teacher nvarchar(30) not null,
    start_day datetime
);
