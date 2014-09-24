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

def update_product(data,db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "update Product set Name=?, Price=? where ProductID=?"
        cursor.execute(sql,data)
        db.commit()
        
    

if __name__ == "__main__":

    
    db_name = "coffee_shop.db"

    sql = """CREATE TABLE Product(
    ProductID integer,
    Name text,
    Price real,
    Primary Key(ProductID));"""

    create_table(db_name,"Product",sql)
    
    values = ("Espresso",1.5)
    insert_data(values,db_name)
    
    values = ("Latte Express", 1.75)
    insert_data(values,db_name)

    values = ("Standard Coffee", 1.00)
    insert_data(values, db_name)
    
    newValues = ("Latte",2.45,1)
    update_product(newValues,db_name)
    products = select_all_products(db_name)
    print(products)
    
