from requests_html import HTMLSession
from matplotlib import pyplot as plt

url = 'https://www.flashscore.com/player/kaminski-jakub/hbhnybaa/'
session = HTMLSession()
res = session.get(url)
res.html.render()
assistList = list() 
goalList = list()
timeList = list()

# if driver.find_element_by_class_name('profileTable__row profileTable__row--last show-more-last-matches'):  
#     print("dasd")
#     next_btn = driver.find_element_by_class_name('profileTable__row profileTable__row--last show-more-last-matches')
#     next_btn.click()

for div in res.html.find('div.lm__row.lm__row--twoLine'):
    value = div.find('div.lm__iconText--assist')
    value0 = div.find('div.lm__iconText--grey')
    if value:
        assistList.append(int(value[0].text))
    elif value0:
         assistList.append(int(value0[0].text))
    # else:
        # print("Did not play")

for div in res.html.find('div.lm__row.lm__row--twoLine'):
    value = div.find('div.lm__iconText--goal')
    value0 = div.find('div.lm__iconText--grey')
    if value:
        goalList.append(int(value[0].text))
    elif value0:
        goalList.append(int(value0[0].text))
    # else:
        # print("Did not play")

for div in res.html.find('div.lm__row.lm__row--twoLine'):
    value = div.find('div.lm__iconText--minutes-played')
    if value:
        if value[0].text != '?':
            timeList.append(int(value[0].text.replace("'", "")))
        else:
            timeList.append(0)
    # else:
        # print("Did not play")

#Output Charts:
#Goals
plt.subplot(3,1,1)
plt.plot(goalList , 'o-r', ms = 9)
plt.xlabel("Matches ago")
plt.ylabel("Goals")
# plt.grid(axis = 'y')
#Assists
plt.subplot(3,1,2)
plt.plot(assistList , 'o-y', ms = 9)
plt.xlabel("Matches ago")
plt.ylabel("Assists")
# plt.grid(axis = 'y')
#Minutes
plt.subplot(3,1,3)
plt.plot(timeList , 'o-g', ms = 9)
plt.xlabel("Matches ago")
plt.ylabel("Minutes")
plt.grid(axis = 'y')
#End
plt.suptitle("Statistics of player")
plt.show()

