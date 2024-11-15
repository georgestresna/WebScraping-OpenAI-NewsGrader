from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def getData():

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("https://www.forexfactory.com/news")

    latestResults = []
    hotestResults = []

    articles1 = driver.find_elements(By.CSS_SELECTOR, '#flexBox_flex_news_newsLeft1 > ul > li')
    for article in articles1:
        x = article.find_element(By.CSS_SELECTOR, '[href]').get_attribute("href")
        latestResults.append(x)

    # element = driver.find_element(By.CSS_SELECTOR, '#flexBox_flex_news_newsRight1 > div.foot [href]')
    # element.send_keys(Keys.RETURN)
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # driver.execute_script("arguments[0].click();", element)
    # time.sleep(10)

    articles2 = driver.find_elements(By.CSS_SELECTOR, '#flexBox_flex_news_newsRight1 > ul > li')
    for article in articles2:
        x = article.find_element(By.CSS_SELECTOR, '[href]').get_attribute("href")
        hotestResults.append(x)
    
    results = [latestResults, hotestResults]
    
    driver.close()

    for section_index, section in enumerate(results):
        for article_index, article_url in enumerate(section):

            article_site = webdriver.Chrome()
            article_site.implicitly_wait(2)
            article_site.get(article_url)

            try:
                text_article = article_site.find_element(By.CSS_SELECTOR, '#newsStory > div > div.pagearrange__layout-column.pagearrange__layout-column--twothird > div:nth-child(1) > div.flexBox.noflex.news__story > ul > li > div > p.news__copy')
                text = article_site.execute_script("return arguments[0].firstChild.textContent;", text_article)

                results[section_index][article_index] = text
            except:
                results[section_index][article_index] = ""
                
            article_site.close()

    return results
