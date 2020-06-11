#import dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': 'C:/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    # NASA Mars News
    #using splinter to make path to NASA website
    nasa_url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(nasa_url)

    #inspecting html using beautiful soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    print(soup.prettify())

    #navigating to the title
    title = soup.select_one('ul.item_list li.slide')
    print(title.prettify())

    #pulling and saving latest article title
    contenttitle = title.find('div', class_='content_title')
    news_title=contenttitle.get_text()
    news_title

    #pulling and saving latest article description
    paragraph = title.find('div',class_='article_teaser_body')
    news_p=paragraph.get_text()
    news_p


    # JPL Mars Space Images - Featured Image
    #using splinter to make path to Mars Space Images website
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    #inspecting html using beautiful soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    print(soup.prettify())

    #navigating to the background image and getting rid of some text
    background_image_route  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    print(background_image_route)

    #need main url to add to the front of the route
    main_url = "https://www.jpl.nasa.gov"
    print(main_url)

    #Combine website url with scrapped route
    featured_image_url = main_url + background_image_route

    # Display full link to featured image
    featured_image_url


    # Mars Weather
    #using splinter to make path to Mars Weather Twitter account
    mars_twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_twitter_url)

    #inspecting html using beautiful soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    print(soup.prettify())

    # Find latest element that contain tweets
    mars_weather = soup.find('div', attrs = {"lang" : "en"})
    latest_tweet = mars_weather.get_text()
    latest_tweet


    # Mars Facts
    #using splinter to make path to Mars Facts account
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    #using pandas to to scrape the table containing facts about the planets including Diameter, Mass, etc
    table = pd.read_html(facts_url)
    table

    #indexing to get the Mars information
    mars_facts = table[1]
    mars_facts

    #only keep Mars info, rename columns, and set index
    mars_facts.rename(columns={"Mars - Earth Comparison":"Description","Mars":"Value"},inplace=True)
    mars_facts = mars_facts[["Description","Value"]]
    mars_facts

    # using pandas to convert the data to a HTML table string
    mars_facts.to_html('table.html',index=False)


    # Mars Hemispheres
    #using splinter to make path to USGS Astrogeology site
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)

    #inspecting html using beautiful soup
    soup = BeautifulSoup(browser.html, 'html.parser')
    print(soup.prettify())

    # Retrieve all elements that contain image information
    results = soup.find("div", class_ = "result-list" )
    print(results.prettify())

    hemispheres = results.find_all("div", class_="item")
    print(hemispheres)

    # empty list to append dictionaries of titles & links to images
    hemisphere_image_urls = []

    # iterate through each image and collect titles & links
    for hemisphere in hemispheres:
        #grab title
        title = hemisphere.find("h3").text
        #clean title
        title = title.replace("Enhanced", "")
        #grab image link
        image_route = hemisphere.find("a", class_='itemLink product-item')["href"]
        image_link = "https://astrogeology.usgs.gov/" + image_route
        #visit site using splinter to scrape
        browser.visit(image_link)
        #parse using beautiful soup
        soup = BeautifulSoup(browser.html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})

    print(hemisphere_image_urls)

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": latest_tweet,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

if __name__ == '__main__':
    scrape()