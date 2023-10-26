# Prompt the user for hours and rate per hour
weight = input("Enter weight: ")
height = input("Enter height in Meters: ")

# Convert the input strings to floating-point numbers
weight = float(weight)
height = float(height)

# Calculate gross pay
BMI= weight/height**2

# Display the result
print("BMI:", BMI)

if BMI < 18.5:
    print("You're in the underweight range")
elif 18.5 <= BMI < 25:
    print("You're in the healthy weight range")
elif 25 <= BMI < 30:
    print("You're in the overweight range")
else:
    print("You're in the obese range")




