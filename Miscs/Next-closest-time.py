def NextClosestTimme(time):

    """
        1. Get digits from given time
        2. Store unique digits from given time
        3. Store indexs of each digit from step-2

    """
    digits = [
        int(digit) for digit in time if digit.isdigit()
    ]
    # input time as -> str
    if len(digits) !=4:
        return "Invalid time"
    
    
    unique_digits = sorted(set(digits))
    digits_indexs = [
        unique_digits.index(digit) for digit in digits
    ]


    # loop throught last to first digit
    for i in range(3, -1, -1):
        # if postion index is less than unqiue array length , then replace that digit will sorted digit
        if digits_indexs[i] < len(unique_digits)-1:
            digits[i] = unique_digits[digits_indexs[i]]
            # if it matches the valid time
            if digits[2] <6 and digits[0]*10+digits[1] <24:
                return "{}{}:{}{}".format(*digits)

        digits[i] =unique_digits[0]

    return "{}{}:{}{}".format(*digits)



        
print(NextClosestTimme("15:56"))
print(NextClosestTimme("19:34"))
print(NextClosestTimme("23:59"))