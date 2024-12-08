-- vim:set ft=sqloracle cms=--\ %s:

-- connect bca24/bca24@172.16.36.101:1521/orcl
-- set lines 180
-- set pages 100
-- select table_name from user_tables order by table_name;

-- e_no, e_name, e_address, e_ph_no, dept_no, dept_name, job_id, salary,

--------
-- 01 --
--------
drop table employee;
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
---
alter table employee add hiredate date;
alter table employee modify (job_id varchar2(15));
alter table employee rename column emp_no to e_no;
alter table employee modify (job_id char(5));

--------
-- 02 --
--------
insert into employee values (11, 'James', 'p1', 1, 10, 'D10', 10, 72000, to_date('1-May-81'));
insert into employee values (12, 'Hudson', 'p1', 1, 40, 'MECH', 10, 75000, to_date('3-Dec-81'));
insert into employee values (13, 'Sully', 'p1', 1, 50, 'SALES', 10, 65000, to_date('17-Dec-81'));
insert into employee values (14, 'def', 'p1', 1, 51, 'CLERK', 10, 92000, to_date('12-Jan-80'));
insert into employee values (15, 'efg', 'p1', 1, 70, 'ANALYST', 10, 80000, to_date('1-Jan-82'));
insert into employee values (16, 'fgh', 'p1', 1, 71, 'IT PROF', 10, 73000, to_date('16-Mar-85'));
insert into employee values (17, 'ghi', 'p1', 1, 90, 'PRESIDENT', 10, 70000, to_date('22-Sep-78'));
insert into employee values (18, 'hij', 'p1', 1, 41, 'MGR', 10, 68000, to_date('13-Mar-83'));

select * from employee;

select * from employee
where dept_name = 'D10';

update employee
set e_address = 'nagpur'
where e_no = 12;

select * from employee
where dept_name = 'MECH';

update employee
-- set email = ''
set e_ph_no = 0
where e_name = 'James';

select * from employee
where dept_name = 'SALES';

--------
-- 03 --
--------
alter table employee
rename column dept_name to designation;
---
select
    e_no,
    e_name,
    salary
from employee
where designation = 'MANAGER';

select * from employee
where salary > (
    select max(e.salary) from employee e
    where e.designation = 'IT PROFF'
);

select * from employee
where hiredate > to_date('31-Dec-1981')
order by designation asc;

select
    e_name,
    trunc((sysdate - hiredate) / 365) as experience,
    trunc(salary / 30) as daily_salary
from employee;

select * from employee
where designation = 'CLERK' or designation = 'ANALYST';

select * from employee
where hiredate = to_date('1-May-81')
   or hiredate = to_date('3-Dec-81')
   or hiredate = to_date('17-Dec-81')
   or hiredate = to_date('12-Jan-80');

select * from employee
where dept_no = 10
   or dept_no = 20;

select * from employee
where e_name like 'S%';

select substr(e_name, 1, 5) from employee
where e_name like 'H%';

select * from employee
where designation != 'PRESIDENT'
   or designation != 'MGR'
order by salary asc;

--------
-- 04 --
--------
drop table dept;
create table dept (
    dept_no int,
    dept_name varchar(15)
);
insert into dept values (1, 'A1');
insert into dept values (2, 'B2');
insert into dept values (3, 'C3');
insert into dept values (10, 'D10');
insert into dept values (40, 'MECH');
insert into dept values (41, 'MGR');
insert into dept values (50, 'SALES');
insert into dept values (51, 'CLERK');
---
select dept_no from employee
union
select dept_no from dept;

select dept_no from employee
union all
select dept_no from dept;

select dept_no from employee
minus
select dept_no from dept;

select dept_no from dept
minus
select dept_no from employee;

--------
-- 05 --
--------
drop table sailors;
drop table boats;
drop table reserves;

create table sailors (sid int primary key, sname varchar(5), rating int, age int);
insert into sailors values (1, 'aria', 5, 20);
insert into sailors values (2, 'bob', 4, 18);
insert into sailors values (3, 'cat', 2, 16);
insert into sailors values (4, 'dave', 5, 24);

create table reserves (sid int, bid int, day date);
insert into reserves values (1, 101, to_date('1-Jan-00'));
insert into reserves values (1, 102, to_date('1-Jan-00'));
insert into reserves values (2, 101, to_date('2-Jan-00'));
insert into reserves values (3, 102, to_date('2-Jan-00'));

create table boats (bid int primary key, bname varchar(5), color varchar(3));
insert into boats values (101, 'ss a', 'wht');
insert into boats values (102, 'ss b', 'red');
---
select s.* from sailors s, reserves r, boats b
where s.sid = r.sid
  and r.bid = 101;

select b.bname from sailors s, reserves r, boats b
where s.sid = r.sid
  and b.bid = r.bid
  and s.sname = 'bob';

select s.sname, s.age from sailors s, reserves r, boats b
where s.sid = r.sid
  and b.bid = r.bid
  and b.color = 'red'
order by s.age asc;

select s.sname from sailors s, reserves r
where s.sid = r.sid
group by r.bid;

select unique s.sname from sailors s, reserves r, boats b
where s.sid = r.sid
  and b.bid = r.bid
  and r.day = r.day;

--------
-- 06 --
--------
--------
-- 07 --
--------
--------
-- 08 --
--------
create table emp (
    empno number(6) primary key check (no > 100),
    ename varchar(20),
    job varchar(15),
    deptno number(3) unique,
    sal number(7, 2)
)
