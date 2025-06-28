# Predefined subjects
subjects = ["Math", "English", "Science"]

# Empty dictionary to store all results
results = {}

# Ask how many students to enter
num_students = int(input("How many students do you want to enter? "))

# Collect input for each student
for _ in range(num_students):
    name = input("\nEnter student name: ").strip().title()
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
    
    results[name] = scores

# Function to calculate total and average
def calculate_results(data):
    summary = {}
    for student, subjects in data.items():
        total = sum(subjects.values())
        average = total / len(subjects)
        summary[student] = {
            "Total": total,
            "Average": round(average, 2),
            **subjects
        }
    return summary

# Function to display result in a table format
def display_results(summary):
    header = f"{'Student':<10}" + "".join([f"{sub:<10}" for sub in subjects]) + f"{'Total':<10}{'Average':<10}"
    print("\n" + header)
    print("-" * len(header))
    for student, record in summary.items():
        row = f"{student:<10}" + "".join([f"{record[sub]:<10}" for sub in subjects]) + f"{record['Total']:<10}{record['Average']:<10}"
        print(row)

# Main logic
summary = calculate_results(results)
display_results(summary)
