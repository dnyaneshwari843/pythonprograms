#print even number from 2 to n
def even(num):
    i=2
    while i<=num:
        if i%2==0:
          print("even number=",i,end=" ")
          break
        else:
           print("odd number=",i,end=" ")
        
        i+=1
even(30)