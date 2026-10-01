# Student Grade Calculator

def calculate_grade(average):
    """Function to determine the letter grade based on average score."""
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F (Fail)'

def main():
    print("=" * 40)
    print("   STUDENT GRADE CALCULATOR & TRACKER")
    print("=" * 40)

    student_name = input("\nEnter Student Name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    
    # Input loop to collect marks for each subject
    for i in range(1, num_subjects + 1):
        while True:
            try:
                score = float(input(f"Enter marks for Subject {i} (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Invalid score! Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    # Calculations
    total_marks = sum(marks)
    average_marks = total_marks / num_subjects
    grade = calculate_grade(average_marks)

    # Output Summary
    print("\n" + "-" * 40)
    print("           PERFORMANCE SUMMARY          ")
    print("-" * 40)
    print(f"Student Name   : {student_name}")
    print(f"Total Subjects : {num_subjects}")
    print(f"Total Score    : {total_marks:.2f} / {num_subjects * 100}")
    print(f"Average Score  : {average_marks:.2f}%")
    print(f"Final Grade    : {grade}")
    print("-" * 40)

if __name__ == "__main__":
    main()