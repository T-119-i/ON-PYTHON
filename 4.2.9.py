s=input()
so=s.split(',')
for i in so:
    i=i.strip()
    if i.isdigit() and int(i)%2!=0:
        print(i,end=' ')