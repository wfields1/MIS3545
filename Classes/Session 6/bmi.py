import math

def calculate_bmi(weight, height):
    BMI = 703 * (weight / (height*height))

    if BMI >= 30:
        print('Your BMI is {:.1f}. You are obese.'.format(BMI))
    elif BMI >= 25:
        print('Your BMI is {:.1f}. You are overweight.'.format(BMI))
    elif BMI >= 18.5:
        print('Your BMI is {:.1f}. You are normal weight.'.format(BMI))
    else:
        print('Your BMI is {:.1f}. You are underweight.'.format(BMI))

weight = input('What is your weight in pounds? ')
height = input('What is your height in inches? ')

weight = float(weight)
height = float(height)



