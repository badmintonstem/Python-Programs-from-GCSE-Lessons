#Program to validate a date input.  Expected dd/mm/yyyy
while True:

    valid = False
    while not valid:
        date = input("Enter the DOB: ")
        valid = True

        #Presence check
        if len(date) == 0:
            print("Failed presence check (no data)")
            valid = False
            
        #Length check
        if len(date)!= 10:
            print("Failed length check (not 10 characters)")
            valid = False

        else:
            #Manipulate string to extract day, month, year
            day = date[0:2]
            month = date[3:5]
            year = date[6:]
            #Manipulate string to extract /
            divider1 = date[2:3]
            divider2 = date[5:6]

            #Format check
            if divider1 != "/" or divider2 != "/":
                print("Failed format check (not dd/mm/yyyy)")
                valid = False
            else:
                #Type checks
                if not day.isnumeric():
                    print("Failed type check on day number")
                    valid = False
                
                if not month.isnumeric():
                    print("Failed type check on month number")
                    valid = False
                
                if not year.isnumeric():
                    print("Failed type check on year number")
                    valid = False

                if day.isnumeric() and month.isnumeric() and year.isnumeric():

                    #Cast numbers to integers
                    day = int(day)
                    month = int(month)
                    year = int(year)

                    #Range checks
                    if day < 1:
                        print("Failed range check on day number (too small)")
                        valid = False

                    if month < 1:
                        print("Failed range check on month number (too small)")
                        valid = False

                    if month > 12:
                        print("Failed range check on month number (too large)")
                        valid = False
                
                    if year < 1900:
                        print("Failed range check on year number (too small)")
                        valid = False

                    if day > 29 and month == 2:
                        print("Failed range check on day number (too large)")
                        valid = False

                    if day > 30 and month in [2,4,6,9,11]:
                        print("Failed range check on day number (too large)")
                        valid = False

                    if day > 31 and month in [1,3,5,7,8,10,12]:
                        print("Failed range check on day number (too large)")
                        valid = False
                    
                    if day == 29 and month == 2 and year % 4 != 0:
                        print("Failed range check on day number (too large)")
                        valid = False

    print("Valid date entered.")
