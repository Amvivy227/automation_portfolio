# Build Log - AI & Automation

Documenting my Python knowledge in public and building my first automation projects here.

## Week 1 - Workflows

### Day 1: creating a Customer enquiry with Python and building my first workflow on n8n
<img width="960" height="477" alt="image" src="https://github.com/user-attachments/assets/4fe60795-7a85-44f1-aa75-200e685402a1" />


### Day 2: Creating a simple workflow manually triggered.

This workflow consists of 3 nodes;
- A manual trigger
- Code node
- Edit field

It is a manually triggered workflow, it doesn't start automatically nor does it rely on a schedule, so everytime you want to get the workflow started, you have to click on the manual trigger node (or we can call it a button in this case).
The second node picks up the enquiry data as it is as a json data and the Edit field node is used to cleanup the data to the format that we require them to be in, retaining only what we need.

<img width="958" height="470" alt="image" src="https://github.com/user-attachments/assets/ca2c6b32-8ca6-4b1d-b227-93b10ea31e31" />

<img width="958" height="438" alt="image" src="https://github.com/user-attachments/assets/f725c8e2-d676-47fc-9bf0-28685cb68042" />


<img width="958" height="444" alt="image" src="https://github.com/user-attachments/assets/f8a7d68f-d37e-4587-8f84-ad7128f2ad9c" />


### Day 3: Adding Decisions with IF node

Today, I added an IF node to the already existing customer enquiry workflow. The IF node is used to carry out a decision (or condition check as I love to call it) check. The aim is to separate the sales enquiry from the other categories of enquiries that exists in our log.
It is worth noting that the IF node on n8n workflow is case-sensitive, but I was able to overcome this by making sure that my strings were all in lowercase. You can also turn on the "ignore case" option on the IF node's Parameters page.


#### Results

1.  A python code demonstration of using the IF statement to retrieve only the enquiries in the Sales category
<img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/a26b968a-4ee9-4ecf-be01-a1e0314f7441" />


2. The True Branch of the IF node on my n8n workflow. You can see that only one item meets the decision/condition of being in the "sales" category.
<img width="954" height="443" alt="image" src="https://github.com/user-attachments/assets/134c0778-e287-4b28-921e-20bc73bbaefd" />


3. The False Branch of the IF node. The output consists of 3 items that did not meet the condition. 
<img width="937" height="464" alt="image" src="https://github.com/user-attachments/assets/b5c906c2-3412-4bbd-a978-8474d3c686ee" />


### Day 4 - Switch Node

*Replaced the IF node with a switch node.*

Using the switch node, I was able to split the enquiries data into multiple paths based on different conditions. Unlike the IF node that only has 2 outputs of True or False, the Switch node can have multiple outputs, making it easier to manage several categories in one place. 
Lastly, the Switch node has a behaviour similar to an IF, ELIF, ELSE construct. Except it is better structured.

<img width="954" height="448" alt="image" src="https://github.com/user-attachments/assets/0cc8095f-710c-4319-b44f-d0efba426ad5" />

<img width="959" height="450" alt="image" src="https://github.com/user-attachments/assets/5fd21228-8419-4662-93c1-0c4a7438e8b6" />

<img width="944" height="445" alt="image" src="https://github.com/user-attachments/assets/92679e97-a057-4d4d-be20-80f1f40248e8" />

<img width="960" height="446" alt="image" src="https://github.com/user-attachments/assets/746edfd6-2564-4a10-bbaf-c2514c45a53f" />

*That leads us to my favorite part: A Python script that prints a different message for sales, support, and general, using the if/elif/else statements*

<img width="907" height="452" alt="image" src="https://github.com/user-attachments/assets/af655584-c3fc-484a-9edd-3c2e222941cc" />


### Day 5: Failures and Fixes themed "Break it on Purpose and Fix it"

Today, I carried out different tests to see how the switch node outputs hold up with categorizing and routing data. From leaving fields empty, removing key:value pairs entirely, mispelling categories, adding trailing whitespaces, to changing casing and adding unexpected categories. Then, I observed closely for fallthroughs and added fallbacks to cater to these failures.

Setup: 10 sample enquiries going into a Switch node with 3 rules (Sales, Support, General). Rule 4 (Missing Category) and a fallback output (Unknown) were added during testing. Rule: the total across all outputs must equal the number of items going in.

#### n8n workflow
<img width="922" height="396" alt="image" src="https://github.com/user-attachments/assets/00ddeb67-4194-4b48-a9e2-981d81c937ce" />


<img width="957" height="444" alt="image" src="https://github.com/user-attachments/assets/8c391075-f5c8-4bd8-b605-4fdb5b9a48d8" />

1. Missing key and empty value silently dropped
Observed Behaviour: The General output went from 3 items to 2, with no error.
Cause: One enquiry had an empty category and another had no category key. The Switch had no rule for them, so they matched nothing and were discarded.
Fix: Enabled the fallback output, and added Rule 4 ({{ $json.category }} is equal to an empty value), renamed “Missing Category”. It now catches both the missing key and the empty string (confirmed: 2 items landed there).
Lesson: Without a fallback, bad data disappears silently. Always check that output counts add up to the input count.
<img width="921" height="409" alt="image" src="https://github.com/user-attachments/assets/daf64234-0868-4c9e-9050-03dfde895a3b" />


2. Unexpected category ("technical")
Observed Behaviour: None. The test passed.
Cause: The category isn’t one of the three defined routes.
Fix: No new fix needed. The fallback output (renamed “Unknown”) caught it.
Lesson: A category I didn’t plan for gets routed to a human instead of lost.
<img width="940" height="443" alt="image" src="https://github.com/user-attachments/assets/e5be3b00-b87b-4556-b7e6-1f33900275ff" />


3. Misspelled categories
Observed Behaviour: None. The test passed.
Cause: The Switch compares strings exactly, so a misspelling doesn’t match any rule.
Fix: No new fix needed. The items landed in Unknown.
Lesson: The workflow catches misspellings but doesn’t correct them, which is deliberate. Sending them over for human verification.

4. Title case categories sent to Unknown
Observed Behaviour: Values like "Sales" landed in the fallback output.
Cause: String comparison is case-sensitive by default.
Fix: Turned on the Ignore Case option in the Switch node.
Lesson: Casing differences are common in real data. Handle them before or inside routing.

5. Trailing whitespace sent to Unknown
Observed Behaviour: "sales " (with a trailing space) landed in Unknown.
Cause: Spaces count in an exact comparison, and Ignore Case doesn’t remove them.
Fix: Added an Edit Fields node before the Switch (Manual Mapping, field category, with the “Include Other Input Fields” option on) using {{ ($json.category || "").toString().trim() }}.
Lesson: Clean the data first, then route it. Ignore Case still handles capitalisation.
<img width="923" height="402" alt="image" src="https://github.com/user-attachments/assets/78ec0cc0-0e84-4276-90f0-61d9fca25e83" />


#### Python
Wrote a function get_category(enquiry) that returns the category of an enquiry, or returns "unknown" if the field is missing.

<img width="889" height="448" alt="image" src="https://github.com/user-attachments/assets/28550b53-4dec-4181-9fb4-da9f0e6fe2df" />

