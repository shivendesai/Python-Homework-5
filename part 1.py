# Written by Shiven Desai
# This program calculates the assessment value and property tax of a piece of property based on its actual value.

# Get the actual value of the property from the user
actual_value = float(input("Enter the actual value of the property: $"))

# Calculate the assessment value and property tax
assessment_value = actual_value * 0.6
property_tax = assessment_value / 100 * 72

# Display the assessment value and property tax
print("Assessment value: $%.2f" % assessment_value)
print("Property tax: $%.2f" % property_tax)
