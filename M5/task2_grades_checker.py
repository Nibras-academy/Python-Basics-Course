# Prompt the user to enter Math score
math_score = int(input("Enter your Math score: "))

# Prompt the user to enter Science score
science_score = int(input("Enter your Science score: "))

# Check eligibility for the final exam
if math_score >= 60 and science_score >= 60:
    print("Congratulations! You are eligible to take the final exam.")
elif math_score >= 60 or science_score >= 60:
    print("You are eligible to retake the exam for the subject you scored below 60.")
else:
    print("Sorry, you are not eligible to take the final exam.")



