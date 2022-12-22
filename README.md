# cliff.ai Take Home Assignment

# STEPS I FOLLOWED TO SOLVE THE ASSIGNMENT :

- As ususal I started scraping the given website using CS tags and XPATH as I never came across a dynamic website to scrap and didn't know much about how to scrap it.
- After I learned it's a dynamic website I read and watched many youtube videos that can help me to get started with scraping dynamic website.
- I decided to go with **XHR_request** that are sent to server to load website dynamically. with the help of inspect feature of browser i manage to pin point the XHR         request required to get the categories of product.
- Everything in the project was new to me so I decided to write and test my code as granular(line by line) as possible using Jupyter in **test.ipynp**
- To Scrap category from the response , First I parsed it into a Json with JSON module of python.
- I write down all the elements and code to access the element that could be helpful for me and was necessary to proceed further with the scraping.
- After scraping the list of category and necessary element of categories , I started to scrap the products of each category by generating the XHR request for each           category's product pages. I found the XHR request pattern for it from inspect.
- Again I wrote all the code to scrap the product and all the necessary fields of product and code to extract them from their XHR request's response in                         **Product_scrap_test.ipynb** to test and debug it before i write in my spider.
- After all the testing and debugging I wrote the code in form of functions in my scrapy spider , I learnt how scrapy works and built my pipeline accordingly to load the    product data in my mongodb server.I already knew about pymongo and how to connect with the cluster so that was easy for me.
- For **Analytical** **Part** of the project I revised and also learnt new way to query mongodb database from websites,mongodb community and youtube videos and test        every query for a single collection before writing it for the whole database

Thank you for your time and patience!

# File and Folder Structure

- Leclerc folder is main project folder with analytical queries and along with screenshot folder which contain scrrenshot of terminal with request and response and I       also added the screenshot of my cloud mongo db cluster images containing the database and all its collection.
- test.ipynb and product_scrap_test.ipynb file consist of all the code i tried and tested before writing them into my spider.
- For the Assignment ,I followed the default srapy's project structure.
- All scrapy-related code is placed directly in project folder leclercProducts and subdirectory with the same name (leclercProducts).
- The spider created for crawling the web pages is in the spider folder with name leclerc_spider.py.
- pipeline.py and settings.py file is edited corrospond to the leclerc_spider.py
