remove=lambda s: ''.join(c for c in s if c.lower() not in 'aeiou')
print(remove("hello world"))