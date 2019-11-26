a=['a','e','i','o','u']
n=input()
n=list(n)
vowel=0
con=0
for i in range(0,len(n)):
    if(n[i] in a):
        vowel+=1
    else:
        con+=1
   
print(vowel,con)