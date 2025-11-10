#--------------------------------------------------------
# Name: SNEHANSH JANGIR
# Date: 06-Nov-2025
# Project Title: Daily Calorie Tracker CLI
#--------------------------------------------------------

#----WELCOME MESSAGE----

print("********************************************************************")
print("             Welcome to the Daily Calorie Tracker!              ")
print("********************************************************************")
print("This program helps you log your meals, track total calories,")
print("compare them with your daily calorie limit, and view a summary.\n")

#----INPUTS FROM THE USER----

meals = []
calories = []

num_meals = int(input("How many meals do you want to enter today? :"))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal_name = input("Enter meal name (e.g., Breakfast): ")
    calorie_value = float(input("Enter calorie amount: "))
    meals.append(meal_name)
    calories.append(calorie_value)

#----CALORIE CALCULATION----

total_calories = sum(calories)
average_calories = total_calories / len(calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))

#----LIMIT WARNINGS----

if total_calories > daily_limit:
    status = "ATTENTION!!You have exceeded your daily calorie limit"
else:
    status = "  HURRAYY!!! You are within your daily calorie limit."

#----FORMATTED OUTPUT----

print("\n+================ DAILY CALORIE REPORT =================+")
print("| \t\tMeal Name\t\t\t|\t\t\tCalories \t\t|")
print("+-------------------------------------------------------+")

for i in range(len(meals)):
    print(f"| \t  \t\t{meals[i]:<15}|\t\t\t{calories[i] }\t\t\t|")

print("+-------------------------------------------------------+")
print(f"| \t\t\t\t\tTotal:\t\t{total_calories}\t\t\t\t\t|")
print(f"| \t\t\t\t\tAverage:\t{average_calories:.2f}\t\t\t\t\t|")
print(f"|{status}  |")
print("+=======================================================+\n")

#----SAVE LOG FILE----

save = input("Do you want to save this session to a file? (yes/no): ").lower()

if save == "yes":
    from datetime import datetime
    filename = "calorie_log.txt"
    with open(filename, "w") as file:
        file.write("========== Calorie Tracker Session ==========\n")
        file.write(f"Date & Time: {datetime.now()}\n\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}\t{calories[i]}\n")
        file.write("--------------------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Status: {status}\n")
    print(f"Session saved successfully to {filename}")
else:
    print("Session not saved. Exiting program...")

print("\nThank you for using Daily Calorie Tracker! Stay healthy  :)")

#-------------------------------FINISHED-------------------------------