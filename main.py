# SuperMarket.py - This program creates a report that lists weekly hours worked 
# by employees of a supermarket. The report lists total hours for 
# each day of one week. 
# Input:  Interactive
# Output: Report. 

# Declare variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "Day Total "
SENTINEL = "done"   # Named constant for sentinel value
hoursWorked = 0     # Current record hours
hoursTotal = 0      # Hours total for a day
prevDay = ""        # Previous day of week
notDone = True      # loop control

# Print two blank lines.
print("\n\n")
# Print heading.
print("\t" + HEAD1)
# Print two blank lines.
print("\n\n")

# Read first record 
dayOfWeek = input("Enter day of week or done to quit: ")
if dayOfWeek  == SENTINEL:
    notDone = False
else:
    hoursWorked = input("Enter hours worked: ")
    hoursTotal = hoursTotal + int(hoursWorked)
    prevDay = dayOfWeek

while notDone == True:
    # Implement control break logic here
    # Include work done in the dayChange() function
    if dayOfWeek  == SENTINEL:
      print("\t" + DAY_FOOTER + str(hoursTotal), "for", prevDay)
      notDone = False
    elif dayOfWeek == prevDay:
      dayOfWeek = input("Enter a day of week or done to quit: ")
      if dayOfWeek  == SENTINEL:
        print("\t" + DAY_FOOTER + str(hoursTotal), "for", prevDay)
        notDone = False
      elif dayOfWeek != prevDay:  
          print("\t" + DAY_FOOTER + str(hoursTotal), "for", prevDay)
          hoursTotal = 0
          prevDay = dayOfWeek
          hoursWorked = input("Enter hours worked: ")
          hoursTotal = hoursTotal + int(hoursWorked)
      else:
        hoursWorked = input("Enter hours worked: ")
        hoursTotal = hoursTotal + int(hoursWorked)
print("Thank you")