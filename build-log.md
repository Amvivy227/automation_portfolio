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

1.  A python code demonstration of using the IF statement to retrieve only the enquiries in the Sales category
<img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/a26b968a-4ee9-4ecf-be01-a1e0314f7441" />

2. The True Branch of the IF node on my n8n workflow. You can see that only one item meets the decision/condition of being in the "sales" category.
<img width="954" height="443" alt="image" src="https://github.com/user-attachments/assets/134c0778-e287-4b28-921e-20bc73bbaefd" />

3. The False Branch of the IF node. The output consists of 3 items that did not meet the condition. 
<img width="937" height="464" alt="image" src="https://github.com/user-attachments/assets/b5c906c2-3412-4bbd-a978-8474d3c686ee" />




