enquiries = [
    {"name": "Vivian", "message": "Are you available for business today?", "category": "support"},
    {"name": "Amarachi","message": "Do you operate on Sundays?", "category": "support"},
    {"name": "Aardbei", "message": "What is your social media handle?", "category": "general"},
    {"name": "Meisje", "message": "How much do you charge?", "category": "sales"},
    {"name": "Tunde", "message": "Can I get a quote for 50 branded notebooks?", "category": "sales" },
    { "name": "Chioma", "message": "My order arrived damaged. What should I do?", "category": "support" },
    { "name": "Ibrahim", "message": "Where is your office located?", "category": "general" },
    { "name": "Folake", "message": "Do you offer discounts for bulk purchases?", "category": "sales" },
    { "name": "Emeka", "message": "I was charged twice for my last payment.", },
    { "name": "Zainab", "message": "Do you have a newsletter I can subscribe to?", "category": "" }
]


def get_category(enquiry):
    """Return the category of an enquiry from the list of enquiries,
    and return 'unknown' if the key 'category' is missing or the key has an empty value field"""
    category = enquiry.get("category", "").strip().lower()
    if category == "":
        return "unknown"
    return category

    
for enquiry in enquiries:
    print(get_category(enquiry))