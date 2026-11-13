# Week 1: Enquiry Router

## Problem
Businesses receive enquiries that need to reach the right team. This workflow
takes incoming enquiries and routes each one to Sales, Support or General,
and flags anything with a missing or unrecognised category instead of losing it.
A Python script (`switch_node.ipynb`) applies the same routing logic.

## How it works
<img width="930" height="414" alt="image" src="https://github.com/user-attachments/assets/d96d32a7-01b5-4322-9c51-84a7f243fbac" />

1. **Manual Trigger:** starts the workflow when I click Execute.
2. **Code node:** creates 10 sample enquiries (name, message, category).
3. **Edit Fields:** trims extra spaces from `category` so "sales " matches "sales".
4. **Switch:** routes each enquiry to one of five outputs:
   - Sales, Support, General (matching rules, case ignored)
   - Missing Category (empty or absent category)
   - Unknown (fallback for anything unrecognised, such as typos)

## Result
10 enquiries in, 10 out: Sales 3, Support 4, General 3 (adjust to your
final counts, including any test cases). I check that the output counts add
up to the input after every change.
<img width="950" height="434" alt="image" src="https://github.com/user-attachments/assets/9bdc43e9-1420-460a-bc18-7d40b4f64936" />


## What broke (and how I fixed it)
- **Enquiries silently disappeared.** With no fallback, items with a missing
  category matched no rule and vanished. Fix: added a fallback output and a
  Missing Category rule.
- **"sales " with a trailing space went to Unknown.** Exact matching counts
  spaces. Fix: added an Edit Fields node to trim the value before routing.
- **"Sales" went to Unknown.** Matching is case-sensitive. Fix: turned on
  Ignore Case in the Switch.

## Run it
Import `router.json` into n8n and click Execute workflow.
Python: `switch_node.ipynb`

## Files
- `router.json`: workflow export
- `switch_node.ipynb`: Python version
- Demo: https://www.loom.com/share/cc2c6416a8664f2b8120bc04af8bd0a7

## Week 1 checkpoint
- **Trigger:** what starts a workflow, such as a manual click, a schedule,
  a form submission or a webhook.
- **Node:** one building block of a workflow, doing one job (trigger,
  transform data, make a decision, send a message).
- **Routing:** sending each item down a different output branch based on
  conditions, such as its category.


## What Broke in Python (and how I fixed it)
I made some mistakes earlier while trying to write a python function to return the category of enquiries and specify them as "unknown" if missing. Below are the errors and how I finally got to fix them:

1. printed the get_category instead of return
Observed Behaviour: The function showed values on screen, but nothing else in the code could use them.
Cause: I used print instead of return, and looped over the whole list inside the function.
Fix: The function takes one enquiry and returns its category. The loop sits outside it.
Lesson: A function should do one job and hand back a value.

2. Missing field check could never trigger
Observed Behaviour: The "unknown" branch never ran.
Cause: I compared a whole dictionary to an empty string (i != ""), which is always true.
Fix: Check for the key instead: if "category" in enquiry, or use enquiry.get("category", "unknown").
Lesson: “Missing field” means a missing key, not an empty dictionary.

3. Quotes inside f-strings
Observed Behaviour: None on my machine, but it can fail on older Python versions.
Cause: Double quotes inside a double-quoted f-string only work on Python 3.12+, according to my research.
Fix: Use single quotes inside: f"{enquiry['name']}". Learning to do this consciously.
Lesson: Write code that runs everywhere, not only on my machine.
