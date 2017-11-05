#!/usr/bin/env python

amount = float(input("How much did you deposit:"))
interest_rate = 0.04
first_year_interest = (amount * 0.04) + amount
second_year_interest = (first_year_interest * 0.04) + first_year_interest
third_year_interest = (second_year_interest * 0.04) + second_year_interest

print(f"""
Account Statement
#################################
1st Year:${first_year_interest}
2nd Year: ${second_year_interest}
3rd Year: ${third_year_interest}
""")





