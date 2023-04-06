import json
import pandas as pd
from TikTokApi import TikTokApi

# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial



pd.set_option('display.max_colwidth', None)

def extract_numbers_from_link(link):
    split_link = link.split("/")
    return split_link[-2]


def makePandas(x):
    if type(x) == dict:
        return pd.DataFrame.from_dict(x)
    elif type(x) == list:
        return pd.DataFrame(x)
    else:
        print(f"Type invalid, {type(x)}")
def generate_tree(dictionary, level=0):
    for key in dictionary.keys():
        if key[0].isdigit():  # check if the first character of the key is a digit
            continue  # skip the key if it starts with a digit
        print("  " * level + key)
        if isinstance(dictionary[key], dict):
            generate_tree(dictionary[key], level + 1)

def generate_keys(dictionary, path=''):
    for key in dictionary.keys():
        if key[0].isdigit():  # check if the first character of the key is a digit
            continue  # skip the key if it starts with a digit
        new_path = f"{path}['{key}']"
        print(new_path)
        if isinstance(dictionary[key], dict):
            generate_keys(dictionary[key], new_path)

def tiktokget(dicti):
    if type(dicti) == dict:

        for i in dicti.keys():
            tiktokget(dicti[i])


file = open("user_data.json", "r", encoding="utf8")
data = json.load(file)


dataArr = []


likes = data['Activity']['Like List']['ItemFavoriteList']
loginhistory = data['Activity']['Login History']['LoginHistoryList']
locationdata = data['Activity']['Most Recent Location Data']['LocationData']
vidlist = data['Activity']['Video Browsing History']['VideoList']
ads = data['Ads and data']['Ads Based On Data Received From Partners']
partnerlist = data['Ads and data']['Ads Based On Data Received From Partners']['DataPartnerList']
advlist = data['Ads and data']['Ads Based On Data Received From Partners']['AdvertiserList']
interests = data['App Settings']['Settings']['SettingsMap']['Interests']

dataArr.append(likes)
dataArr.append(loginhistory)
dataArr.append(locationdata)
dataArr.append(vidlist)
dataArr.append(ads)
dataArr.append(advlist)
dataArr.append(interests)

vidlist = pd.DataFrame.from_records(vidlist)
likes = pd.DataFrame.from_records(likes)

vidlist['id'] = vidlist['Link'].apply(extract_numbers_from_link)
likes['id'] = likes['Link'].apply(extract_numbers_from_link)

print(vidlist)
print(likes)

with TikTokApi() as api:
   video_data = api.video(id='https://www.tiktokv.com/share/video/7147050262430059818/').info_full()


print(video_data)

