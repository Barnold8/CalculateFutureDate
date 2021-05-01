#This is a program that calculates the time from the current date to a given date
#Leap year is a year that is divisible by 4 and not years that are in the hundreds unless it is divisible by 400
import datetime

Date = datetime.datetime.now() #Variable to access current Month and year]

Leap_Year = 29 if Date.year % 4 == 0 or Date.year % 400 == 0 else 28

Month_Set = []

for i in range(12):

  if i < 7:                              
    Month_Set.append(31 if i % 2 == 0 else 30 )##Code that generates the months in a year - Their numbers, avoids hard coding
  else:                                        ##Just realised that datetime has a variable called day which gives the number day. I made this code before noticing this, it may be more useful for me later anyway
    Month_Set.append(30 if i % 2 == 0 else 31 )
    
Month_Set[1] = Leap_Year

Curr_Date = [Date.day,Date.month,Date.year]

CalcDate = input("Please input the date you wish to calculate in dd/mm/yyy, including the '/' ")
CalcDate = CalcDate.split('/')

for i in range(len(CalcDate)):

  CalcDate[i] = int(CalcDate[i])

New_year = CalcDate[2] - Curr_Date[2]
New_month = CalcDate[1] - Curr_Date[1] if CalcDate[1] >= Curr_Date[1] else 12 - abs(CalcDate[1] - Curr_Date[1])  
New_day =  CalcDate[0] - Curr_Date[0] if CalcDate[0] >= Curr_Date[0] else Month_Set[CalcDate[1]] - abs(CalcDate[0] - Curr_Date[0])


print(abs(CalcDate[1] - Curr_Date[1])  )
print(f"The date you chose: {CalcDate[0]}/{CalcDate[1]}/{CalcDate[2]}\nCurrent date: {Curr_Date[0]}/{Curr_Date[1]}/{Curr_Date[2]}\nTime till then: | {New_day} Day(s) | {New_month} Month(s) | {New_year} Year(s)")
