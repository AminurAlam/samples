/* vim:set ft=sqloracle cms=/*\ %s\ \*\/: */
/* connect bca24/bca24@172.16.36.101:1521/orcl */
/* set lines 180 */
/* set pages 100 */

/* select table_name from user_tables order by table_name; */
/* create table stud (roll int, sname varchar(20)); */
/**/
/* insert into stud values (1, ''); */
/* insert into stud values (2, ''); */
/* insert into stud values (3, ''); */
/* insert into stud values (4, ''); */
/* insert into stud values (5, ''); */
/* insert into stud values (6, ''); */
/* insert into stud values (7, ''); */
/* insert into stud values (8, ''); */
/* insert into stud values (9, ''); */
/* insert into stud values (10, ''); */

-- 1
create table employee (
    emp_no int primary key,
    e_name varchar(20),
    e_address varchar(10),
    e_ph_no int,
    dept_no int,
    dept_name varchar(10),
    job_id char(10),
    salary int
);

alter table employee add hiredate date;
alter table employee modify (job_id varchar2(20));
alter table employee rename column emp_no to e_no;
alter table emp modify (job_id char(5));

-- 2

-- 8
create table emp (
    empno number(6) primary key check (no > 100),
    ename varchar(20),
    job varchar(15),
    deptno number(3) unique,
    sal number(7, 2)
)
