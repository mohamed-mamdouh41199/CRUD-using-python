# Import flask and render_template and database module 
from flask import Flask , request,  render_template


import string
import random 


# import database module 
import sqlite3

import os

os.chdir(r"E:\web\Zero\4- Python\CRUD")

app = sqlite3.connect('data.db')


# Create a Cursor object
cursor = app.cursor()

# Execute SQL command 
# cursor.execute("CREATE TABLE IF NOT EXISTS Products \
#     (P_Name TEXT, P_Category TEXT, P_Color TEXT, P_Price INTEGER , P_Serial INTEGER)")

def get_Products():
        
    try:
        # connect to data base 
        app = sqlite3.connect('data.db')
        
        # Create a Cursor object
        cursor = app.cursor()
        
        cursor.execute("select *from Products")
        # Save the results so we can use them later
        count = cursor.fetchall()
        print(f"you have in Products table {len(count)} Products :-")
        
        # show all
        def show_all():
            cursor.execute("select *from Products")
            count = cursor.fetchall()
            for product in count:
                print(f"\n Product Name: {product[0]} \t Product Category : {product[1]} \t Product Color : {product[2]} \t Product Price : {product[3]} \
                        \t Product S : {product[4]}")
                
        show_all()
            
       
    except:
        print("Error while connecting to MySQL")

    finally:
        # clos the tables
        app.close()
        print("connection to database have been closed, THANK YOU ")

get_Products()

# Commit the transaction
app.commit()


cursor.execute("select *from Products")
# Save the results so we can use them later
Products = cursor.fetchall() 

print(Products)

# clos the tables
app.close()


# name the app 
CRUD_app = Flask(__name__)

# Create routes
@CRUD_app.route('/')
def home():
    return render_template("CRUD.html" , Products=Products)



@CRUD_app.route('/' , methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        try:
            P_N = request.form['product_name']
            P_C = request.form['product_category']
            P_Co = request.form['product_color']
            P_P = request.form['product_price']
            
            def genSerial():
                #generate serial number only numbers                
                return "".join([random.choice('0123456789') for _ in range(5)])
                
                
            SNR = genSerial()
            P_S = SNR
            
            with sqlite3.connect("data.db") as con:
                cursor = con.cursor()
                cursor.execute("insert into Products (P_Name , P_Category , P_Color , P_Price , P_Serial) \
                                values (?,?,?,?,?)" , (P_N,P_C,P_Co,P_P,P_S))
                
                con.commit()
                app.commit()
                
                msg = "Done"
        except:
            con.rollback()
            msg = "Error" 
            
        finally:
            # connect to data base 
            app = sqlite3.connect('data.db')
                
            # Create a Cursor object
            cursor = app.cursor()
                
            cursor.execute("select *from Products")
            # Save the results so we can use them later
            Products = cursor.fetchall() 
            con.close()
            return render_template('CRUD.html' , Products=Products , msg=msg)



@CRUD_app.route('/delete/<int:D_PS>' , methods=['POST', 'GET'])
def delete(D_PS):
    if True:
        try:
            # D_PS = request.form['product_serial']
            
            with sqlite3.connect("data.db") as con:
                cursor = con.cursor()                                
                
                # cursor.execute(f"delete from users where user_id={select_row}")
                msg = "done" 
                cursor.execute(f"DELETE FROM Products WHERE P_Serial = {D_PS}")
                con.commit()
                app.commit()
                
                msg = "Done"
        except:
            con.rollback()
            msg = "Error" 
            
        finally:
            # connect to data base 
            app = sqlite3.connect('data.db')
                
            # Create a Cursor object
            cursor = app.cursor()
                
            cursor.execute("select *from Products")
            # Save the results so we can use them later
            Products = cursor.fetchall() 
            con.close()
            return render_template('CRUD.html' , Products=Products , msg=msg)

@CRUD_app.route('/update' , methods=['POST', 'GET'])



def update():    
     if request.method == 'POST':
        try:
            NP_N = request.form['product_name']
            NP_C = request.form['product_category']
            NP_Co = request.form['product_color']
            NP_P = request.form['product_price']
        
            # Optinal if iser need to update serial number
            NP_S = request.form['new_product_serial']
            
            # to select which raw will update
            P_S = request.form['product_serial']
            
            with sqlite3.connect("data.db") as con:
                cursor = con.cursor()
                cursor.execute(f"update Products set P_Name = '{NP_N}' where P_Serial = {P_S}")
                cursor.execute(f"update Products set P_Category = '{NP_C}' where P_Serial = {P_S}")
                cursor.execute(f"update Products set P_Color = '{NP_Co}' where P_Serial = {P_S}")
                cursor.execute(f"update Products set P_Price = '{NP_P}' where P_Serial = {P_S}")
                
                
                cursor.execute(f"update Products set P_Serial = '{NP_S}' where P_Serial = {P_S}")
                
                
                con.commit()
                app.commit()
                
                msg = "Done"
        except:
            con.rollback()
            msg = "Error" 
            
        finally:
            # connect to data base 
            app = sqlite3.connect('data.db')
                
            # Create a Cursor object
            cursor = app.cursor()
                
            cursor.execute("select *from Products")
            # Save the results so we can use them later
            Products = cursor.fetchall() 
            con.close()
            return render_template('CRUD.html' , Products=Products , msg=msg)





if __name__ == '__main__':
    CRUD_app.run(debug = True)
    



