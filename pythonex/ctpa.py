#enter marks of 5 subject and calculate total,average and percentage
sub1=int(input("enter marks of 1st subject"))
sub2=int(input("enter marks of 2nd subject"))
sub3=int(input("enter marks of 3rd subject"))
sub4=int(input("enter marks of 4th subject"))
sub5=int(input("enter marks of 5th subject"))
total=sub1+sub2+sub3+sub4+sub5
print("total marks :",total)
avg=total/5
print('average is',avg)
per=total/500*100
print("percentage is",per)