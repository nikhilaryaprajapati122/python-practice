import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Nikhil", "Ravi", "Aman", "Sohan"],
    "Marks": [80, 70, 90, 60]
}

df = pd.DataFrame(data)

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()