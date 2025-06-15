Age=int(input("Enter your Age:"))
if Age >= 18:
    print("you are eligible")
    Voter_id=input("Do you have voter_id:")
    if Voter_id=="Yes":
        print("you can vote")
    else:
        print("you can't vote")
else:
    print("you are not eligible")
