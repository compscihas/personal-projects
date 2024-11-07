def calculate_bmi(weight, height, unit_system='metric'):
    if unit_system == '2':
        bmi = (weight / (height ** 2))  # BMI formula for imperial units
    else:
        bmi = weight / (height ** 2)  # BMI formula for metric units
    return round(bmi, 2)

def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Invalid gender. Please enter 'male' or 'female'.")
    return bmr

def adjust_for_activity_level(bmr, activity_level):
    # Scaled-down multipliers for more conservative adjustments
    if activity_level == '1':
        adjustment_factor = 1.1  # Minimal activity
    elif activity_level == '2':
        adjustment_factor = 1.2  # Light exercise/sports 1-3 days/week
    elif activity_level == '3':
        adjustment_factor = 1.3  # Moderate exercise/sports 3-5 days/week
    elif activity_level == '4':
        adjustment_factor = 1.4  # Hard exercise/sports 6-7 days/week
    elif activity_level == '5':
        adjustment_factor = 1.5  # Very hard exercise or a physical job
    else:
        raise ValueError("Invalid activity level. Please choose from 'sedentary', 'lightly active', 'moderately active', 'very active', 'extra active'.")

    return int(bmr * adjustment_factor)

def main():
    print("Welcome to the Nutrition Planning Program!")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()

    unit_system = input("Would you like to use metric or imperial units? (type 1 for metric or 2 for imperial): ").lower()

    if unit_system == '2':
        height_inches = float(input("Enter your height in inches: "))
        weight_pounds = float(input("Enter your weight in pounds: "))
        height_cm = height_inches * 2.54  # Convert inches to cm
        height_m = height_inches * 0.0254  # Convert inches to meters for BMI
        weight_kg = weight_pounds * 0.453592  # Convert pounds to kg
    else:
        height_cm = float(input("Enter your height in centimeters: "))
        height_m = height_cm / 100  # Convert cm to meters for BMI
        weight_kg = float(input("Enter your weight in kilograms: "))

    # Calculate BMI and BMR
    bmi = calculate_bmi(weight_kg, height_m, unit_system)
    bmr = calculate_bmr(weight_kg, height_cm, age, gender)

    # Ask for activity level
    print("\nHow active are you?")
    activity_level = input("Choose from: (1)'sedentary', (2)'lightly active', (3)'moderately active', (4)'very active', (5)'extra active': ").lower()
    suggested_calories = adjust_for_activity_level(bmr, activity_level)

    print("\n--- Nutrition Report ---")
    print(f"Your calculated BMI is: {bmi}")
    print(f"Your calculated BMR using the Mifflin-St Jeor formula is: {int(bmr)}")
    print(f"Suggested daily caloric intake based on your activity level: {suggested_calories} calories")
    print("Note: Always consult with a dietitian or doctor for personalized nutrition plans.")

if __name__ == "__main__":
    main()