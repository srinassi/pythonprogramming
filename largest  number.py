j=int(raw_input())
l=input().split()
l.sort()
su=0
a=len(l)
while(a>0):
        a=int(l[a-1])
        su=su*10+a
        a-=1
print(su)
