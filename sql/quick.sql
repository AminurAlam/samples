-- vim:set ft=sqloracle cms=--\ %s:

-- connect bca25/bca24@172.16.36.101:1521/orcl
-- set lines 181
-- set pages 101
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

select e_name, substr(e_name, 1, 5) as substr from employee
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

create table sailors (sid int primary key, sname varchar(20), rating int, age number);
insert into sailors values (22, 'Dustin', 7, 45);
insert into sailors values (29, 'Brutus', 1, 33);
insert into sailors values (31, 'Lubber', 8, 55.5);
insert into sailors values (32, 'Andy', 8, 25.5);
insert into sailors values (58, 'Rusty', 10, 35);
insert into sailors values (64, 'Horatio', 7, 35);
insert into sailors values (71, 'Zorba', 10, 16);
insert into sailors values (74, 'Horatio', 9, 40);
insert into sailors values (85, 'Art', 3, 25.5);
insert into sailors values (95, 'Bob', 3, 63.5);

create table reserves (sid int, bid int, day date);
insert into reserves values (22, 101, to_date('10-Oct-98'));
insert into reserves values (22, 102, to_date('10-Oct-98'));
insert into reserves values (22, 103, to_date('08-Oct-98'));
insert into reserves values (22, 104, to_date('07-Oct-98'));
insert into reserves values (31, 102, to_date('10-Nov-98'));
insert into reserves values (31, 103, to_date('06-Nov-98'));
insert into reserves values (31, 104, to_date('12-Nov-98'));
insert into reserves values (64, 101, to_date('05-Sep-98'));
insert into reserves values (64, 102, to_date('08-Sep-98'));
insert into reserves values (74, 103, to_date('08-Sep-98'));

create table boats (bid int primary key, bname varchar(19), color varchar(10));
insert into boats values (101, 'Interlake', 'blue');
insert into boats values (102, 'Interlake', 'red');
insert into boats values (103, 'Clipper', 'green');
insert into boats values (104, 'Marine', 'red');
---
select s.* from sailors s, reserves r
where s.sid = r.sid
  and r.bid = 101;

select b.bname from sailors s, reserves r, boats b
where s.sid = r.sid
  and b.bid = r.bid
  and s.sname = 'Bob';

select s.sname, s.age
from sailors s, reserves r, boats b
where s.sid = r.sid
  and b.bid = r.bid
  and b.color = 'red'
order by s.age asc;

select distinct s.sname
from sailors s, reserves r
where s.sid = r.sid;

select distinct s.sid, s.sname
from sailors s, reserves r1, reserves r2
where s.sid = r1.sid
  and s.sid = r2.sid
  and r1.day = r2.day
  and r1.bid != r2.bid;

select distinct s.sname
from sailors s, boats b, reserves r
where s.sid = r.sid
  and r.bid = b.bid
  and (b.color = 'red' or b.color = 'green');

select sname, age from sailors
where age = (select min(s.age) from sailors s);

select count(sname) from sailors;

select rating, avg(age) from sailors
group by rating;

select rating, avg(age) from sailors
group by rating
having count(*) > 1;

--------
-- 06 --
--------
select designation, sum(salary) as total_salary
from employee
group by designation;

select designation, min(salary) as min_salary
from employee
group by designation;

select designation, count(designation) as count
from employee
group by designation;

SELECT * FROM employee
order by salary asc;

SELECT * FROM employee
where salary > 16000;

--------
-- 07 --
--------
--------
-- 08 --
--------
create table emp (
    empno number(6) primary key check (no > 100),
    ename varchar(20) not null,
    job varchar(15) not null,
    deptno number(3) unique,
    sal number(7, 2)
);

--------
-- 09 --
--------
savepoint xyz;
rollback xyz;
commit;
--------
-- 10 --
--------
