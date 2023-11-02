i = 0
aptnum = 0
list1 = ["Yes", "yes", "y","Y"]
("Contacts.csv")
print("During this process, you may leave any part of the contact blank.")
with open("Contacts.csv", 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    wr.writerow(["Contact Name", "Name", "Age", "Address", "Contact Method", "Contact", "Additional Contact Information", "Additional Information"])
while True:
    contname = ""
    name = ""
    age = ""
    address = ""
    contact = ""
    continfo = ""
    addcont = ""
    add = ""
    contname = input("Please enter the string you would like to use to find this contact: ")
    name = input("Please enter the full name: ")
    age = input("Please enter the age: ")
    address = input("Please enter the full address: ")
    contact = input("Please enter a form of contacting the person: ")
    if contact == "":
        contact = "Unknown"
        continfo = "Unknown"
        addcont = "Unknown"
    else:
        continfo = input("Please enter the contact: ")
        addcont = input("Please enter additional information about the contact: ")
    add = input("Please enter additional information: ")
    print("Processing...")
    if contname == "":
        contname = "Unknown"
    if name == "":
        name = "Unknown"
    if age == "":
        age = "Unknown"
    if address == "":
        address = "Unknown"
    if add == "":
        add = "Unknown"
    with open("Contacts.csv", 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        wr.writerow([contname, name, age, address, contact, continfo, addcont, add])
    go = input("Would you like to add another contact? ")
    if go in list1:
        continue
    else:
        break
while True:
    go = input("Would you like to view a contact? ")
    if go in list1:
        pass
    else:
        break
    print("The following values are the contact names that have been listed.")
    f = csv.reader(open("Contacts.csv", "r"))
    for row in f:
        list.append(row[0])
    print(list)
    while True:
        go = input("Which contact would you like to view? ")
        if not go in list:
            print("The value was not in the list of contacts. Please try again.")
            continue
        else:
            for i in list:
                if go == i:
                    
                
while True:
    go = input("Would you like to edit a contact? ")
    if go in list1:
        pass
    else:
        break
    print("The following words are the contact names that have been listed.")
    
    

