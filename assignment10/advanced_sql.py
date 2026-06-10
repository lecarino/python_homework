import sqlite3



try:
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    ### --- TASK 1 START --- ###
    print("--- TASK 1: First 5 Orders Total Price ---")

    query = """
        SELECT orders.order_id, SUM(products.price * line_items.quantity)
        FROM orders
        JOIN line_items ON orders.order_id = line_items.order_id
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id
        LIMIT 5;
    """
    
    cursor.execute(query)
    results = cursor.fetchall()

    # print(results)

    for row in results:
        order_id = row[0]
        total_price = row[1]
        print(f"Order ID: {order_id} | Total Price: ${total_price:.2f}")

    ### --- TASK 1 END --- ###


    ### --- TASK 2: START --- ###
    print("--- TASK 2: Understanding Subqueries ---")

    #Use task 1 query as subquery for task 2

    query2 = '''
        SELECT customers.customer_name, AVG(sq.total_price) AS average_total_price
        FROM customers
        LEFT JOIN (
            SELECT orders.customer_id AS customer_id_b, SUM(products.price * line_items.quantity) AS total_price
            FROM orders
            JOIN line_items ON orders.order_id = line_items.order_id
            JOIN products ON line_items.product_id = products.product_id
            GROUP BY orders.order_id
        ) sq ON customers.customer_id = sq.customer_id_b
        GROUP BY customers.customer_id;
    '''
    cursor.execute(query2)
    results2 = cursor.fetchall()
    
    # print(results2)
    for row in results2:
        customer_name = row[0]
        avg_price = row[1]
        if avg_price:
            print(f"Customer Name: {customer_name} | Average Price: ${avg_price:.2f}")
        else:
            print(f"Customer Name: {customer_name} | Average Price: $0")

    # ### --- TASK 2: END --- ###


    ### --- TASK 3: START --- ###
    print("--- TASK 3: An Insert Transaction Based on Data ---")
    
    #SELECT: customer_id, product_id, employee_id
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]

    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    cheap_products = cursor.fetchall() # Returns a list of 5 tuples

    #TRANSACTION
    try:
        #create new order:
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date) 
            VALUES (?, ?, date('now')) 
            RETURNING order_id;
            """, (customer_id, employee_id))
        new_order_id = cursor.fetchone()[0]
        print(f"-> Successfully created Order #{new_order_id}")

        #5 cheapest products
        for product in cheap_products:
                prod_id = product[0]
                cursor.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity) 
                    VALUES (?, ?, 10);
                """, (new_order_id, prod_id))
        conn.commit()
        #Finished Transaction
        
        #check if success
        check_query = """
            SELECT line_items.line_item_id, line_items.quantity, products.product_name
            FROM line_items
            JOIN products ON line_items.product_id = products.product_id
            WHERE line_items.order_id = ?
        """
        cursor.execute(check_query, (new_order_id,))
        
        for row in cursor.fetchall():
            print(f"Line Item ID: {row[0]} | Quantity: {row[1]} | Product: {row[2]}")

    except Exception as e:
        conn.rollback()
        print("Error:",e)

    ### --- TASK 3: END --- ###

    ### --- TASK 4: START --- ###
    print("--- Task 4: Aggregation with HAVING ---")

    query4 = """
            SELECT employees.employee_id, employees.first_name, employees.last_name, COUNT(orders.order_id) AS order_count
            FROM employees
            JOIN orders ON employees.employee_id = orders.employee_id
            GROUP BY employees.employee_id
            HAVING COUNT(orders.order_id) > 5;
        """
        
    cursor.execute(query4)
    results4 = cursor.fetchall()
    
    for row in results4:
        emp_id = row[0]
        first_name = row[1]
        last_name = row[2]
        order_count = row[3]
        
        print(f"Employee ID: {emp_id} | Name: {first_name} {last_name} | Total Orders: {order_count}")

    ### --- TASK 4: END --- ###


except sqlite3.Error as e:
    print(f"Error: {e}")

conn.close()
print("DB closed")

