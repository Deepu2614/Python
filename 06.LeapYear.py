year = int(input("Enter a Year:"))
if (year % 400 == 0 and year % 100 == 0):
    print("Leap Year")
elif ((year % 4 == 0 and year % 100 != 0)):
    print("Leap Year")
else:
    print("Not a Leap Year")


# Default function to implement conditions to check leap year
def CheckLeap(Year):
  # Checking if the given year is leap year
  if((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Given Year is a leap Year");
  # Else it is not a leap year
  else:
    print ("Given Year is not a leap Year")
# Taking an input year from user
Year = int(input("Enter the number: "))
# Printing result
CheckLeap(Year)

print("\n\n By Deepak")