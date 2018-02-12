import sqlite3
import sys

def add_entry(cursor):
    name=input('Enter the name: ')
    systems=input('Enter what consoles the title is available: ')
    rating=input("Enter this game's rating (0-5): ")
    year=input('What year was this game released: ')
    cursor.execute('INSERT INTO Games VALUES (?,?,?,?);', [name, systems, rating, year])
    
    consoles=systems.split(',')
    for item in consoles:
        cursor.execute('SELECT MAX ID FROM Inventory WHERE Console=?;'[item])
        cursor.execute('INSERT INTO Inventory VALUES (?,?,?,?,?);', [ID,name,systems,0,0])
    
        edit_stock=input('Adjust game stock? [Y/N]:')
        if edit_stock=='Y':
            mod_stock(cursor, ID, name, systems)

def mod_stock(cursor, ID, name, console):
    stock=input('Enter the number of games in stock: ')
    holds=input('Enter the number of copies on hold: ')
    cursor.execute('INSERT INTO Inventory VALUES (?,?,?,?,?);', [ID,name,console,stock,holds])

def title_srch(cursor, title):
    cursor.execute('SELECT * FROM Games WHERE Title=?;', [title])
    result = str(cursor.fetchone())
    print(result)
    
def title_inv(cursor, title):
    cursor.execute('SELECT * FROM Inventory WHERE Title=?;', [title])
    result = str(cursor.fetchone())
    print(result)
    
def make_sale(cursor, title):
    cursor.execute('SELECT In Stock FROM Inventory WHERE Title=?;', [title])
    stock=int(cursor.fetchone())
    cursor.execute('SELECT On Hold FROM Inventory WHERE Title=?;', [title])
    on_hold=int(cursor.fetchone())
    
    if (on_hold<stock):
        stock=stock-1
        cursor.execute('UPDATE Inventory SET In Stock=? WHERE Title=?;', [stock, title])
    
    else:
        print('All available copies on hold; Transaction terminated.')
    
def console_srch(cursor, cnsl):
    cursor.execute('SELECT Title FROM Games WHERE Console=?;', [cnsl])
    result = cursor.fetchall()
    for row in result:
        print(row)    
    
def rating_srch(cursor, rtng):
    print("Enter the search type: \n")
    print("1) Less than               : <  \n")
    print("2) Less than or equal to   : =< \n")
    print("3) Equal to                : =  \n")
    print("4) Greater than or equal to: >= \n")
    print("5) Greater than            : <  \n")
    srch_type = input('Enter operator (not number): ')
    sql = 'SELECT Title FROM Games WHERE rating'+str(srch_type)+str(rtng)+';'
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
    
def year_srch(cursor, year):
    print("Enter the search type: \n")
    print("1) Less than               : <  \n")
    print("2) Less than or equal to   : =< \n")
    print("3) Equal to                : =  \n")
    print("4) Greater than or equal to: >= \n")
    print("5) Greater than            : <  \n")
    srch_type = input("Select operator (not number): ")
    sql = 'SELECT Title FROM Games WHERE year'+str(srch_type)+str(year)+';'
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)