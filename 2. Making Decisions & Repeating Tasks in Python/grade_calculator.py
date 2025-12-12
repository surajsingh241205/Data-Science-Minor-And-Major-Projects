# Student grade calculator module

import sys 

def get_valid_marks(prompt = "Enter marks (0 to 100) : "):
    
    while True:
        raw = input(prompt).strip() # remove extra spaces from the prompt
        if raw == "":
            print("No input provided. please enter valid marks between 0 and 100.")
            continue
        try:
            marks = int(raw)
        except Exception as err:
            print(f"Invalid input '{raw}'. Please enter an integer value between 0 and 100.")
            continue
        
        if 0 <= marks <= 100:
            return marks
        print("Out of range. Please enter marks between 0 and 100.")
        
def compute_grade_and_message(marks):
    if 90 <= marks <= 100:
        return 'A', "Excellent work!"
    elif 80 <= marks < 89:
        return 'B', "Very good job!"
    elif 70 <= marks < 79:
        return 'C', "Good effort!"
    elif 60 <= marks < 69:
        return 'D', "You passed."
    else:
        return 'F', "Better luck next time."
    
    
def main():
    print("==================== WELCOME TO THE STUDENT GRADE CALCULATOR ====================") 
    name = input("Enter the student's name: ").strip()
    if not name:
        print("No name provided. Exiting the program.")
        sys.exit(1)
        
    marks = get_valid_marks()
    grade, message = compute_grade_and_message(marks)
    print(f"\nStudent Name: {name}")
    print(f"Marks Obtained: {marks}")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        sys.exit(0)