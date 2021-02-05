import requests
import numpy as np


BASE = "http://127.0.0.1:3000/"
# BASE = "https://capstone-2021.herokuapp.com/"

# response = requests.patch(BASE + "2", {"txt": "whatthefuck"})
# print(response.json())
# BASE = 'http://viethoangtranduong.pythonanywhere.com/'
# BASE = "http://127.0.0.1:3001/"
# BASE = 'http://ec2-18-232-83-67.compute-1.amazonaws.com:3000/'


data = [{"publication_url": 'https://medium.com/swlh', 'year_query': 2019},
        {"publication_url": 'https://towardsdatascience.com', 'year_query': 2020}]
        

print("Test 1: put response")

for i in range(len(data)):
    print(BASE + 'running', data[i])
    response = requests.put(BASE + "running", data[i])
    
    print(response)
    print(response.json())
    print("")

# print("Test 2: get response")

# response = requests.get(BASE + "1")
# print(response.json())

# print("Test 3: not existed")

# response = requests.get(BASE + "9")
# print(response.json())

# print("Test 4: delete")

# response = requests.delete(BASE + "0")
# print(response)

