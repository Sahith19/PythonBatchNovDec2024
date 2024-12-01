"""
convert from hex to oct , and vice versa
"""

# Hex to Oct
hex_value = input("Enter a hex num : ")
decimal_value = int(hex_value, 16)  # Convert hex to decimal
octal_value = oct(decimal_value)   # Convert decimal to octal
print(octal_value)

# Oct to Hex
octal_value = input("Enter an oct num : ")
decimal_value = int(octal_value, 8)  
hex_value = hex(decimal_value)      
print(hex_value)

