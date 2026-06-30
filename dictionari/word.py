text=input("enter a sentence to count word:")
word=text.split()
wc={}
for i in word:
    if i in wc:
        wc[i]+=1
    else:
        wc[i]=1
print(wc)