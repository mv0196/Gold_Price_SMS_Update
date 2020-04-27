#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
import bs4
import re
from datetime import datetime as dt
import time


# In[2]:


url_gold='https://www.ndtv.com/business/commodity/gold-price_gold'
url_silver='https://www.ndtv.com/business/commodity/silver-price_silver'


# In[ ]:


auth_key=input("Enter the authentication key:")
no=input("Enter the contact number:")#numbers separated by , on which message is to be sent


# In[3]:


def send_sms(url_gold,url_silver,no):
    res_g=requests.get(url_gold)

    s_g=bs4.BeautifulSoup(res_g.text,'html')
    mydivs_g = s_g.findAll("td", {"class": "txt-right"})

    mydiv_g=str(mydivs_g)
    
    match_g=re.search('>(.+)<',mydiv_g)
    price_g=match_g.group(1)

    
    
    res_s=requests.get(url_silver)

    s_s=bs4.BeautifulSoup(res_s.text,'html')
    mydivs_s = s_s.findAll("td", {"class": "txt-right"})

    mydiv_s=str(mydivs_s)
    
    match_s=re.search('>(.+)<',mydiv_s)
    price_s=match_s.group(1)

    
    
    msg='Current Gold(MCX) price at time '+str(dt.now().hour)+':'+str(dt.now().minute)+' is: Rs.'+price_g+'/- per 10gm'+' and Current Silver(MCX) price is: Rs.'+price_s+'/- per 1kg'
    
    api_url_gold_base = 'https://www.fast2sms.com/dev/bulk?authorization='+auth_key+'&sender_id=FSTSMS&message='+msg+'&language=english&route=p&numbers='+no#+'&flash=1'
    

    response = requests.get(api_url_gold_base)
    print(response.status_code)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


# In[ ]:


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23) and dt.now().weekday()!=5 and dt.now().weekday()!=6:
        sms = send_sms(url_gold)
        time.sleep(3600)
        


# In[ ]:




