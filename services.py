from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector


def flights():
    cnx = mysql.connector.connect(user='root', password='root', database='flight')
    cursor = cnx.cursor()

    query = ("SELECT op_nb, origin, destination FROM flight ")
    cursor.execute(query)

    arr = []
    for (op_nb, origin, destination) in cursor:
        arr.append((op_nb, origin, destination))
    print(arr)

    cursor.close()
    cnx.close()
    return arr




def flight(op_nb):
    cnx = mysql.connector.connect(user='root', password='root', database='flight')
    cursor = cnx.cursor()

    query = ("SELECT op_nb, origin, destination FROM flight WHERE op_nb = %s")
    cursor.execute(query, (op_nb))

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(
            last_name, first_name, hire_date))

    cursor.close()
    cnx.close()



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