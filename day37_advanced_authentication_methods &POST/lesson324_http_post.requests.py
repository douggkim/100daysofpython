import requests

# DOCUMENTATION : https://docs.pixe.la/
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




