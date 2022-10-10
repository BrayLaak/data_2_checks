#    Pull in data from an API. Here's a list of public APIs that don't require Auth keys, 
#        though if you have another API you want to use feel free: https://apipheny.io/free-api/
#    Find and print TWO descriptive statistics about your data. This can be absolutely anything,
#        from the mean() or sum() of a column to the number of different categories,
#        to the number of null values in a column. We just want to see two pieces of information.
#    Write a query in Pandas to select a particular set of your data. 
#        You can use a mask or with .query(), but we want you to pull out a subset based on 
#        any parameter you like. This could be "show me every row where HTTPS=False" or anything else.
#    Select and print the SECOND AND THIRD columns of your data frame.
#    Select and print the FIRST 4 rows of you data frame.

import pandas as pd
import requests as rq
import json

bored_api_url = 'https://www.boredapi.com/api/activity'

#initialize df
r = rq.get(bored_api_url)

bored_dict = r.json()
bored_df = pd.json_normalize(bored_dict)

bored_df = bored_df.drop(labels=0, axis=0)


while True:
    try:
        num_activities = int(input("How many activity options would you like? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if num_activities < 5:
        print("Sorry, I want more options.")
        continue
    
    elif num_activities > 20:
        print("Sorry, I'm too tired for that many.")
        continue   
    
    else:
        break


for activity in range(num_activities):
    
    r = rq.get(bored_api_url)
    activity_dict = r.json()
    print(activity_dict)
    activity_df = pd.json_normalize(activity_dict)

    bored_df = bored_df.append(activity_df, ignore_index=True)


bored_df.describe()

print(bored_df.loc[bored_df['type'] == 'social'])

print(bored_df[['activity','type']].head())

print(bored_df.iloc[:, 1:3])

print(bored_df.iloc[0:4])