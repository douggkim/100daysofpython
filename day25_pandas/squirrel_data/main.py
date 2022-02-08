import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.txt")
print(squirrel_data["Primary Fur Color"])

# number of squirrel for each color
# values : 어떤 열을 가지고 계산할 것인지 / aggfunc : 함수 / index : 어떤 값을 행으로 쓸 건지 / columns : column 내부 항목들을 쪼개서 열로 뿌려서 보여줌
print(pd.pivot_table(squirrel_data, index="Primary Fur Color", values="Unique Squirrel ID", aggfunc=["count"]))

# 아래도 가능
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinammon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinammon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_data.txt")
