def calculate_bmr(gender, height_ft, height_in, weight, age, activity_level):
    # Convert height to centimeters
    height_cm = height_ft * 30.48 + height_in * 2.54

    # Map of activity levels to their multipliers
    activity_levels = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    elif gender.lower() == 'female':
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError('Invalid gender')

    # Adjust BMR based on activity level
    if activity_level.lower() in activity_levels:
        bmr *= activity_levels[activity_level.lower()]
    else:
        raise ValueError('Invalid activity level')

    return bmr