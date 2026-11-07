# creating daily activity tracker
import requests
from datetime import datetime

#"HTTP POST" of request module
# Step:1 creating user account on pixela
# pixela_endpoint="https://pixe.la/v1/users"
#
# user_params = {
#     "token": "pxmanash",
#     "username":"manashvi",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Step:2 create a graph definition
# USERNAME="manashvi"
# TOKEN="pxmanash"
#
# pixela_endpoint="https://pixe.la/v1/users"
# user_params = {
#      "token": TOKEN,
#      "username":USERNAME,
#      "agreeTermsOfService":"yes",
#      "notMinor":"yes"
# }
#
# graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config={
#     "id":"graph1",
#     "name":"course",
#     "unit":"min",
#     "type":"int",
#     "color":"sora"
#
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response=requests.post(graph_endpoint, json=graph_config,headers=headers)
# print(response.text)

# Step:3 Get the graph

#https://pixe.la/v1/users/a-know/graphs/test-graph this one is like syntax
#https://pixe.la/v1/users/manashvi/graphs/graph1.html

# Step:4 Post value to graph
USERNAME="manashvi"
TOKEN="pxmanash"
GRAPH_ID="graph1"
pixela_endpoint="https://pixe.la/v1/users"

user_params = {
      "token": TOKEN,
      "username":USERNAME,
      "agreeTermsOfService":"yes",
      "notMinor":"yes"
}

graph_config={
     "id":GRAPH_ID,
     "name":"course",
     "unit":"min",
     "type":"int",
     "color":"sora"
}

headers = {
     "X-USER-TOKEN": TOKEN
}

pixela_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today= datetime.now()

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"50",
}

response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

#How to use PUT(update) and DELETE of request module

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity":"39"
}
# response1=requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response1.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response2 = requests.delete(url=delete_endpoint, headers=headers)
# print(response2.text)