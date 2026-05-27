# Discounts and Fees

## Your Assignment

Your team must create **two functions**:

- One function calculates and returns the numeric discount amount for the
  reservation.
- One function calculates and returns the numeric service fee amount for the
  reservation.

You decide the function names and the parameters needed for each function.

## Required Shared Outputs

- A numeric reservation discount amount.
- A numeric service fee amount.

## Available Inputs

The Ticket Pricing team will produce the reservation subtotal. The starting app
also has the number of guests in the reservation and whether registration was
completed online.

## Business Rules

- Reservations of 10 or more guests receive a discount equal to 15% of the
  original subtotal.
- Reservations of 5 through 9 guests receive a discount equal to 10% of the
  original subtotal.
- Reservations of fewer than 5 guests receive no discount.
- Online registration adds a service fee equal to 5% of the original subtotal.
- In-person registration adds no service fee.
- Calculate both the discount and service fee from the original subtotal. Do
  not subtract the discount before calculating the service fee.

## Who Uses Your Outputs?

The Final Check-In Decision team needs both amounts to calculate the quoted
final amount. `app.py` will also display them in the operations summary.

## Examples To Discuss

```text
A ten-person reservation with a 200.00 subtotal -> 30.00 discount
A six-person reservation with a 120.00 subtotal -> 12.00 discount
A three-person reservation with a 60.00 subtotal -> 0.00 discount
A 100.00 subtotal registered online -> 5.00 service fee
A 100.00 subtotal registered in person -> 0.00 service fee
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
