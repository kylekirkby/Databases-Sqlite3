import sqlite3


def create_table(db_name,table_name,sql):

    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        #expects a tuple - need comma after value in tuple
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? y/n ?: ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
            else:
                print("The existing table was kept.")
        else:
            keep_table = False

        if not keep_table:
            cursor.execute(sql)
            db.commit()
            
def select_all_products(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        return products
            
def insert_data(values,db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "insert into Product(Name,Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

def delete_product(data,db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "delete from Product where Name=?"
        cursor.execute(sql,data)
        db.commit()

def update_product(data,db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "update Product set Name=?, Price=? where ProductID=?"
        cursor.execute(sql,data)
        db.commit()

        
def select_product(db_name,productID):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select * from Product WHERE ProductID=?",(productID,))
        product = cursor.fetchone()
        return product


def menu():
    print("Product Table Menu")
    print()
    print("1. (Re)Create Product Table")
    print("2. Add New Product")
    print("3. Edit Existing Product")
    print("4. Delete Existing Product")
    print("5. Search for Products")
    print("0. Exit")
    print()

def addProduct(db_name):
    accepted = False
    while accepted == False:
        try:
            productName = input("Enter the product name (enter 'q' to stop): ")
            if productName == 'q':
                accepted = True
                print("tesrt")
            else:
                productPrice = float(input("Enter the product price (float): "))
                if productName != "":
                    with sqlite3.connect(db_name) as db:
                        cursor = db.cursor()
                        values = (productName, productPrice)
                        sql = "insert into Product(Name,Price) values (?,?)"
                        cursor.execute(sql,values)
                        db.commit()
                        print("Product has been added successfully!")
        

                
        except ValueError:
            print("Please enter a string for the product name and a float for the price!")
        
def editProduct(db_name):
    accepted = False
    while accepted == False:
        try:
            productID = input("Enter the product id to edit (enter 'q' to stop): ")
            if productID == 'q':
                accepted = True
                print("tesrt")
            else:
                productID = int(productID)
                productPrice = float(input("Enter the product price (float): "))
                if productName != "":
                    with sqlite3.connect(db_name) as db:
                        cursor = db.cursor()
                        values = (productName, productPrice)
                        sql = ""
                        cursor.execute(sql,values)
                        db.commit()
                        print("Product has been added successfully!")
        

                
        except ValueError:
            print("Please enter a string for the product name and a float for the price!")
        

    
def managementMenu():
    db_name = "coffee_shop.db"
    
    sql = """CREATE TABLE Product(
    ProductID integer,
    Name text,
    Price real,
    Primary Key(ProductID));"""

    
    exitMenu = False

    while exitMenu == False:

        menu()
        try:

            choice = int(input("Enter Option: "))

            if choice == 1:
                create_table(db_name,"Product",sql)
            elif choice == 2:
                addProduct(db_name)
            elif choice == 3:
                editProduct(db_name)
            elif choice == 4:
                deleteProduct(db_name)
            elif choice == 5:
                searchProducts(db_name)
            elif choice == 0:
                exitMenu = True
            else:
                print("Please enter a valid choice!!")
        except ValueError:
            
            print("Please enter an integer!")
    

if __name__ == "__main__":

    managementMenu()
    
##    db_name = "coffee_shop.db"
##
##    sql = """CREATE TABLE Product(
##    ProductID integer,
##    Name text,
##    Price real,
##    Primary Key(ProductID));"""
##
##    create_table(db_name,"Product",sql)
##    
##    values = ("Espresso",1.5)
##    insert_data(values,db_name)
##    
##    values = ("Latte Express", 1.75)
##    insert_data(values,db_name)
##
##    values = ("Standard Coffee", 1.00)
##    insert_data(values, db_name)
##    
##    newValues = ("Latte",2.45,1)
##    update_product(newValues,db_name)
##
##    data = ("Espresso",)
##    delete_product(data,db_name)
##
##
##    products = select_all_products(db_name)
##    print(products)
##
##    product = select_product(db_name,1)
##    print(product)
    
    
