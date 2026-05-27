# Event Check-In Operations Lab

## At a Glance

| Item | Details |
| --- | --- |
| **Teams** | 5 teams of 2 students |
| **Team task** | Design and implement 2 functions |
| **Main skills** | Functions, data contracts, calculations, decisions, and loops |
| **Class deliverable** | One integrated event check-in operations app |
| **Integration file** | `src/app.py` |
| **Testing file** | `tests/test_app.py` for whole-flow tests |

## Scenario

The app helps event staff check in one reservation by calculating its ticket cost, checking whether there is room for the full reservation, estimating the wait, and reporting the next action.


> [!NOTE]  
> Examples of group event check-in include school conferences, museum tours, community workshops, career fairs, festival sessions, or other events where one reservation covers several attendees checking in together.

For this lab, the reservation holder's eligibility determines the ticket rate used for everyone in the reservation. The reservation checks in together:
either everyone fits within capacity or check-in is denied.

The app calculates a quoted final amount even if check-in is denied. The final check-in status tells event staff whether to proceed with payment and entry.

## App Requirements

The app starts with information about:

- The reservation holder's age
- Whether the reservation holder is a student
- Whether the reservation holder is a veteran
- The number of guests in the reservation
- Whether registration was completed online
- The number of guests already checked in
- The event's maximum capacity
- The number of people ahead in line
- The estimated time to serve one person
- Whether the reservation holder has a priority pass

Using functions created by the teams, the app must:

- Determine a per-person ticket rate
- Calculate the reservation's ticket subtotal
- Calculate any reservation discount and service fee
- Determine how full the event is
- Decide whether the full reservation can check in
- Estimate the wait time
- Choose a check-in lane
- Calculate the quoted final amount
- Produce a final check-in status

The completed program should print an operations summary showing the important
results for event staff.

## Data Contracts

> [!IMPORTANT]  
> **Data contracts are public promises**: they tell other teams what inputs your function accepts and what value it returns.

In this lab, a function signature is one part of its data contract. The full
contract also explains what the returned value means, assumptions the function
makes, and behavior other teams can depend on.

For example, the ticket pricing file may return a subtotal that the discounts and fees file uses to calculate a discount. 


## Team Responsibilities

| Team Area | Required Shared Outputs |
| --- | --- |
| **Ticket Pricing** | Per-person ticket rate; reservation subtotal |
| **Discounts and Fees** | Discount amount; service fee |
| **Capacity Management** | Current capacity percentage; check-in permission |
| **Wait Time Estimator** | Wait minutes; check-in lane |
| **Final Check-In Decision** | Quoted final amount; final check-in status |

## Repository Layout

```text
README.md
docs/
    TICKET_PRICING.md
    DISCOUNTS_FEES.md
    CAPACITY_MANAGEMENT.md
    WAIT_TIME.md
    CHECKIN_DECISION.md
src/
    app.py
    ticket_pricing/
    discounts_fees/
    capacity_management/
    wait_time/
    checkin_decision/
tests/
    test_app.py               Whole-flow tests for class integration
```

## Lab Phases

### Roadmap

| Phase | What Happens | Deliverable |
| --- | --- | --- |
| **1. Map** | Build the app flowchart together | Shared flowchart |
| **2. Design** | Teams design two data contracts | Docstrings or empty stubs |
| **3. Review** | Representatives verify shared outputs | Approved contracts |
| **4. Build** | Teams implement their functions | Working team modules |
| **5. Integrate** | Run the provided tests and connect the app | Completed `app.py` |


### Phase 1: Understand the App Flow Together

As a class, **make a flowchart of the event check-in operations system**. 

Identify the information the app begins with, the broad logical steps it needs
to take to proceed, and which team owns which part.

### Phase 2: Design Team Data Contracts

Split into teams and read your brief in `docs/`. Each team designs the data
contracts for its **two functions**. Decide each function's name, parameters, return value, and expected behavior.

Record your approved proposal as docstrings or empty function stubs in your team file, then push those contract changes so the class can review them.

Do not write the complete function logic yet.

### Phase 3: Review the Data Flow

Each team sends one representative to the board. Together, compare the team
contracts to the class flowchart and decide whether the shared outputs line up:

- Does every function receive the data it needs?
- Does another team know how to use each shared output?
- Are any values missing, duplicated, or in the wrong order?

Revise contracts as needed. Once approved, the contracts freeze unless the
class agrees to a change.

### Phase 4: Implement Team Functions

Return to your teams and write the code for your two approved functions. Follow the contract exactly so other teams can rely on your outputs during integration. Push descriptive commits.

> [!WARNING]  
> Only edit files belonging to your team. Do not edit `app.py`. Push your changes frequently. Pull other teams' changes frequently.

### Phase 5: Integrate and Test as a Class

#### Whole-Flow Test Cases

Two whole-flow tests are provided in `tests/test_app.py`. They call one
app-level processing function so the entire flow can be checked without
simulating keyboard input. As a class, make these scenarios pass using the
approved team functions.

**Case 1: Student reservation can check in**

- A six-person reservation is checking in online.
- The reservation holder is a student.
- There is enough room for the reservation.
- The standard line has a short wait.

Test that student pricing, a reservation discount, an online fee, and a
successful payment-required check-in decision work together.

**Case 2: Senior reservation is denied for capacity**

- A ten-person reservation is checking in in person.
- The reservation holder qualifies for senior pricing.
- The event does not have room for the whole reservation.
- The line is crowded.

Test that the larger reservation discount, no online fee, priority lane choice,
and capacity denial work together.

The exact starting values and expected results are recorded in the provided
test file.

#### Building `app.py`

We will integrate as a class.

Students will lead integration using functions from a team other than their
own. Read that team's approved data contracts, add its imports and function
calls to `app.py`, and connect shared outputs to the next step in the flow.

`main()` collects reservation details from the user and prints the summary.
`process_reservation()` accepts those details as parameters, calls the team
functions, and returns results for `main()` and the tests to use.


## Function Rules

- Give each function one clear job.
- Use parameters to receive needed data.
- Return values for other code to use.
- Use `input()` only in `main()`; team functions receive data through parameters.
- Use `print()` only in `main()`; team functions return results.
- A contract freezes after approval. Discuss changes before editing it.

## Run the App

```bash
python src/app.py
```

## Run the Tests

During integration, run the provided whole-flow tests:

```bash
pytest
```
