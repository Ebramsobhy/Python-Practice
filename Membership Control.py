# Practical Membership Control

admins = ["Ebram", "Sameh", "Osama", "Enas"]
name = input("Write Your Name: ").strip().capitalize()

if name in admins:
    print("You Are Admin")
    option = input("Choose Update or Delete ").strip().capitalize()
    if option == "Update":
        newName = input("Write New Name ")
        admins[admins.index(name)] = newName
        print("Name Updated")

    elif option == "Delete":
        admins.remove(name)
    else:
        print("Invalid Option")
else:
    status = input("Not Admin, Do You Want Became Admin? Y , N ").strip().capitalize()
    if status == "Y" :
        admins.append(name)
    else:
        print("Okay, You Not added")    
