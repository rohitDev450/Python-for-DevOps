import re

text = "This split function / u can use anyever"
pattern = r"/"

sp = re.split(pattern, text)
print("The text is split : ", sp)