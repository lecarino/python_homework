from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import json

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
try:
    driver.get(url)
    time.sleep(5)
    '''
Find all the li elements in that page for the search list results.  You use the class values you stored in task 2 step 3. 
Also use the tag name when you do the find, to make sure you get the right elements.
Within your program, create an empty list called results.  You are going to add dict values to this list, one for each search result.
 '''
    results = []
    search_items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")
    #print(f"There are {len(search_items)} books on the page.\n")

    for item in search_items:
        #TITLE 
        try:
            title_element = item.find_element(By.CSS_SELECTOR, "span.title-content")
            title = title_element.text
            #print(f"Title: {title}")
        except:
            title = "Title Not Found"
        
        #AUTHOR/S
        try:
            author_element = item.find_elements(By.CSS_SELECTOR, "a.author-link")
            #if multiple authors:
            author_names= [author.text for author in author_element]
            authors="; ".join(author_names)
            #print(f'authors: {authors}')
        except:
            authors = "No Authors Found"

        #FORMAT/ YEAR
        try:
            format_element = item.find_element(By.CSS_SELECTOR, "span.display-info-primary")
            format_year = format_element.text
            #print(f"Format/Year: {format_year}")
        except:
            format_year= 'Format/Year Not Found'

        #DICT:
        book_dict = {
            "Title": title,
            "Authors": authors,
            "Format-Year": format_year
        }
        results.append(book_dict)

except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()

#print(results)
books_df = pd.DataFrame(results)
# print(books_df)

# Task 4: Write out the Data
# Write the DataFrame to a file called get_books.csv, within the assignment8 folder.  Examine the file to see if it looks right.
books_df.to_csv("get_books.csv", index=False)

# Write the results list out to a file called get_books.json, also within the assignment8 folder.  You should write it out in JSON format.  Examine the file to see if it looks right.
with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)



