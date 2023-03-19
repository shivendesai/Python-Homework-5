# Written by Shiven Desai
# This program calculates the income generated from ticket sales at a stadium, based on the number of tickets sold for each seating category.

# Get the number of tickets sold for each seating category from the user
num_class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
num_class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
num_class_c_tickets = int(input("Enter the number of Class C tickets sold: "))

# Calculate the total income generated from ticket sales
total_income = num_class_a_tickets * 20 + num_class_b_tickets * 15 + num_class_c_tickets * 10

# Display the total income generated from ticket sales
print("Total income from ticket sales: $%.2f" % total_income)
