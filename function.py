def validate_number(number):
    if type(number) != int:
        if type(number) == str :
            return "input integer"
        elif number >=1 and number <= 11:
            return "input integer"
        else:
            return "out of rang"
    elif number >= 1 and number <= 12:
        return number
        
    else:
        return "out of rang"
        

def number_to_month(num) :
    month = ["january","february","march", "april", "may","june","july",
            "august","september","october","november","december"]
    return month[num - 1]

def display_month(number):
    result = validate_number(number)
    if type(result) == int:
        return number_to_month(result)
    else:
        return result