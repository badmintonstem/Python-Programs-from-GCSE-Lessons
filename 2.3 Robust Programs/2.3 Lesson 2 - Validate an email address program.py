#email address validation
valid = False
while not valid:
    valid = True
    address = input("Enter your email address: ")
    #Sanitise domain to lowercase
    address = address.lower()

    #Format check: must contain a @
    if "@" not in address:
        valid = False
        print("Invalid email address, no @ symbol")
    else:
        #Format check: double dots not permitted
        if ".." in address:
            valid = False
            print("Invalid email address, double dots not permitted")

        else:
            at_position = address.find("@")
            local_part = address[:at_position]
            domain = address[at_position+1:]

            #Dot cannot be the first or last character
            if local_part[0] == ".":
                valid = False
                print("Invalid email address, local part cannot start with a dot")
            if domain[0] == ".":
                valid = False
                print("Invalid email address, domain cannot start with a dot")

print("Valid address entered")
#Find more validation checks at: https://en.wikipedia.org/wiki/Email_address
