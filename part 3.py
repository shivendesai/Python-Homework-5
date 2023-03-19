# Written by Shiven Desai
# This program calculates the amount of county and state sales tax collected by a retail company, based on the total sales for the month.

# Get the total sales for the month from the user
total_sales = float(input("Enter the total sales for the month: $"))

# Calculate the amount of county and state sales tax
county_sales_tax = total_sales * 0.025
state_sales_tax = total_sales * 0.05
total_sales_tax = county_sales_tax + state_sales_tax

# Display the amount of county and state sales tax, and the total sales tax
print("County sales tax: $%.2f" % county_sales_tax)
print("State sales tax: $%.2f" % state_sales_tax)
print("Total sales tax: $%.2f" % total_sales_tax)
