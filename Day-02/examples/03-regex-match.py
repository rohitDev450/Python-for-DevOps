# import re 

# text = "This is match found in re package"
# pattern = r"found"

# match = re.match(pattern, text)
# if match:
#     print("Match Found :", pattern)
# else:
#     print("Match Not Found!")

import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")