"""
Student Grade Management System
Author: Ashu
Simple console app using dictionaries, lists, and basic control flow.
"""

import json

# Data structure:
# students = {
#    student_id: {
#        "name": "Alice",
#        "marks": {"Math": 90, "Physics": 85, ...}
#    },
#    ...
# }

students = {}
next_id = 1  # auto-increment student ID


def input_nonempty(prompt):
    s = input(prompt).strip()
    while not s:
        s = input("Please enter a value: ").strip()
    return s


def add_student():
    global next_id
    name = input_nonempty("Enter student name: ")
    students[next_id] = {"name": name, "marks": {}}
    print(f"Student added with ID: {next_id}")
    next_id += 1


def remove_student():
    sid = input_nonempty("Enter student ID to remove: ")
    if not sid.isdigit() or int(sid) not in students:
        print("Invalid ID.")
        return
    sid = int(sid)
    confirm = input(f"Delete {students[sid]['name']} (ID {sid})? (y/n): ").lower()
    if confirm == "y":
        del students[sid]
        print("Student removed.")
    else:
        print("Cancelled.")


def add_or_update_marks():
    sid = input_nonempty("Enter student ID: ")
    if not sid.isdigit() or int(sid) not in students:
        print("Invalid ID.")
        return
    sid = int(sid)
    subject = input_nonempty("Enter subject name: ")
    score_str = input_nonempty("Enter marks (0-100): ")
    if not score_str.isdigit():
        print("Marks must be a number.")
        return
    score = int(score_str)
    if not (0 <= score <= 100):
        print("Marks should be between 0 and 100.")
        return
    students[sid]["marks"][subject] = score
    print(f"Marks updated for {students[sid]['name']} -> {subject}: {score}")


def calculate_total_percentage_grade(marks_dict):
    if not marks_dict:
        return 0, 0.0, "N/A"
    total = sum(marks_dict.values())
    count = len(marks_dict)
    percentage = total / count
    grade = get_grade(percentage)
    return total, percentage, grade


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"


def view_student():
    sid = input_nonempty("Enter student ID: ")
    if not sid.isdigit() or int(sid) not in students:
        print("Invalid ID.")
        return
    sid = int(sid)
    s = students[sid]
    print(f"\n--- Student: {s['name']} (ID {sid}) ---")
    if not s["marks"]:
        print("No marks recorded yet.")
    else:
        for subj, m in s["marks"].items():
            print(f"{subj}: {m}")
    total, perc, grade = calculate_total_percentage_grade(s["marks"])
    print(f"Total: {total} | Average: {perc:.2f}% | Grade: {grade}")
    print("--------------------------------\n")


def list_all_students():
    if not students:
        print("No students available.")
        return
    print("\nAll Students:")
    for sid, info in students.items():
        total, perc, grade = calculate_total_percentage_grade(info["marks"])
        print(f"ID: {sid} | Name: {info['name']} | Avg: {perc:.2f}% | Grade: {grade}")
    print()


def show_topper():
    if not students:
        print("No students available.")
        return
    best_id = None
    best_perc = -1
    for sid, info in students.items():
        _, perc, _ = calculate_total_percentage_grade(info["marks"])
        if perc > best_perc:
            best_perc = perc
            best_id = sid
    if best_id is None or best_perc == 0:
        print("No marks available to determine topper.")
    else:
        s = students[best_id]
        print(f"Topper: {s['name']} (ID {best_id}) - Average: {best_perc:.2f}%")
    print()


def save_data(filename="students_data.json"):
    try:
        with open(filename, "w") as f:
            json.dump({"students": students, "next_id": next_id}, f, indent=2)
        print(f"Data saved to {filename}")
    except Exception as e:
        print("Error saving data:", e)


def load_data(filename="students_data.json"):
    global students, next_id
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        students = data.get("students", {})
        next_id = data.get("next_id", 1)
        # keys in JSON become strings, convert to int keys
        students = {int(k): v for k, v in students.items()}
        print(f"Data loaded from {filename}")
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
    except Exception as e:
        print("Error loading data:", e)


def menu():
    print("""
===== Student Grade Management System =====
1. Add student
2. Remove student
3. Add / Update marks
4. View student details
5. List all students
6. Show topper
7. Save data
8. Load data
9. Exit
""")

def main():
    load_data()  # try to load existing data automatically
    while True:
        menu()
        choice = input("Enter choice (1-9): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            add_or_update_marks()
        elif choice == "4":
            view_student()
        elif choice == "5":
            list_all_students()
        elif choice == "6":
            show_topper()
        elif choice == "7":
            save_data()
        elif choice == "8":
            load_data()
        elif choice == "9":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
