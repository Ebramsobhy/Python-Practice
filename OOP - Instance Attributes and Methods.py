class Member:
    def __init__(self, first_name, middle_name, last_name, gender) : 
       
       self.fName = first_name
       self.mName = middle_name
       self.lName = last_name
       self.gender = gender
    
    def full_name(self) :
        return f"{self.fName} {self.mName} {self.lName}"
    
    def name_with_title(self) :
        if self.gender == "Male":
           return f"Hello Mr {self.fName}"
        else :
           return f"Hello Miss {self.fName}"
    
    def get_all_info(self) :
        return f"{self.name_with_title()}, Your Full Name is: {self.full_name()}"
    
member_one = Member("Ebram", "Sobhy", "Isaac", "Male")   
member_two = Member("Osama", "Mohamed", "Kamal", "Male")   
member_three = Member("Mona", "Mohammed", "Ali", "Female") 

print(member_three.get_all_info())

