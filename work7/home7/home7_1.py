"""Продолжаем работу с таблицами из домашнего задания №5 и классом Заяка из домашнего задания №2:
Расширить поведение класса Заявка. Теперь заявка должна иметь следующие методы, которые будут взаимодействовать
с БД (получать данные, изменять данные, удалять данные и т.д.):
создание новой заявки;
изменение статуса;
изменение описания;
изменение id создателя;
При изменении данных заявки в БД необходимо изменять поле updated_dt.
Аналогичные классы создать для департаментов и сотрудников. Во время выполнения задания постарайтесь максимально
использовать концепции ООП (инкапсуляцию, наследование, полиморфизм).
"""

import time
import psycopg2
from psycopg2 import sql
from datetime import datetime
from envparse import Env

from abc import ABC, abstractmethod

env = Env()
DB_URL = env.str("SOME_DB_URL", default="postgres://postgres:********@localhost:5432/postgres")
connect = psycopg2.connect(DB_URL)


"""
CREATE TABLE if not exists orders (
    order_id SERIAL PRIMARY KEY,
    created_dt DATE NOT NULL,
    updated_dt,
    order_type TEXT NOT NULL,
    description TEXT,
    status text NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    foreign key (creator_id) references employees (employee_id)
    );
CREATE TABLE if not exists employees (
    employee_id SERIAL PRIMARY key,
    fio text NOT NULL,
    position TEXT,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
    );
CREATE TABLE if not exists departments (
	department_id SERIAL PRIMARY key,
    department_name TEXT NOT NULL
    );
"""



class BaseModel(ABC):
    @abstractmethod
    def create_new_data(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_data_by_id(self, *args, **kwargs):
        pass

    def real_method(self):
        pass


class DataRequiredException(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs


class Order(BaseModel):
    count_request = 0

    CREATE_ORDER_QUERY = sql.SQL("""INSERT INTO orders (created_dt, updated_dt, order_type, description, status,
                                    serial_no, creator_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING order_id""")
    DELETE_ORDER_QUERY = sql.SQL("""DELETE FROM orders WHERE order_id = %s""")
    CHANGE_ORDER_QUERY = sql.SQL("""UPDATE orders SET updated_dt = %s, status = %s WHERE order_id = %s""")

    def __init__(self, created_dt, updated_dt, order_type,description, status, serial_no, creator_id, order_id=None):
        Order.date_object = datetime.now().strptime("%d %B, %Y")
        self.created_dt = Order.date_object
        self.updated_dt = updated_dt
        self.order_type = order_type
        self.description = description
        self.status = status
        self.serial_no = serial_no
        self.creator_id = creator_id
        self.order_id = order_id
        Order.count_request += 1

    def create_date(self):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CREATE_ORDER_QUERY, (datetime.now(), self.order_type, self.description,
                                                               self.status, self.serial_no, self.creator_id))
            order_id = cursor.fetchone()[0]
            self.order_id = order_id
        return {"order_id": order_id}

    def delete_data(self):
        if not self.order_id:
            raise DataRequiredException(message="Enter order_id")
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.DELETE_ORDER_QUERY, (self.order_id))

    def status_change(self, new_status):
        with connect, connect.cursor() as cursor:
            cursor.execute(self.__class__.CHANGE_ORDER_QUERY, (new_status, self.order_id))

    def request_id(self):
        return self.__id

    def r_close(self):
        self.status = "closed"

    def r_open(self):
        self.status = "active"

    def __str__(self):
        pending = datetime.now() - self.time
        delta = divmod(pending.total_seconds(), 60)
        return f'pending time: {delta[0]} minutes and {delta[1]} seconds'

r = Request(id="1", name='Test', ser_number='222')
t = Request(id="2", name='Test2', ser_number='SB222')
time.sleep(2)
print(r.status)
print(r.request_id())
print(t.request_id())
print(r.time)
print(Request.count_request)
print(r)
r.r_close()
print(r.status)