def temp(temp):
    """_summary_

    Args:
        temp (_type_): _description_
    """
    if(temp>40):
        print("you are sick because your temp was %d"%temp)
        # python don't have && and || it was and / or
    elif(temp<40 and temp >36):
        print("you are nice your temp is %d",temp)
    else:
        print("go to see the doctor bro because your are %d",temp)
temp(100)
temp(2)
temp(37)