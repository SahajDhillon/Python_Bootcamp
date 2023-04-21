# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

bill = float(input("Enter the bill:"))
members = float(input("amount of members:"))
tip = float(input("Enter the  amount of tip 12%, 15% or 20%"))
Total_bill = (tip/100*bill) + bill
print(Total_bill)
after_split = Total_bill/members
after_split = str(round(after_split, 2))
print(f"Total bill after split is {after_split}")