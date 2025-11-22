# -------------------------------------------------------
# Name: Snehansh Jangir
# Date: 18-Nov-2025
# Project: GradeBook Analyzer
# -------------------------------------------------------
import csv

print("=======================================")
print("      SIMPLE GRADEBOOK ANALYZER        ")
print("=======================================")

print("\n1. Enter student marks manually")
print("2. Load marks from CSV file")
print("3. Exit")

choice = input("Enter your choice: ")

marks = {}

# ----------- CHOICE 1- MANUAL ENTRY -----------
if choice == "1":
    n = int(input("\nHow many students? "))
    for i in range(n):
        name = input(f"Enter student {i+1} name: ")
        score = float(input(f"Enter marks(out of hundred) for {name}: "))
        marks[name] = score

# ----------- CHOICE 2- CSV IMPORT -----------
elif choice == "2":
    file_name = input("Enter CSV file name: ")
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                marks[row[0]] = float(row[1])
        print("CSV loaded successfully!")
    except:
        print("Could not open file. Try again.")
 #       continue

elif choice == "3":
    print("Exiting program...")
 #   break

else:
    print("Invalid option. Try again.")
 #   continue

# ----------- STATISTICS -----------
scores = list(marks.values())
average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

# Median
scores_sorted = sorted(scores)
mid = len(scores_sorted) // 2
if len(scores_sorted) % 2 == 0:
    median = (scores_sorted[mid - 1] + scores_sorted[mid]) / 2
else:
    median = scores_sorted[mid]

print("\n----- STATISTICS -----")
print("Average:", round(average, 2))
print("Median:", median)
print("Highest:", highest)
print("Lowest:", lowest)

# ----------- GRADES -----------
grades = {}
for name, score in marks.items():
    if score >= 90:
        grades[name] = "A"
    elif score >= 80:
        grades[name] = "B"
    elif score >= 70:
        grades[name] = "C"
    elif score >= 60:
        grades[name] = "D"
    else:
        grades[name] = "F"

# ----------- PASS/FAIL LISTS -----------
passed = [name for name, s in marks.items() if s >= 40]
failed = [name for name, s in marks.items() if s < 40]

print("\n----- PASS/FAIL -----")
print("Passed:", passed)
print("Failed:", failed)

# ----------- RESULTS TABLE -----------
print("\n+--------- FINAL RESULTS ---------+")
print("|   Name\t\t\tMarks\tGrade |")
print("+---------------------------------+")
for name in marks:
    print(f"|\t{name:<15}\t{marks[name]}\t{grades[name]}\t  |")
print("+---------------------------------+") 

# ----------- OPTIONAL CSV EXPORT -----------
save = input("\nSave results to CSV? (yes/no): ").lower()
if save == "yes":
    with open("grade_output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks", "Grade"])
        for name in marks:
            writer.writerow([name, marks[name], grades[name]])
    print("Saved to grade_output.csv!")

print("\nAnalysis done!\n")
