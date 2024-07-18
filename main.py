print("Welcome to the tip calculator.")
Total_bill = input("What was the total bill?$")
Tip = input("What percentage tip would you like to give? 10, 12 or 15")
Num_people = input("How many people to split the bill?")
Total_bill = float(Total_bill)
Tip = int(Tip)
Num_people = int(Num_people)

calc = ((Total_bill+(Total_bill*Tip/100))/Num_people)
calc = round(calc,2)
print(f"Each person should pay: ${calc}")
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇