
# coding: utf-8

# In[13]:


# Import dependencies
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from splinter import Browser


# In[14]:


#!which chromedriver


# In[15]:


# Initialize Chromedriver 
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless= False)


# In[16]:


########################### NASA MARS NEWS ###########################


# In[17]:


# URL for scrape
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[18]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[19]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')
type(soup)


# In[20]:


# Examine the results, then determine element that contains news title and news paragraph text
print(soup.prettify())


# In[21]:


# Find the content_title class, which contains the titles of the news articles
content_title = soup.find(class_="content_title")
print(content_title)


# In[22]:


news_title = content_title.find("a").get_text()
print(news_title)


# In[23]:


news_p = soup.find(class_="rollover_description_inner").get_text()
print(news_p)


# In[24]:


########################### JPL MARS SPACE IMAGES - FEATURED IMAGE ###########################
# URL for scrape
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[25]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[26]:


# Design an XPATH selector to grab the full seize featured image
# xpath = '//*[@id="fancybox-lock"]/div/div[1]/img'


# In[27]:


# Use splinter to bring up the full resolution image
# results = browser.find_by_xpath(xpath)
# print(results)


# In[28]:


# img = results[0]
# img.click()


# In[29]:


# Create BeautifulSoup object; parse to find the full resolution image of mars
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
print(soup)


# In[30]:


a_href = soup.select('a[href]')
print(a_href)


# In[31]:


a = soup.find_all('a')
#print(a)
for link in soup.find_all('a'):
    print(link.get('data-fancybox-href')) 


# In[32]:


# This is a cheat because I was unable to parse down to only the jpg I wanted so I am just looking at it from the code above
featured_image_url = "https:www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA07137_ip.jpg"


# In[35]:


########################### MARS WEATHER ###########################
# Visit mars weather twitter account and scrape the latest mars weather tweet from the page
url = "http://twitter.com/marswxreport?lang=en"
# Save tweet text for the report as variable
browser.visit(url)


# In[36]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[37]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')
type(soup)


# In[38]:


# Examine the results, then determine element that contains mars weather 
print(soup.prettify())


# In[39]:


mars_weather = soup.find(class_="js-tweet-text-container").get_text()
print(mars_weather)


# In[41]:


########################### MARS FACTS ###########################
# Visit the mars facts webpage, use pandas to scrape the table containing facts about the planet including diameter, mass, etc
facts_url = "http://space-facts.com/mars"

tables = pd.read_html(facts_url)
tables


# In[42]:


# Convert list to dataframe
facts_df = tables[0]

# Set first column to index
facts_df.set_index(0, inplace=True)
facts_df.head(8)


# In[43]:


# Use pandas to convert the data to a HTML table string
facts_table_html = facts_df.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None)
print(facts_table_html)


# In[ ]:


########################### MARS HEMISPHERES ###########################


# In[44]:


# Visit the USGS Astrogeology site to obtain hi-res images for each of Mars' hemispheres
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
html = browser.html


# In[45]:


# Retrieve page with the requests module
response = requests.get(url)
print(response)


# In[46]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')
type(soup)


# In[47]:


# Examine the results, then determine element that contains images
print(soup.prettify())


# In[48]:


# Find all image tags
images = soup.find_all("img")
print(images)
#type(images)


# In[49]:


# List comprehension to find only the hemispheres images
img_url = [img["src"] for img in soup.find_all("img") if "Hemisphere" in img["alt"]]
print(img_url)


# In[50]:


# List comprehension to find only the hemisphere names
hemisphere_title = [img["alt"] for img in soup.find_all("img") if "Hemisphere" in img["alt"]]
print(hemisphere_title)


# In[53]:


# Use a python dictionary to store the data using keys img_url and hemisphere title
hemisphere_dictionary = dict(zip(img_url, hemisphere_title))
print(hemisphere_dictionary)

