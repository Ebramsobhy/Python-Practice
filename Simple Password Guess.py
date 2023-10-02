# Loop while training

# Simple Password Guess
main_password = "Hero@1237"
input_password = input("Write Password: ").strip()
tries = 4

while input_password != main_password :
    tries -= 1
    print(f"Wrong Password, {'Last' if tries == 0 else tries} tries left")
    input_password = input("Write Password: ").strip()
    
    if tries == 0:
        break
else:
    print("Correct Password")   

