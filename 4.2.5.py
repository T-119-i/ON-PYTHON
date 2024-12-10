s=input()
chu_hoa=0
chu_thuong=0
chu_so=0
for char in s:
    if char.isupper():
        chu_hoa+=1
    elif char.islower():
        chu_thuong+=1
    elif char.isdigit():
        chu_so+=1
print("Chu hoa:",chu_hoa)
print("Chu thuong:",chu_thuong)
print("Chu so:",chu_so)