# web-scraping-challenge

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

##
## Part 1 - Scraping
Websites Scraped:
* [NASA Mars News Site](https://mars.nasa.gov/news/)
* [NASA Featured Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
* [Mars Weather Twitter](https://twitter.com/marswxreport?lang=en)
* [Mars Facts Webpage](https://space-facts.com/mars/)
* [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

##
## Part 2 - MongoDB and Flask Application

I used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Flask Routes:
* `/scrape` 
	* imports `scrape_mars.py` script and calls the `scrape` function.
  	* Stored the return value in Mongo as a Python dictionary.
* `/` 
	* Queries the Mongo database and passes the mars data into an HTML template to display the data

HTML:
* `index.html`
	* takes the mars data dictionary and displays all of the data in the appropriate HTML elements.

<img src="https://github.com/kelseyoros/web-scraping-challenge/blob/master/images/final_app.png" width="800">