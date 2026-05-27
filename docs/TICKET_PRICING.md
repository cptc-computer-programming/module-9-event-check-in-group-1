# Ticket Pricing

## Your Assignment

Your team must create **two functions**:

- One function determines and returns the numeric per-person ticket rate for
  the reservation.
- One function calculates and returns the numeric ticket subtotal for the
  whole reservation.

You decide the function names and the parameters needed for each function.

## Required Shared Outputs

- A numeric per-person ticket rate for the reservation.
- A numeric reservation ticket subtotal before discounts or fees.

## Available Inputs

The starting app has the reservation holder's age, student status, veteran
status, and the number of guests in the reservation.

## Business Rules

- The reservation holder's eligibility determines the ticket rate used for
  every guest in this reservation.
- Child: age 12 or younger costs `8.00`.
- Senior: age 65 or older costs `10.00`.
- Student: student status of `True` costs `12.00`.
- Veteran: veteran status of `True` costs `14.00`.
- General: everyone else costs `20.00`.
- If the reservation holder qualifies for more than one rate, use the least
  expensive eligible rate.
- The reservation subtotal is the number of guests multiplied by the
  per-person ticket rate.
- To practice repetition, use a loop: start a total at `0` and add one ticket
  rate for each guest in the reservation.

## Who Uses Your Outputs?

The Discounts and Fees team needs the subtotal. The Final Check-In Decision
team and `app.py` also need the money calculations produced from your work.

## Examples To Discuss

```text
A reservation holder age 10 -> 8.00 per person
A reservation holder age 70 who is also a student -> 10.00 per person
A student reservation holder age 20 -> 12.00 per person
A veteran reservation holder age 40 -> 14.00 per person
A general reservation holder age 35 -> 20.00 per person
A four-person reservation at 12.00 each -> 48.00 subtotal
```

## Create Two Data Contracts

You must create **two data contracts** before writing function code. Decide
your function names, parameters, and return values, post the contracts for the
class, and get approval before coding.

```text
Function name:
Purpose:
Parameters:
Returns:
Possible return values:
Assumptions:
Example call:
Example result:
Who might use this function?
```
