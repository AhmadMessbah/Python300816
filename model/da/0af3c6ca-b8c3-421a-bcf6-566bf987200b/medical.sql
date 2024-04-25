create table medical_record(
    id int primary key auto_increment,
    disease nvarchar(20) not null ,
    medicine nvarchar(20) not null ,
    datee date,
    doctor nvarchar(20),
    status bool not null
);