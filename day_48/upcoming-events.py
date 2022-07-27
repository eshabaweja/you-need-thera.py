# {0:{'time': x, 'event':y},}
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.python.org/')

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {i:{
    'time':event_times[i].text,
    'name':event_names[i].text}
    for i in range(len(event_times))}
# for event in upcoming_events:
#     events[str(i):{
#       'time': event.find_element(By.TAG_NAME,"time").text ,
#       'name': event.find_element(By.TAG_NAME,"a").text
#       }]
#     i+=1

driver.quit()

# print(event_names)
# print(event_times)
print(events)