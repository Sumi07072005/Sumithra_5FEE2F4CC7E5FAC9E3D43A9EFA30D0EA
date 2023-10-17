Certainly! Here's a Python program that determines whether a year is a leap year or not using if-elif-else statements:

```python
# Get the year input from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
```

