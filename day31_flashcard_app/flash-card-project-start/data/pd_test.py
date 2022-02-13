import pandas as pd
import random

vocab_raw = pd.read_csv("french_words.csv")
vocab_dict = vocab_raw.to_dict(orient="records")
print(vocab_dict)
print(random.choice(vocab_dict))
print(random.choice(vocab_dict)["French"])
print(random.choice(vocab_dict)["English"])