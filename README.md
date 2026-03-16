# Student Grade Calculator

## Project Overview
The Student Grade Calculator is a simple Python program that calculates a student's grade based on the marks entered by the user. The program takes the student’s name and marks as input, validates the marks, and then determines the grade according to predefined grading rules.

The goal of this project is to practice basic Python programming concepts such as conditional statements, loops, functions, and input validation while building a structured program.

---

## Project Objectives

- Accept student details as input
- Validate marks within the range of 0–100
- Calculate grade based on grading logic
- Display an encouraging message based on the student's performance
- Demonstrate basic Python programming structure

---

## Grading Logic

The program assigns grades based on the following criteria:

| Marks Range | Grade |
|-------------|------|
| 90 – 100 | A |
| 80 – 89 | B |
| 70 – 79 | C |
| 60 – 69 | D |
| 0 – 59 | F |

Each grade is accompanied by an encouraging message to provide feedback to the student.

Example messages:

- **A** → Excellent work! Keep it up!
- **B** → Very good! Keep improving!
- **C** → Good effort! Practice more.
- **D** → Keep trying! Improvement is possible.
- **F** → Don't give up! Work harder next time.

---

## Features

- Accepts student name and marks
- Validates marks between 0 and 100
- Uses a while loop to handle invalid inputs
- Calculates grades using if-elif-else statements
- Displays encouraging feedback messages
- Uses functions to organize program logic

---

## Technical Details

### Programming Concepts Used

**Conditional Statements**
- The grading system uses `if-elif-else` statements to determine the correct grade.

**Input Validation**
- A `while` loop ensures that the marks entered by the user fall within the valid range (0–100).

**Functions**
- A function is used to calculate the grade and return the corresponding message.

**Program Flow**

1. Ask the user to enter the student name
2. Request marks from the user
3. Validate marks using a loop
4. Calculate grade using conditional statements
5. Display the final result with a message

---

## Setup Instructions

### Requirements
- Python 3.x installed on your system

### Steps to Run the Program

1. Clone or download the repository
2. Open a terminal or command prompt
3. Navigate to the project folder

Run the program using: python grade_calculator.py


## Testing Evidence

The program has been tested with multiple inputs to ensure:

- Correct grade calculation
- Proper handling of invalid inputs
- Accurate display of encouraging messages

Example test scenarios include:

- Valid marks input
- Marks above 100
- Marks below 0
- Different grade boundaries

Detailed test cases can be found in `test_cases.txt`.

---

## Visual Documentation

Screenshots of the program execution are included in the **screenshots** folder to demonstrate the working of the application.

Examples include:

- Successful program execution
- Grade output display
- Handling of invalid marks input

