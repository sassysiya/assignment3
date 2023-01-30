day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
if 1 <= month <= 12 and 1 <= day <= 31 and 1800 <= year <= 2025:
    list1 = [1,3,5,7,8,10,12]
    if month in list1:
        day = day + 1
        print ("Next date is:{day}/0{month}/{year}".format(day = day, month = month, year = year))
        month = month+1
    list3 = [4,6,11]
    if month in list3:
        if 1 <= month <= 30:
            day = day + 1
            print ("Next date is:{day}/0{month}/{year}".format(day = day, month = month, year = year))
            month = month + 1
        else:
            print ("error")
    if month == 2:
        if year % 4:
            if 1 <= day <= 29:
                day = day + 1
                print("Next date is:{day}/0{month}/{year}".format(day = day, month = month, year = year))
            else:
                print ("error")
        else:
            if 1 <= day <= 28:
                day = day + 1
                print("Next date is:{day}/0{month}/{year}".format(day = day, month = month, year = year))
            else:
                print ("error")
    else:
        print ("error")
else:
    print ("error")
