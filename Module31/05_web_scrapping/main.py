import re

with open('examples.html', 'r') as file:
    text = file.read()

pattern = r'<h3>(.*?)</h3>'

result = re.findall(pattern, text)

print(result)
