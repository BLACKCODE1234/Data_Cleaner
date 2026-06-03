import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


file = pd.read_csv(r"C:\Users\USER\Desktop\DATASCIENCE\project\Economy\Ghana.csv")
file = file.fillna({"1960":0},inplace=True)
# print(file["1960"])
# print(file.to_string())
# print(file.head())
# print(file.columns)
print(file["1960"])