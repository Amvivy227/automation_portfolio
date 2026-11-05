# Week 1

### Workflows

The goal is to build an enquiry router in n8n that sends each enquiry to the right category and  a corresponding python code build-up.

#### Python
Made some mistakes earlier while trying to write a python function to return the category of enquiries and specify them as "unknown" if missing. Below are the errors and how I finally got to fix them:

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
