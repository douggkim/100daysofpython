import requests
import pprint

class SearchMovie():
    def __init__(self):
        self.target_url = "https://api.themoviedb.org/3/search/movie"
        with open("CONFIG.txt") as file:
            self.api_token = file.readline().strip()
        self.params = {
            "language": "en-US",
            "api_key": self.api_token,
            "include_adult": "false",
            "query": ""
        }

    def search(self, movie_name: str) -> dict[str]:
        '''Search for the movie in themoviedb. INPUT: movie_name'''
        self.params["query"] = movie_name
        response = requests.get(self.target_url, params=self.params).json()
        print(response)
        pprint.pprint(response["results"])
        for result in response["results"]:
            print(result["id"])
            print(result["original_title"])
            print(result["overview"])
            print(result["release_date"])
            print(result["poster_path"])
            print("===============================")

        return response["results"]



