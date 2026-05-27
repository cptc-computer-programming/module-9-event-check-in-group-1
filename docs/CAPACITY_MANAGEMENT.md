# Capacity Management

## Your Assignment

Your team must create **two functions**:

- One function calculates and returns the numeric percentage of event capacity
  currently in use.
- One function decides and returns whether the entire arriving reservation is
  allowed to check in.

You decide the function names and the parameters needed for each function.

## Required Shared Outputs

- A numeric percentage showing how much capacity is currently used.
- A boolean decision stating whether the full reservation can check in.

## Available Inputs

The starting app has the number of guests already checked in, the event's maximum capacity, and the number of guests in the arriving reservation.

## Business Rules

- Capacity percentage describes event occupancy **before** the arriving
  reservation is added.
- Capacity percent is `guests already checked in / maximum capacity * 100`.
- The reservation checks in together. Do not allow part of the reservation to
  enter.
- A reservation can check in only when the guests already checked in plus the
  arriving reservation size is less than or equal to maximum capacity.
- If maximum capacity is `0` or less, capacity percent is `0` and the
  reservation cannot check in.

## Who Uses Your Outputs?

The Final Check-In Decision team needs the boolean check-in permission.
`app.py` will display both current occupancy and whether the reservation may
enter.

## Examples To Discuss

```text
75 guests checked in out of 100 -> 75.0 percent currently used
0 guests checked in out of 100 -> 0.0 percent currently used
95 checked in and a four-person reservation with capacity 100 -> True
95 checked in and a six-person reservation with capacity 100 -> False
Any arriving reservation when capacity is 0 -> False
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
