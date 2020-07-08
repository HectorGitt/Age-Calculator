# This is an age calculator
from datetime import date, time, datetime
today = str(datetime.today())
OriYear = int(today[:4])
OriMonth = int(today[5:7])
OriDay = int(today[8:10])
MonthDict = {"01" : "January", "02" : "February", "03" : "March", "04" : "April", "05" : "May", "06": "June", "07" : "July", "08" : "August", "09" : "September", "10" : "October", "11" : "November", "12" : "December"}
print("This Little software helps to calculate your age")
Cont = input("Do you want to continue? (Yes/No) ")
Cont2 = Cont.upper()
while Cont2 == ("YES"):
    Year = int(input("Enter the Year(YYYY): "))
    while (not (len(str(Year))) == 4) and Cont2 == "YES":
        print("Invalid year format, Write in (YYYY)")
        Cont = input("Do you want to continue? (Yes/No) ")
        Cont2 = Cont.upper()
        if Cont2 == "YES":
            Year = int(input("Enter the Year(YYYY): "))
    if not (len(str(Year))) == 4:          
        continue
    Mont = (input("Enter the Month(MM): "))
    while not len(str(Mont)) == 2 and Cont2 == "YES":
        print("Invalid Month format, Write in (MM)")
        Cont = input("Do you want to continue? (Yes/No) ")
        Cont2 = Cont.upper()
        if Cont2 == "YES":
            Mont = (input("Enter the Month(MM): "))
    if not (len(str(Mont))) ==2:
        continue
    Da = (input("Enter the day(DD): "))
    while (not (len(str(Da))) == 2) and Cont2 == "YES":
        print("Invalid day format, Write in (DD)")
        Cont = input("Do you want to continue? (Yes/No) ")
        if Cont2 == "YES":
            Da = (input("Enter the day(DD): "))
    if not (len(str(Da))) == 2:
        continue
    Month = int(Mont)
    Day = int(Da)
    AgeYear = OriYear - Year
    if AgeYear < 0:
        print("You dont exist yet")
        Cont = input("Do you want to start again? (Yes/No) ")
        Cont2 = Cont.upper()
    else:
        if Month > OriMonth:
            if Day > OriDay:
                OriAgeYear = AgeYear - 1
                print("You are ", OriAgeYear, "Years Old")
            else:
                OriAgeYear = AgeYear - 1
                print("You are ", OriAgeYear, "Years Old")
        elif Month == OriMonth:
            if Day > OriDay:
                OriAgeYear = AgeYear - 1
                print("You are ", OriAgeYear, "Years Old")
            if Day < OriDay :
                OriAgeYear = AgeYear
                print("You are ", OriAgeYear, "Years Old")
            if Day == OriDay:
                print("You are ", OriAgeYear, "Years Old")
                print("Happy Birthday Human")
        else:
            OriAgeYear = AgeYear
            print("You are ", OriAgeYear, "Years Old")
        Cont = input("Do you want to start again? (Yes/No) ")
        Cont2 = Cont.upper()