def calculate_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def get_marks(subjects):
    marks = {}
    for subject in subjects:
        while True:
            try:
                value = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= value <= 100:
                    marks[subject] = value
                    break
                print("Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter numeric marks.")
    return marks


def format_marksheet(student_name, marks, total, average, grade):
    lines = [
        f"Marks Sheet for: {student_name}",
        "=" * 40,
    ]
    for subject, score in marks.items():
        lines.append(f"{subject}: {score:.2f}")
    lines.extend([
        "=" * 40,
        f"Total Marks: {total:.2f}",
        f"Average Marks: {average:.2f}",
        f"Grade: {grade}",
    ])
    return "\n".join(lines)


def main():
    subjects = ["Math", "Science", "English", "History", "Computer"]
    print("\n=== Student Marks Sheet ===\n")
    student_name = input("Enter student name: ").strip() or "Unknown Student"
    marks = get_marks(subjects)

    total = sum(marks.values())
    average = total / len(subjects)
    grade = calculate_grade(average)

    report = format_marksheet(student_name, marks, total, average, grade)
    print("\n" + report + "\n")


if __name__ == "__main__":
    main()
