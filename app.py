from bs4 import BeautifulSoup
import requests

#########################################################################################################################
#LEETCODE


# Fetch the LeetCode contest page
leetcode_html = requests.get('https://leetcode.com/contest/').text
soup = BeautifulSoup(leetcode_html, "html.parser")

# Find the element containing the timer
leetcode_timer_element = soup.find('div' ,class_= 'flex items-center text-[14px] leading-[22px] text-label-2 dark:text-dark-label-2')

# Extract the timer text
leetcode_weekly_timer_text = leetcode_timer_element.text.strip()

print(f" leetcode_weekly_contest at : {leetcode_weekly_timer_text}")

#############################################################################################################
#CODEFORCES

codeforces_html = requests.get('https://codeforces.com/contests').text
soup_cf = BeautifulSoup(codeforces_html,"html.parser")

codeforces_timer_element = soup_cf.find('span' ,class_= "format-time" )
cf_timer_text = codeforces_timer_element.text.strip()

print(f"Codeforces contest at :{cf_timer_text}")

################################################################################################
# #CODECHEf
#
# codechef_html = requests.get('https://www.codechef.com/contests').text
# soup_cc = BeautifulSoup(codechef_html,"html.parser")
# print(soup_cc)
#
# codechef_timer_element = soup_cc.find('table' ,class_= "MuiTable-root jss13 _mui-table__container_ioa8k_417" )
#
# # cc_timer_text = codechef_timer_element.text.strip()
# #
# # print(f"Codeforces contest at :{cf_timer_text}")
###############################################################################################################
#GFG

#CODEFORCES

gfg_html = requests.get('https://www.geeksforgeeks.org/events?itm_source=geeksforgeeks&itm_medium=main_header&itm_campaign=contests').text
soup_gfg = BeautifulSoup(gfg_html,"html.parser")

gfg_timer_element = soup_gfg.find('div' ,class_= "five wide computer five wide large screen eight wide mobile seven wide tablet five wide widescreen column" )
print(gfg_timer_element)

# gfg_timer_text = gfg_timer_element.text.strip()

# print(f"GFG contest at :{gfg_timer_text}")

