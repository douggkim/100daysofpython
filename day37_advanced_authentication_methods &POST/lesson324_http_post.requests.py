import requests
import datetime

# DOCUMENTATION : https://docs.pixe.la/

# TODO 1 : Create USER
USERNAME = "dougie"
with open("CONFIG.txt") as file:
    TOKEN = file.readline()
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "dougie",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# json : json 형태의 데이터를 넘겨줌
# {'message': "Success. Let's visit https://pixe.la/@dougie , it is your profile page!", 'isSuccess': True}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.json())

# TODO 2 : Create graph
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}
# Token 은 주로 header에 넣을 것. log에 안 남고, Sniffing 에 취약함.
graph_header = {
    "X-USER-TOKEN": TOKEN
}

# CHECK THE GRAPH : https://pixe.la/v1/users/dougie/graphs/graph1.html
response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=graph_header)
print(response.text)

# TODO 3 : FILL GRAPH
# https://docs.pixe.la/entry/post-pixel

pixela_post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# strftime() 으로 원하는 식으로 날짜 데이터를 수정할 수 있음
today = datetime.date(year=2022, month=2, day=14)

post_pixel_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run today? ")
}

response = requests.post(url=pixela_post_pixel_endpoint, json=post_pixel_parameter, headers=graph_header)
print(response.json())

# TODO 4: UPDATE PIXEL

pixela_put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

put_pixel_parameters = {
    "quantity": "32",
}

response = requests.put(url=pixela_put_pixel_endpoint, json=put_pixel_parameters, headers=graph_header)

# TODO 5 : DELETE PIXEL

pixela_delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

response = requests.delete(url=pixela_delete_pixel_endpoint, headers=graph_header)