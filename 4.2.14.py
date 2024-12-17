#sap xep xau
import re
s = input().strip()
numbers = re.findall(r'\d+', s)
numbers = [int(num) for num in numbers]
numbers.sort()
result = []
number_index = 0
i = 0
while i < len(s):
    if s[i].isdigit():
        number = ''
        while i < len(s) and s[i].isdigit():
            number += s[i]
            i += 1
        result.append(str(numbers[number_index]))
        number_index += 1
    else:
        result.append(s[i])
        i += 1
print(''.join(result))