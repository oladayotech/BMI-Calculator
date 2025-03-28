# Body Mass Index (BMI)
# BMI is calculated by dividing your weight (in kilograms)
# by the square of your height (in meters)

import time

# Function to print out text slowly
def type_text(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
    
# Function to get unit to for height and weight to be measured in 
def print_dict(dicts):
    for key, value in dicts.items():
        print(f"{key}. {value}")

def iterate_dicts(dicts, user_input):
        for key, value in dicts.items():
            if user_input in dicts[key]:
                return key
        print("ERROR! Invalid input")
        
def get_weight_unit_height_unit(unit_weight, unit_height): 
    # Dictionary to be iterated on to 
    # print on screen for user to select
    weight_unit_dict = {1:'kilogram(kg)', 2:'Pounds(lb)'}
    height_unit_dict = {1:'feet(ft)',2:'centimeter(cm)',3:'meters(m)'}
    height_unit = weight_unit = 0

    while weight_unit == 0 or weight_unit == None:
        # Input to get the unit height will be calculated in
        print("\nSelect a unit to input your height")
        
        print_dict(weight_unit_dict)

        get_weight_unit = input("").lower()
        weight_unit = iterate_dicts(unit_weight, get_weight_unit)

    while height_unit == 0 or height_unit == None:
        print("\nSelect a unit to input your weight")

        print_dict(height_unit_dict)
            
        get_height_unit = input("").lower()
        height_unit = iterate_dicts(unit_height, get_height_unit)
            
    print(weight_unit, height_unit)
    return weight_unit, height_unit

def get_weight_height(weight_unit, height_unit):
    if weight_unit == None:
        weight = None
        print("height's unit is empty")
    elif weight_unit == 'kg':
        get_weight = float(input("Input your weight in kg"))
        print(get_weight)
        weight = get_weight
    elif weight_unit == 'lb':
        get_weight = float(input("Input your weight in lb"))
        print(get_weight)
        weight = get_weight * 0.45

    if height_unit == None:
        height = None
        print("height's unit is empty")
    elif height_unit == 'ft':
        get_height = input("\nInput your height in feet (E.g 5 ft 9)")
        splitted_height = get_height.split("ft")
        get_height = [int(height) for height in splitted_height]
        print(get_height)
        if len(get_height) >= 2:
            height = (get_height[0] * 0.3048) + (get_height[1] * 0.0254)
        else:
            height = (get_height[0] * 0.3048)
    elif height_unit == 'cm':
        get_height = float(input("Input your weight in cm"))
        print(get_height)
        height = get_height * 0.01
    elif height_unit == 'm':
        get_height = float(input("Input your weight in m"))
        print(get_height)
        height = get_height

    return weight, height

def bmi_calculator(get_weight, get_height):
    if get_weight == None:
        print(f"Error, You must have inputted wrong weight ")
    elif get_height == None:
        print(f"Error, You must have inputted height")
    else:
        result = get_weight / (get_height ** 2)
        result = round(result, 2)
    return result

def main():
    possible_user_input_kg = ['kilogram', 'kg', '1']
    possible_user_input_lb = ['pounds', 'lb', '2']
    
    possible_user_input_feet = ['feet', 'ft', '1']
    possible_user_input_cm = ['centimeter', 'cm', '2']
    possible_user_input_m = ['meters', 'm', '3']
    unit_weight = {'kg': possible_user_input_kg, 'lb': possible_user_input_lb}
    unit_height = {'ft': possible_user_input_feet, 'cm': possible_user_input_cm, 'm': possible_user_input_m}
    
    while True:
        type_text("""Body Mass Index (BMI)
BMI is calculated by dividing your weight (in kilograms) by the square of your height (in meters).""")
        
        weight_unit, height_unit = get_weight_unit_height_unit(unit_weight, unit_height)
        weight, height = get_weight_height(weight_unit, height_unit)
        BMI = bmi_calculator(weight, height)

        print(f"Your Body Mass Index (BMI) is: {BMI}")

        type_text("""\nKeep in mind that BMI is not a perfect measure, as it does not take into account muscle mass or body composition. 
However, it can provide a general indication of whether your weight is in a healthy range.
""")

        check_again = input("Do you want to check your bmi again (yes/no)")
        if check_again.lower() == 'no':
            break

main()