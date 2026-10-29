# Making a list of enquiries, each a dictionary with name, message and category

enquiries = [
    {"name": "Vivian", "message": "Are you available for business today?", "category": "support"},
    {"name": "Amarachi","message": "Do you operate on Sundays?", "category": "support"},
    {"name": "Aardbei", "message": "What is your social media handle?", "category": "General"},
    {"name": "Meisje", "message": "How much do you charge?", "category": "sales"},
    ]

# Print out the enquiries in the dictionaries.
for enquiry in enquiries:
    print(enquiry)
    print(f"{enquiry["name"]} asked: {enquiry["message"]} (Category: {enquiry["category"]})")  # Print the enquiries in one statement. One enquiry per sentence.