import sqlite3
conn = sqlite3.connect('commerce.db')

# Create cursor
c = conn.cursor()
'''
# Create table
c.execute("""CREATE TABLE customers(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		product_type varchar(255) NOT Null,
		price REAL NOT Null,
        user_name varchar(255),
		phone_number int ,
		status VARCHAR(25),
		description text,
		photo1 text,
		photo2 text,
		photo3 text
  
	)""")
c.execute("""CREATE TABLE customer_supply(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		product_type_supply varchar(255) NOT Null,
		max_price REAL NOT Null,
        min_price REAL NOT Null,
		status_supply VARCHAR(25),
		description_supply text,
		user_name text,
		date DATE
	)""")
'''
# Create Function to Delete A Record
def insert(product_type,price,user_name,phone_number,status,description,photo1,photo2,photo3):
	# Create a database or connect to one
	conn = sqlite3.connect('commerce.db')
	# Create cursor
	c = conn.cursor()
	c.execute("INSERT INTO customers(product_type, price, user_name, phone_number, status, description,photo1,photo2,photo3) values(?,?,?,?,?,?,?,?,?)",(product_type,price,user_name,phone_number,status,description,photo1,photo2,photo3))
	#Commit Changes
	conn.commit()
	# Close Connection 
	conn.close()
 
def get_last_row_id():
    # Create a database or connect to one
    conn = sqlite3.connect('commerce.db')
    # Create cursor
    c = conn.cursor()
    # Execute a query to get the last row ID
    c.execute("SELECT MAX(ID) FROM customers")
    # Fetch the result
    last_row_id = c.fetchone()[0]
    # Close Connection 
    conn.close()
    # Return the last row ID
    return last_row_id

# Create Query Function
def insert_supply(product_type_supply,max_price,min_price,status_supply,description_supply,user_name,date):
	# Create a database or connect to one
	conn = sqlite3.connect('commerce.db')
	# Create cursor
	c = conn.cursor()
	c.execute("INSERT INTO customer_supply (product_type_supply,max_price,min_price,status_supply,description_supply,user_name,date) values(?,?,?,?,?,?,?)",(product_type_supply,max_price,min_price,status_supply,description_supply,user_name,date))
	#Commit Changes
	conn.commit()
	# Close Connection 
	conn.close()
 
def query(product_type_supply, max_price, min_price, status_supply, description_supply):
    # Create a database or connect to one
    conn = sqlite3.connect('commerce.db')
    # Create cursor
    c = conn.cursor()
    
    # Use parameter substitution in the query
    c.execute("""
        SELECT customers.* 
        FROM customers
        WHERE (customers.product_type LIKE '%' || ? || '%' OR customers.description LIKE '%' || ? || '%') 
        AND (customers.price BETWEEN ? AND (? + 5000)) 
        ORDER BY customers.price LIMIT 8
    """, (product_type_supply, description_supply, min_price, max_price))  # Provide the variables as a tuple

    # Fetch the results
    results = c.fetchall()
    
    return results
