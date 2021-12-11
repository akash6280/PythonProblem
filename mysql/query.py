create_table_query = """ create table employee_payroll ( id  INT unsigned NOT NULL AUTO_INCREMENT,
  name  VARCHAR(150) NOT NULL,  salary Double NOT NULL, 
   start  DATE NOT NULL,  PRIMARY KEY (id) );"""

insert_data_query = """insert into employee_payroll(name,salary,start) values 
                    ('mark',20.0,'2019-01-03'), ('bill',10.0,'2020-01-03'), ('charlie',30.0,'2021-01-03');"""

show_table_employee_payroll = """select * from employee_payroll;"""

specific_employee_salary = """select salary from employee_payroll where name='bill';"""

employee_joining_dates = """select * from employee_payroll where start between cast('2019-01-03' as date) and date(
now()); """

alter_table = """alter table employee_payroll add gender char(1) after name;"""

update_mark_and_bill = """update employee_payroll set gender='F' where name='mark' or  name='bill';"""

update_charlie = """update employee_payroll set gender='M' where name='charlie';"""

avg_salary_query = """select avg(salary) from employee_payroll where gender='M' group by gender;"""

max_salary_query = """select max(salary) from employee_payroll where gender='M' group by gender;"""

min_salary_query = """select min(salary) from employee_payroll where gender='M' group by gender;"""

sum_salary_query = """select sum(salary) from employee_payroll where gender='M' group by gender;"""

count_salary_query = """select count(gender) from employee_payroll where gender='M' group by gender;"""

drop_table_employee_payroll = """DROP TABLE employee_payroll;"""

delete_row_id_1 = """delete from employee_payroll where id=1"""

# select avg(salary) from employee_payroll where gender='F' group by gender;
#
# select max(salary) from employee_payroll where gender='F' group by gender;
#
# select min(salary) from employee_payroll where gender='F' group by gender;
#
# select count(gender) from employee_payroll where gender='F' group by gender;
# select sum(salary) from employee_payroll where gender='F' group by gender;

create_books_table_query = """
    CREATE TABLE  books (
        id INT,
        author VARCHAR(100),
        title VARCHAR(100),
        image VARCHAR(100),
        quantity INT,
        price INT,
        description TEXT
    )
"""

inner_join_query = """
select author, salary   
from employee_payroll,books
where employee_payroll.id = books.id 
"""
