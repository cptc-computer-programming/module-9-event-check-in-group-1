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
# Function name:
# Purpose:
# Parameters:
# Returns:
# Possible return values:
# Assumptions:
# Example call:
# Example result:
# Who might use this function?
#
# Data contract template for Function 2:
# Function name:
# Purpose:
# Parameters:
# Returns:
# Possible return values:
# Assumptions:
# Example call:
# Example result:
# Who might use this function?
#
# TODO: After approval, write your two function definitions below.
def ticket_rate(is_student, is_veteran, has_priority, age):
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

