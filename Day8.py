 from datetime import datetime,date


 tdate = datetime.today().date()
 dob = date(2007,1,26)

 years = tdate.year-dob.year

 print(years)