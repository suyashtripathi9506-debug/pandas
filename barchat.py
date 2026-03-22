import matplotlib.pyplot as plt

# Data
students = ["Aman", "Rahul", "Riya", "Sita"]
marks = [80, 70, 90, 85]

# Bar Chart
plt.bar(students, marks)


# Title and Labels
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")


# Show chart
plt.show()