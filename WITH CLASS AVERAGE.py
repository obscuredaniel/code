# Predefined subjects
subjects = ["Math", "English", "Science, "]

# Dictionary to store student data using ID as key
results = {}

# Ask how many students to enter
num_students = int(input("How many students do you want to enter? "))

# Collect input for each student
for _ in range(num_students):
    # Ensure unique 8-digit ID
    while True:
        student_id = input("\nEnter 8-digit unique Student ID: ").strip()
        if not student_id.isdigit():
            print("❌ Student ID must contain digits only.")
        elif len(student_id) != 8:
            print("❌ Student ID must be exactly 8 digits long.")
        elif student_id in results:
            print("❌ This ID already exists. Please enter a different one.")
        else:
            break  # Valid ID entered

    # Collect remaining student info after valid ID
    name = input("Enter student full name: ").strip().title()
    scores = {}

    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter score for {subject}: "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Store result using the validated ID
    results[student_id] = {"Name": name, **scores}

# Function to assign grade based on average
def assign_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

# Function to assign remark based on grade
def assign_remark(grade):
    remarks = {
        "A": "Excellent",
        "B": "Very Good",
        "C": "Good",
        "D": "Fair",
        "F": "Fail"
    }
    return remarks.get(grade, "")

# Function to calculate total, average, grade, remark
def calculate_results(data):
    summary = []
    for student_id, record in data.items():
        subject_scores = {sub: record[sub] for sub in subjects}
        total = sum(subject_scores.values())
        average = total / len(subjects)
        grade = assign_grade(average)
        remark = assign_remark(grade)

        student_record = {
            "ID": student_id,
            "Name": record["Name"],
            **subject_scores,
            "Total": total,
            "Average": round(average, 2),
            "Grade": grade,
            "Remark": remark
        }
        summary.append(student_record)
    return summary

# Function to calculate class average
def calculate_class_average(summary):
    if not summary:
        return 0
    total_avg = sum(student["Average"] for student in summary)
    return round(total_avg / len(summary), 2)

# Function to display the ranked result table
def display_results(summary):
    ranked = sorted(summary, key=lambda x: x["Average"], reverse=True)

    header = f"{'Rank':<7}{'ID':<12}{'Name':<15}" + "".join([f"{sub:<10}" for sub in subjects]) + f"{'Total':<10}{'Average':<10}{'Grade':<8}{'Remark'}"
    print("\n" + header)
    print("-" * len(header))

    for i, record in enumerate(ranked, start=1):
        row = f"{i:<7}{record['ID']:<12}{record['Name']:<15}" + "".join([f"{record[sub]:<10}" for sub in subjects]) + f"{record['Total']:<10}{record['Average']:<10}{record['Grade']:<8}{record['Remark']}"
        print(row)

    # Display class average at the end
    class_avg = calculate_class_average(summary)
    print(f"\nClass Average(%): {class_avg}")

# Run the logic
summary = calculate_results(results)
display_results(summary)
