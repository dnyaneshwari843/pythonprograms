count=lambda s:sum(1 for c in s if c.isupper())
print(count("Hello world"))