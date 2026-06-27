import numpy as np

student_name = input("Enter Student Name: ")
student_class = input("Enter Student Class: ") # type: ignore

math = int(input("Enter Math score: "))
science = int(input("Enter Science score: "))
english = int(input("Enter English score: "))
hindi = int(input("Enter Hindi score: "))
computer = int(input("Enter Computer score: "))

total = math + science + english + hindi + computer
print(f"Total Score: {total}")

average = total / 5
print(f"Average Score: {average}")

highest = max(math, science, english, hindi, computer)
print(f"Highest Score: {highest}")

lowest = min(math, science, english, hindi, computer)
print(f"Lowest Score: {lowest}")

persentage = (total / 500) * 100
print(f"Percentage: {persentage}%")


if persentage >= 33:
    print("Result: Pass")
    print(f"Congratulations ! {student_name} for passing the exam with {persentage}% in {student_class} class.")
else:  
     print("Result: Fail")
     print(f"Sorry ! {student_name} for failing the exam with {persentage}% in {student_class} class. Better luck next time.")

print("\nReport Card:")