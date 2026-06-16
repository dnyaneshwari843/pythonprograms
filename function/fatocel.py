def fartocel(far):
    cel=(far-32)*5/9
    print(f"{far}f={cel}c")
far=float(input("enter temperature:"))
fartocel(far)