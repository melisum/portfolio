from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas


list_of_links=[]
cake_names=[]
ratings=[]

cake = input("What do you want to search for? :\n")
recipes_url = f"https://www.allrecipes.com/search?q={cake}"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

driver.get(recipes_url)
time.sleep(3)


action=driver.find_element(By.ID, value='onetrust-reject-all-handler')
action.click()

result=driver.find_elements(By.CLASS_NAME, value="mntl-card-list-items")
for r in result:
    link=r.get_property("href")
    list_of_links.append(link)

result=driver.find_elements(By.CLASS_NAME, value="card__title-text ")
for r in result:
    cake=r.text
    cake_names.append(cake)

result=driver.find_elements(By.CLASS_NAME, value="rating-count-number")
for r in result:
    rating=r.text
    ratings.append(rating)

max=max(ratings)
position=ratings.index(max)

print(f"{len(list_of_links)} results were extracted")
print(f"{cake_names[position]} has the most ratings")
print(f"You can check it out on this link: {list_of_links[position]}")

data_dict = {
    cake: cake_names,
    "ratings": ratings,
    "links": list_of_links
}

data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("cakes.csv")

