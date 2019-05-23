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
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    add_flight = ("INSERT INTO flight "
                "(op_nb, origin, destination) "
                "VALUES ('"+op_nb+"', '"+ori+"', '"+dst+"')")

    data_flight = (op_nb, ori, dst)

    # Insert new flight
    cursor.execute(add_flight)

    # Make sure data is committed to the database
    conn.commit()
    cursor.close()
    conn.close()
    return "ok"





def edit_flight(op_nb, ori, dst):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    print(op_nb , ori, dst)

    sql = ''' UPDATE flight
              SET origin = ? ,
                  destination = ? 
              WHERE op_nb = ?'''


    # Insert new flight
    cursor.execute(sql, (ori, dst, op_nb))

    # Make sure data is committed to the database
    conn.commit()
    cursor.close()
    conn.close()
    return "ok"