''' Automation tester python Task '''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver =  webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(2)

# --------------------------.Go to https:https:https://www.goibibo.com/hotels/------------

driver.get("https://www.goibibo.com/hotels/")
time.sleep(2)

# ---------------------------Select "India" Radio button.---------------------------------

radio_buttons = driver.find_elements_by_name("CountryType")
clicked_radio_button_india = radio_buttons[0].click()
time.sleep(2)
print("select india successfully")

# ----------------------------3.Select any city from "Where" dropdown.--------------------------


where = driver.find_element_by_id("downshift-1-input").click()

ideal_city = driver.find_element_by_id('downshift-1-input').send_keys("G")
time.sleep(2)

cities_where = driver.find_elements_by_xpath("//li[contains(@class,'HomePageAutosuggeststyles__SearchListItem-sc-1v6s32j-2 cFiIpU')]")

for city in cities_where:
    if "Gaya Airport ( GAY ), Gaya" in city.text:
        time.sleep(1)
        city.click()
        print("city clicked")
        break
time.sleep(2)
guest_and_rooms_click = driver.find_element_by_xpath("//span[contains(text(),'Guests & Rooms')]").click()

# ------------bottom box------------------
tag = driver.find_elements_by_xpath("//div[contains(@class,'dwebCommonstyles__CenteredSpaceWrap-sc-112ty3f-0 PaxWidgetstyles__ContentActionWrapperDiv-sc-gv3w6r-5 eHRHNU lhNBSu')]")
rooms = tag[0]
adults = tag[1]
chidrens = tag[2]
# ------------signs - 1 +
rooms_signs = rooms.find_elements_by_xpath("//span[contains(@class,'PaxWidgetstyles__ContentActionIconWrapperSpan-sc-gv3w6r-8 dxKRvV')]")
adults_signs = adults.find_elements_by_xpath("//span[contains(@class,'PaxWidgetstyles__ContentActionIconWrapperSpan-sc-gv3w6r-8 dxKRvV')]")
chidrens_signs = chidrens.find_elements_by_xpath("//span[contains(@class,'PaxWidgetstyles__ContentActionIconWrapperSpan-sc-gv3w6r-8 dxKRvV')]")

# --------------select 2 rooms--------------

time.sleep(2)
rooms_signs[1].click()
time.sleep(2)

# ------------------select 3 audults ---------

time.sleep(2)
for i in range (0,1):
    time.sleep(2)
    adults_signs[3].click()

# ----------------select 2 child---------
 
time.sleep(2)
for i in range(0,2):
    time.sleep(2)
    chidrens_signs[5].click()
    time.sleep(2)
    
# ---------------------8.Check 2 "Child" dropdown is enabled or not-------------

children_dropdown = driver.find_elements_by_xpath("//div[contains(@class,'dwebCommonstyles__CenteredSpaceWrap-sc-112ty3f-0 PaxWidgetstyles__ContentActionWrapperDiv-sc-gv3w6r-5 PaxWidgetstyles__ContentActionDropdownWrapper-sc-gv3w6r-6 eHRHNU lhNBSu kfVCVI')]")
first_child= children_dropdown[0]
dropdown_arrow = first_child.find_elements_by_xpath("//span[contains(@class,'PaxWidgetstyles__ContentActionIconWrapperSpan-sc-gv3w6r-8 dxKRvV')]")
time.sleep(2)

# ----------------------9.Select Age from childs dropdown --------------------------

dropdown_arrow[6].click()
list_of_no = first_child.find_element_by_xpath("//ul[contains(@class,'PaxWidgetstyles__ChildDropdownWrap-sc-gv3w6r-9 cuOfFa')]")
age = list_of_no.find_element_by_xpath("//li[contains(text(),'3')]")
time.sleep(2)
age.click()
time.sleep(2)
print("age selected successfully")
second_child = children_dropdown[1]
dropdown_arrow_for_second_child = first_child.find_elements_by_xpath("//span[contains(@class,'PaxWidgetstyles__ContentActionIconWrapperSpan-sc-gv3w6r-8 dxKRvV')]")
time.sleep(2)
dropdown_arrow_for_second_child[7].click()
list_of_no = first_child.find_element_by_xpath("//ul[contains(@class,'PaxWidgetstyles__ChildDropdownWrap-sc-gv3w6r-9 cuOfFa')]")
age = list_of_no.find_element_by_xpath("//li[contains(text(),'5')]")
time.sleep(2)
age.click()
time.sleep(2)
print("age selected successfully")

# -----------------10.Click on 'Done' Button.--------------------

Done = driver.find_element_by_xpath("//button[contains(@class,'dwebCommonstyles__ButtonBase-sc-112ty3f-10 PaxWidgetstyles__ButtonWrapper-sc-gv3w6r-11 KETBj dIHxWr')]")
time.sleep(2)
Done.click()
time.sleep(2)

# ----------------11.Click on 'Serch Hotel' button.-----------------

search_hotels = driver.find_element_by_xpath("//button[contains(@class,'dwebCommonstyles__ButtonBase-sc-112ty3f-10 SearchBlockUIstyles__SearchButtonAutoSuggest-sc-fity7j-13 KETBj dMpVqc')]")
search_hotels.click()
print("hotels searching")