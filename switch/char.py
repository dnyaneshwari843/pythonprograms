def char():
    ch=(input("enter character from (a to z )to check it is vowel or consonent:"))
    match ch:
        case "A"|"E"|"I"|"O"|"U"|"a"|"e"|"i"|"o"|"u":
            print(f"{ch} is vowel" )
        case _:
            print(f"{ch} is consonent")
char()