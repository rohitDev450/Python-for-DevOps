import re

text = "This my red color"
pattern = r"red"

replace = "green"

rep = re.sub(pattern, replace, text)
print("Replace successfully :", rep)