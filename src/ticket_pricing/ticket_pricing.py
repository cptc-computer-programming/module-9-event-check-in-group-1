"""Ticket Pricing.

This module is your team's workspace for ticket-rate and reservation-subtotal work.
"""

# Your job:
# Design two functions that produce the required shared outputs described in
# docs/TICKET_PRICING.md.
#
# Before coding:
# 1. Read the business rules and target examples in your team brief.
# 2. Decide on one clear job for each of your two functions.
# 3. Write a data contract for each function.
# 4. Check your shared outputs with the teams that need them.
# 5. Get instructor approval for both contracts.
#
# Data contract template for Function 1:
# Function name: ticket_rate
# Purpose: determine price per person
# Parameters: is_stuednt, is_veteran, age
# Returns: per_person_rate
# Possible return values: 20,8,10,12,14
# Assumptions:
# Example call: ticket_rate(true, true, 11)
# Example result: 8.00
# Who might use this function?
#
# Data contract template for Function 2:
# Function name: calculate_subtotal
# Purpose: calculates the subtotal for reservation using the ticket_rate and total_guests
# Parameters: ticket_rate, total_guests
# Returns: float subtotal
# Possible return values: any positive float value
# Assumptions: n/a?
# Example call: calculate_subtotal(20.00, 4)
# Example result: 80.00
# Who might use this function? Discounts and fees group, final check in group.
#
# TODO: After approval, write your two function definitions below.
def ticket_rate(is_student, is_veteran, age):
    per_person_rate = 20.00
    if age <= 12:
        per_person_rate = 8.00
    elif age >= 65:
        per_person_rate = 10.00
    elif is_student:
        per_person_rate = 12.00
    elif is_veteran:
        per_person_rate = 14.00
    return((per_person_rate))

def calculate_subtotal(per_person_rate, reservation_size):
    subtotal = 0.00
    for _ in range(reservation_size):
        subtotal += float(per_person_rate)
    return(subtotal)