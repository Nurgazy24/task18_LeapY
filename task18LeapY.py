def checkYear(year): 
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)); 
  

year = 2020
if(checkYear(year)): 
    print("Високосный год") 
else: 
    print("Не високосный год") 