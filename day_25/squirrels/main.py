import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grays = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
cinnamons = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()
blacks = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()

print(f"There are {grays} grays.")
print(f"There are {cinnamons} cinnamons.")
print(f"There are {blacks} blacks.")

data_dict = {
    "Fur Colors": ["Gray", "Cinnamon", "Black"],
    "Count" : [grays, cinnamons, blacks]
}

print(data_dict)

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")