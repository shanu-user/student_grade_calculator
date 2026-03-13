print("Enter student name: ")
name = input()

print("Enter marks (0-100): ")
marks = int(input())

def remarks(marks):
    if marks>=90 and marks<=100:
        grade='A'
    elif marks>=80 and marks<=89:
        grade='B'
    elif marks>=70 and marks<=79:
        grade='C'
    elif marks>=60 and marks<=69:
        grade='D'
    elif marks>=0 and marks<=59:
        grade='F'
    return grade

print(f"📊RESULT FOR {name.upper()}")
print(f"Grade: {remarks(marks)}")
print("Message: Very Good! Keep it up! 👍")
