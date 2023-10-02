# Loop while training

# Empty List To Fill Later
myFavouriteWebs = []

# Maximum Allowed Websites 
maximumWebs = 5 

while maximumWebs > 0 :
    # Input The New Website
    web = input("Write your web name without https:// ").strip().lower()
    # Add The New Website To The List 
    myFavouriteWebs.append(f"https://{web}")
    maximumWebs -= 1
    print(f"Website Added, {maximumWebs} Places Left")

    print(myFavouriteWebs)
else:
    print("Bookmark Is Full, You Can't Add More") 

