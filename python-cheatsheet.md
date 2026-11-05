### Here I would be building a personal cheat sheet for Python, recording the syntaxes I forget, with a tiny example.


1. Python Break Statement: The break statement is used to exit a loop immediately without running any remaining code in the loop, regardless of the results of any conditional tests.
   Example:
```
for i in range(10):
  if i == 5:
    break
  print(i)
```
*Here, the loop is ended immediately i equals 5, terminating the remaining iterations.*

2. Return vs print: return hands a value back, print only displays it
```
def get_category(enquiry):
    return enquiry.get("category", "unknown")
```

3. .get(key, default): safe lookup in a dictionary, no KeyError if the key is missing
```
enquiry.get("category", "unknown")
```

4. Check if a key exists
```
if "category" in enquiry:
```

5. f-strings: use different quotes inside
```
f"Hello {enquiry['name']}"
```
