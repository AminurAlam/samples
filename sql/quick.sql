-- sqlplus/nolog
-- connect bca24/bca24@172.16.36.101:1521/orcl
-- set lines 180
-- set pages 100

select table_name from user_tables order by table_name;
create table stud (roll int, sname varchar(20));

insert into stud values (1, '');
insert into stud values (2, '');
insert into stud values (3, '');
insert into stud values (4, '');
insert into stud values (5, '');
insert into stud values (6, '');
insert into stud values (7, '');
insert into stud values (8, '');
insert into stud values (9, '');
insert into stud values (10, '');
