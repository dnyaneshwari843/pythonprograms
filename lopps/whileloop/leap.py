def leap(year):
    i=2001
    while i<=year:
        if i%4==0:
            print(f"{i}leap year")
        i+=1
leap(2026)