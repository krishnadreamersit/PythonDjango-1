import sys
import mysql.connector
import sqlite3

DB_FILE = "mydb.sqlite3"

def create_table1():
    sql="""
        CREATE TABLE IF NOT EXISTS tbl_person(
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            contact_address TEXT NOT NULL
        );
    """
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Create table successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

def create_table2():
    sql="""
        CREATE TABLE IF NOT EXISTS tbl_person(
            id int(11) PRIMARY KEY,
            full_name varchar(50) NOT NULL,
            contact_address varchar (50) NOT NULL
        );
    """
    try:
        conn = mysql.connector.connect(host='localhost', database='test', user='root', password='')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Create table successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

def insert_record1(): # Insert Record in SQLiteDB
    sql="""INSERT INTO tbl_person(id, full_name, contact_address) values(?, ?, ?)"""
    values = (1, 'Ram Poudel','Kathmandu')
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        print("Insert record successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
        cursor.close()
        conn.close()

def insert_record2(): # Insert Record in MySQL
    sql="""INSERT INTO tbl_person(id, full_name, contact_address) values(%s, %s, %s)"""
    values = (1, 'Ram Poudel','Kathmandu')
    try:
        conn = mysql.connector.connect(host='localhost', database='test', user='root', password='')
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Insert record successfully")
    except:
        print("Error : ", sys.exc_info()[0])
    finally:
       pass

# Test
# create_table1()
# insert_record1()

# create_table2()
insert_record2()