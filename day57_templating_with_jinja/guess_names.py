import requests


class GuessNames:
    def __init__(self, input_name: str):
        self.name_input = input_name

    def guess_age(self) -> str:
        age_response = requests.get(f"https://api.agify.io/?name={self.name_input}").json()
        age_guess = age_response["age"]

        return age_guess

    def guess_gender(self) -> str:
        response = requests.get(f"https://api.genderize.io/?name={self.name_input}").json()
        gender_guess = response["gender"]

        return gender_guess
