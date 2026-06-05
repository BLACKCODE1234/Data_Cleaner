import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

file = pd.read_csv(r"C:\Users\USER\Desktop\DATASCIENCE\project\Economy\Nike_Sales_Uncleaned.csv")
# print(file.head())
# print(file.info())
# print(file.isnull().sum())
file["Order_Date"] = pd.to_datetime(file["Order_Date"], errors='coerce')
print(file.head())
file.to_csv(r"C:\Users\USER\Desktop\DATASCIENCE\project\Economy\Nike_Sales_Cleaned.csv", index=False)