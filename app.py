import pandas as pd

# Step 1: Create a DataFrame from a dictionary
data = {
    "Name": ["Ram", "Sita", "Gita", "Anuj"],
    "Age": [10, 20, 30, 25],
    "City": ["Delhi", "Mumbai", "Agra", "Jaipur"]
}

df = pd.DataFrame(data)
print(df)
df.to_csv("output.csv")
#df.to_excel("output.xlsx")
df.to_json("output.json")



