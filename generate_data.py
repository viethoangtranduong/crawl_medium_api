import requests
import numpy as np


BASE = "http://ec2-54-221-124-167.compute-1.amazonaws.com:2110/"
# BASE = "https://capstone-2021.herokuapp.com/"

# response = requests.patch(BASE + "2", {"txt": "..."})
# print(response.json())
# BASE = 'http://viethoangtranduong.pythonanywhere.com/'
# BASE = "http://127.0.0.1:3001/"
# BASE = 'http://ec2-18-232-83-67.compute-1.amazonaws.com:3000/'

# src_link: https://medium.com/better-marketing/43-active-publications-on-medium-in-2020-8a03c1e5b7c9

medium_links = [
    'https://medium.com/human-parts', 
    'https://medium.com/one-zero', 
    'https://medium.com/elemental-by-medium', 
    'https://medium.com/forge', 
    'https://gen.medium.com/',
    'https://medium.com/marker',
    'https://modus.medium.com/',
    'https://medium.com/heated',
    'https://medium.com/zora',
    'https://medium.com/swlh',
    'https://medium.com/the-mission',
    'https://medium.com/personal-growth',
    'https://towardsdatascience.com/',
    'https://uxdesign.cc/',
    'https://uxplanet.org/',
    'https://writingcooperative.com/',
    'https://medium.muz.li/',
    'https://psiloveyou.xyz/',
    'https://byrslf.co/',
    'https://blog.prototypr.io/',
    'https://entrepreneurshandbook.co/',
    'https://medium.com/dailyjs'
]

years = [2019, 2020]


# data = [{"publication_url": 'https://medium.com/swlh', 'year_query': 2019},
#         {"publication_url": 'https://towardsdatascience.com', 'year_query': 2020}]
        

print("Test 1: put response")

for medium_link in medium_links:
    for year in years:
        data = {"publication_url": medium_link, 'year_query': year}
        try:
            print(BASE + 'running', data)
            response = requests.put(BASE + "running", data)
            
            print(response)
            print(response.json())
            print("")
        except:
            print("Error in:", data)


