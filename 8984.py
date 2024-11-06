 
import re
expression = input()
operations = re.findall(r'\+|\-|\*{1,2}|\/{1,2}|%', expression)
print(len(operations))