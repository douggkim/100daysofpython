import requests

class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"

    def get_blog(self) -> dict[str]:
        response = requests.get(self.url).json()

        return response

