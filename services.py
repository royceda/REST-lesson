from __future__ import print_function
from datetime import date, datetime, timedelta
import sqlite3




def flights():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    query = ("SELECT op_nb, origin, destination FROM flight ")
    cursor.execute(query)

    arr = []
    for (op_nb, origin, destination) in cursor:
        tmp = {
            "op_nb" : op_nb,
            "origin" : origin,
            "destination" : destination 
        }
        arr.append(tmp)
    print(arr)

    cursor.close()
    conn.close()
    return arr




def get_flight(id):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    query = ("SELECT op_nb, origin, destination FROM flight WHERE op_nb = '"+id+"'")
    cursor.execute(query)
    arr = []

    for (op_nb, origin, destination) in cursor:
        tmp = {
            "op_nb" : op_nb,
            "origin" : origin,
            "destination" : destination 
        }
        arr.append(tmp)
    cursor.close()
    conn.close()
    return arr



def create_flight(op_nb, ori, dst):
    cnx = mysql.connector.connect(user='scott', database='employees')
    cursor = cnx.cursor()

    tomorrow = datetime.now().date() + timedelta(days=1)

    add_flight = ("INSERT INTO flight "
                "(op_nb, origin, destination) "
                "VALUES (%s, %s, %s)")

    data_flight = ('AF1000', 'CDG', 'MAD')

    # Insert new employee
    cursor.execute(add_flight, data_flight)
    flt_no = cursor.lastrowid

    # Insert salary information
    data_salary = {
        'op_nb': flt_no,
        'origin': ori,
        'destination': dst
    }
    cursor.execute(add_flight, data_flight)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()





def edit_flight(op_nb, ori, dst):
    cnx = mysql.connector.connect(user='scott', database='employees')
    cursor = cnx.cursor()
    #tomorrow = datetime.now().date() + timedelta(days=1)

    add_flight = ("UPDATE flight "
                "(op_nb, origin, destination) "
                "WHERE op_nb = (%s)"
                "SET ori = %s, dst = %s")

    data_flight = ('AF1000', 'CDG', 'MAD')
    #data_flight = (op_nb, ori, dst)

    # Insert new employee
    cursor.execute(add_flight, data_flight)
    flt_no = cursor.lastrowid

    # Insert salary information
    data_flight = {
        'op_nb': flt_no,
        'origin': ori,
        'destination': dst
    }
    cursor.execute(add_flight, data_flight)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()