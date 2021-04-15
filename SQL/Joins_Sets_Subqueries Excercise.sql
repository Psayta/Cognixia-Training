--CONNECT: HR 

--1.) Every employees job and department 
SELECT
    first_name, last_name, job_title, department_name
FROM 
    employees e 
LEFT JOIN 
    jobs j 
ON  
    e.job_id = j.job_id 
LEFT JOIN 
    departments d 
ON 
    e.department_id = d.department_id;
    
--2.) All employees dependents 
--a.)join 
SELECT 
    e.first_name, e.last_name, e.email 
FROM 
    employees e
RIGHT JOIN 
    dependents d 
ON 
    e.employee_id = d.employee_id;

--b.) Subquery 
SELECT 
    first_name, last_name, email 
FROM 
    employees 
WHERE 
    employee_id IN( 
    SELECT 
        employee_id 
    FROM 
        dependents 
    );
    
--3.) UNION between employees and dependents 
SELECT first_name, last_name FROM employees 
UNION 
SELECT first_name, last_name FROM dependents; 

--4.) Employees who make above average and removes managers 
SELECT 
    job_id
FROM 
    employees
WHERE  
    salary > (
    SELECT 
    AVG(Salary) 
    FROM Employees)
MINUS 
SELECT 
    job_id
FROM 
    jobs 
WHERE job_title LIKE '%Manager';
    

--5.) Job titles with average salaries and amount of people 
SELECT  
    job_title,
    COUNT(e.Job_id),
    AVG(e.salary)
FROM 
    employees e
LEFT JOIN 
    jobs j
ON 
    j.job_id = e.job_id
GROUP BY 
    job_title; 
    
--6.) 
SELECT 
    city, 
    state_province,
    COUNT(e.job_id) 
FROM 
    locations
WHERE location_id IN 
    ( 
    SELECT 
        department_id
    FROM 
        departments 
    WHERE department_id IN
        (
        SELECT 
            job_id
        FROM 
            employees 
        )
    );

SELECT 
    employee_id, 
    city, 
    state_province
FROM 
    employees e 
LEFT JOIN 
    departments d 
ON 
    e.department_id = d.department_id 
LEFT JOIN 
    locations l 
ON 
    d.location_id = l.location_id 


    