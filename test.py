import datetime

a = datetime.datetime(2024, 9, 2, 13, 52, 16, 660000).strftime(r"%b %d, %Y")
b = datetime.datetime(2024, 9, 2, 13, 52, 16, 660000).strftime(r"%d %B %Y - %I:%M %p UTC").lstrip('0')
# b = datetime.datetime(2024, 9, 22, 13, 52, 16, 660000).strftime(r"%-d %B %Y - %I:%M %p UTC")
print(a)
print(b)

ab = {}

print( 'hello' not in ab)