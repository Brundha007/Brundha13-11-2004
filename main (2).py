1# puthyon program  yo check if year is leap year or not
year =int (input('Enter year:'))

if (year%4==0and year%100 !=0)or(year%400==0):
  print(year,"is a leap year.")
else :
  print(year,"is not a leap year.")