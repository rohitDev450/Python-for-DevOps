import re

text = "This python find for DevOps"
pattern = r"DevOps"

search = re.search(pattern, text)
if search:
    print("Pattern Found: ")
else:
    print("Pattern Not Found !") 