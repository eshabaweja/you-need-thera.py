# Create a dataframe from scrach
import pandas

data_dict = {
    "names": ["Reggie", "Five", "Vanya"],
    "scores": [57, 69, 83]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_dataframe.csv")