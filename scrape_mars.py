
# coding: utf-8

# In[2]:


# Import dependencies
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from splinter import Browser


# In[3]:


#!which chromedriver


# In[4]:


# Initialize Chromedriver 
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless= False)


# In[ ]:


########################### NASA MARS NEWS ###########################


# In[ ]:


# URL for scrape
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[ ]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[ ]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')
type(soup)


# In[ ]:


# Examine the results, then determine element that contains news title and news paragraph text
print(soup.prettify())


# In[ ]:


# Find the content_title class, which contains the titles of the news articles; returns a list
content_title = soup.find(class_="content_title")
print(content_title)


# In[ ]:


news_title = content_title.find("a").get_text()
print(news_title)


# In[ ]:


news_p = soup.find(class_="rollover_description_inner").get_text()
print(news_p)


# In[ ]:


########################### JPL MARS SPACE IMAGES - FEATURED IMAGE ###########################
# URL for scrape
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[ ]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[ ]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')
type(soup)


# In[ ]:


# Examine the results, then determine element that contains images and url
print(soup.prettify())


# In[ ]:


# Find image url to full size
carousel_items = soup.find(class_="carousel_items")
print(carousel_items)
# Save a complete url string for this image


# In[ ]:


#for link in carousel_items:
    #print(carousel_items.get('data-fancybox-href'))


# In[ ]:


########################### MARS WEATHER ###########################
# Visit mars weather twitter account and scrape the latest mars weather tweet from the page
url = "http://twitter.com/marswxreport?lang=en"
# Save tweet text for the report as variable
browser.visit(url)


# In[ ]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[ ]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')
type(soup)


# In[ ]:


# Examine the results, then determine element that contains mars weather 
print(soup.prettify())


# In[ ]:


mars_weather = soup.find(class_="js-tweet-text-container").get_text()
print(mars_weather)


# In[ ]:


########################### MARS FACTS ###########################
# Visit the mars facts webpage, use pandas to scrape the table containing facts about the planet including diameter, mass, etc
facts_url = "http://space-facts.com/mars"

tables = pd.read_html(facts_url)
tables


# In[ ]:


# Convert list to dataframe
facts_df = tables[0]

# Set first column to index
facts_df.set_index(0, inplace=True)
facts_df.head(8)


# In[ ]:


# Use pandas to convert the data to a HTML table string
facts_table_html = facts_df.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None)
print(facts_table_html)


# In[ ]:


########################### MARS HEMISPHERES ###########################


# In[5]:


# Visit the USGS Astrogeology site to obtain hi-res images for each of Mars' hemispheres
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
html = browser.html


# In[6]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[7]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')
type(soup)


# In[8]:


# Examine the results, then determine element that contains images
print(soup.prettify())


# In[13]:


# Find all image tags
images = soup.find_all("img")
#print(images)
type(images)


# In[12]:


# List comprehension to find only the hemispheres images
img_url = [img["src"] for img in soup.find_all("img") if "Hemisphere" in img["alt"]]
print(img_url)


# In[ ]:


#soup.img.attrs


# In[ ]:


# Save image url string and the hemisphere title containing the hemisphere name

# Use a python dictionary to store the data using keys img_url and hemisphere title
def hemisphere_dict(img_url, title):
    return {
        "": img_url,
        "": title
    }


# Append the dictionary with the image url string and the hemisphere title to a list; the list will contain one dictionary for each hemisphere

# Store image data in array 
 

