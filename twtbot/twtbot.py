#!/usr/bin/env python
# coding: utf-8

# In[30]:


#!pip install pandas


# In[31]:



import tweepy
import webbrowser
import datetime
import pandas as pd


# In[32]:


consumer_key="xxx"
consumer_secret="xxx"


#access_token="xxx"
#access_token_secret="xxx"

callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret,callback_uri)
#auth.set_access_token(access_token, access_token_secret)

redirect_url = auth.get_authorization_url()
webbrowser.open(redirect_url)
user_pint_input = input("What's the pin value?")
auth.get_access_token(user_pint_input)


# In[33]:


api = tweepy.API(auth)


# In[34]:


me = api.me()
print(me.screen_name)


# In[55]:


#my_timeline = api.home_timeline()


# In[56]:


columns = set()
allowed_types = [str, int]
tweets_data = []
for status in my_timeline:
    print(status.author.screen_name)
    status_dict = dict(vars(status))
    keys = vars(status).keys()
    single_tweet_data = {"user": status.user.screen_name, "author":status.author.screen_name}
    for k in keys:
        try:
            v_type = type(status_dict[k])
        except:
            v_type = None
        v_type = type(status_dict[k])
        if v_type in allowed_types:
            single_tweet_data[k] = status_dict[k]
        columns.add(k)
    tweets_data.append(single_tweet_data)

header_cols = list(columns)


# In[57]:


tweets_data


# In[58]:


#df = pd.DataFrame(tweets_data, columns= header_cols)
#df.head()


# In[65]:


#img_obj = api.media_upload("img3.png")


# In[66]:


#new_status = api.update_status("#Prachbot img timeline", media_ids=[img_obj.media_id_string])


# In[67]:


#len(api.home_timeline())


# In[ ]:


#for i, status in enumerate(tweepy.Cursor(api.home_timeline).items(50)):
#    print(i, status.text)

