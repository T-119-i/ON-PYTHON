s=input()
dem={}
for char in s:
    if char in dem:
        dem[char]+=1
    else:
        dem[char]=1
for char,count in dem.items():
    print("'{0}': {1}".format(char,count))