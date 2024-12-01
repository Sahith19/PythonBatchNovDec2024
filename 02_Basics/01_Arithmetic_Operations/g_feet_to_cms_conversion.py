"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""


feet = input("Enter the value in feet: ")
feet = float(feet)
cms = feet * 30.48
inches = feet * 12
centimeters = inches * 2.54
print(" feet to cms :",round(cms,2))
print(" feet to inches :",round(inches,2))
print(" inches to centimeters :",round(centimeters, 2))