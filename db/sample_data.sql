INSERT INTO departments (name)
VALUES ('HR'), ('Engineering'), ('Sales');

INSERT INTO employees (name, department_id, email, salary)
VALUES
('Amit Sharma', 2, 'amit@company.com', 75000),
('Priya Verma', 3, 'priya@company.com', 65000),
('Rahul Singh', 1, 'rahul@company.com', 55000);

INSERT INTO products (name, price)
VALUES
('Laptop', 80000),
('Wireless Mouse', 1500),
('Mechanical Keyboard', 4500);

INSERT INTO orders (customer_name, employee_id, order_total, order_date)
VALUES
('John Doe', 1, 82000, '2025-01-01'),
('Alice Brown', 2, 4500, '2025-01-03');
