#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("what was the total bill?")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
split = input("How many people to split the bill? ")

bill_int = int(bill)
tip_int = int(tip)
split_int = int(split)

bill_with_tip = (((tip_int / 100) * bill_int) + bill_int)

split_total = bill_with_tip / split_int
split_total_int = int(split_total)

new_total = round(split_total_int, 2)

print(new_total)
