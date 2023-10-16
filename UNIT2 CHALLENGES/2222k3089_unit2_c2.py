# 2.Leap Year
def isLeapYear(year):
if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
return True
else:
return False
year = int(input(&quot;Enter a year : &quot;))
if isLeapYear(year):
print(&#39;{} is a leap year.&#39;.format(year))
else:
print(&#39;{} is not a leap year.&#39;.format(year))
