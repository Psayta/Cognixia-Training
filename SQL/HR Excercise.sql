--Connect to HR 

-- 1.) Top 3 Lowest Salaries 
SELECT 
    employee_id, first_name, last_name, salary 
FROM
    employees 
ORDER BY salary 
FETCH NEXT 3 ROWS ONLY;

--2.) 2nd Highest salaries with phone numbers beginning with 515
SELECT 
  First_Name, Last_Name, Salary, Phone_number
FROM 
    Employees 
WHERE 
    Phone_number LIKE '515%' --AND Salary < (SELECT MAX(Salary) FROM Employees)
ORDER BY 
    Salary DESC
OFFSET 1 ROW
FETCH NEXT ROW ONLY;

--3.) Salaries above $10000 and hired before 1995 
SELECT 
    first_name,last_name,salary,hire_date
FROM 
    employees 
WHERE 
    Hire_date < '31-DEC-94' AND Salary > 10000;
    
--4.) All UNIQUE SALARIES 
SELECT DISTINCT
     salary 
FROM 
    employees
ORDER BY salary DESC;

--5.) Counts each employee for each unique salary 
SELECT DISTINCT 
    salary, 
    COUNT(*)
FROM 
    employees 
GROUP BY 
    salary
ORDER BY salary DESC;

--6.)Diplays average salaries for each department_id
SELECT 
    department_id,
    ROUND(AVG(salary)) 
FROM 
    employees 
GROUP BY
    department_ID
ORDER BY 
    AVG(Salary); 
    
--7.)
--a.) Displays employees hired between 1995 and 1997 
SELECT 
    first_name, 
    last_name, 
    hire_date,
    department_id
FROM 
    employees
WHERE 
    hire_date BETWEEN '31-DEC-94' AND '01-JAN-98'
    
--b.) Order bys the employed by department_id and hire_date 
ORDER BY 
    department_id, hire_date;
    
--8.) Displays the avg salaries of each department and removes odd salaries when rounded ** 
SELECT 
    department_id,
    ROUND(AVG(salary)) AS "AVG Salary" 
FROM 
    employees 
GROUP BY
    department_ID
HAVING 
    MOD(ROUND(AVG(salary)),2) = 0
    