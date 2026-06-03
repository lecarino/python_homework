# ---- TASK 5: READ INTO A DATAFRAME ----

import sqlite3
import pandas as pd

# 1. The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, and price from a JOIN of the line_items table and the product table
#Hint: Your ON statement would be ON line_items.product_id = products.product_id.
sql_query = """
    SELECT 
        line_items.line_item_id, 
        line_items.quantity, 
        line_items.product_id, 
        products.product_name, 
        products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
"""
try:
    with sqlite3.connect("../db/lesson.db") as conn:
        print("Successfully connected to db ")
        df = pd.read_sql_query(sql_query, conn)

        '''Print the first 5 lines of the resulting DataFrame. 
        Run the program to make sure this much works.'''

        print("\n Data (First 5 Rows)")
        print(df.head())
    
        
        '''Add a column to the DataFrame called "total". 
        This is the quantity times the price. 
        (df['total'] = df['quantity'] * df['price'].)'''

        print("\nAdding 'Total' Column")
        df['total'] = df['quantity'] * df['price']
        print(df.head())


        '''Add groupby() code to group by the product_id. 
        Use an agg() method that specifies 'count' for the line_item_id column, 
        'sum' for the total column, 
        and 'first' for the 'product_name'. '''

        print("\nGrouping Data")
        summary_df = df.groupby('product_id').agg({
            'line_item_id': 'count', # Count how many orders
            'total': 'sum',          # Add up all the money
            'product_name': 'first'  # Keep the name of the product
        })
        print(summary_df.head())


        '''Sort the DataFrame by the product_name column.'''

        print('\nSorting Data')
        summary_df = summary_df.sort_values(by='product_name')
        print(summary_df.head())
        
        '''Add code to write this DataFrame to a file order_summary.csv, which should be written in the assignment9 directory. 
        Verify that this file is correct.'''

        print("\n Writing To CSV")
        summary_df.to_csv("order_summary.csv")
        print("\n Success to writing to csv")
        
except Exception as e:
    print(f"An error occurred: {e}")