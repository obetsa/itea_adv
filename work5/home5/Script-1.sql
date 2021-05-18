CREATE TABLE if not exists orders (
    order_id SERIAL PRIMARY KEY,
    created_dt DATE NOT NULL,
    updated_dt DATE NOT NULL,
    order_type text NOT NULL,
    description TEXT,
    status text NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT null,
    foreign key (creator_id) references employees (employee_id)
    );
   
CREATE TABLE if not exists employees (
    employee_id SERIAL PRIMARY key,
    fio text NOT NULL,
    position TEXT,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
    ON DELETE CASCADE
    );

CREATE TABLE if not exists departments (
	department_id SERIAL PRIMARY key,
	department_name text NOT null
	);


DROP TABLE IF EXISTS employees;

INSERT INTO employees VALUES (1, 'Dfcz', '213sdfz', '1');
INSERT INTO departments VALUES (1, 'Dfcz');