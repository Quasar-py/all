def p(maximum, number, sign):
    if sign == '<=':
        if maximum+1 >= number and 2*maximum >= number > 2:
            return int(((number-1)*number)/2)
        elif maximum+1 < number and 2*maximum >= number > 2:
            r = 2*maximum-number
            return int(maximum**2-((r+1)*r)/2)
        else:
            return "Ошибочка"
    elif sign == '>=':
        if maximum+1 >= number and 2*maximum >= number > 2:
            number -= 1
            return int(maximum**2-((number-1)*number)/2)
        elif maximum+1 < number and 2*maximum >= number > 2:
            r = 2*maximum+1-number
            return int(((r+1)*r)/2)
        else:
            return "Ошибочка"
    elif sign == '<':
        if maximum+1 >= number and 2*maximum >= number >= 2:
            number -= 1
            return int(((number-1)*number)/2)
        elif maximum+1 < number and 2*maximum >= number >= 2:
            r = 2*maximum+1-number
            return int(maximum**2-((r+1)*r)/2)
        else:
            return "Ошибочка"
    elif sign == '>':
        if maximum+1 >= number and 2*maximum >= number >= 2:
            return int(maximum**2-((number-1)*number)/2)
        elif maximum+1 < number and 2*maximum >= number >= 2:
            r = 2*maximum-number
            return int(((r+1)*r)/2)
        else:
            return "Ошибочка"
    elif sign == '==':
        if maximum+1 >= number and 2*maximum >= number >= 2:
            return int(number-1)
        elif maximum+1 < number and 2*maximum >= number >= 2:
            return int(2*maximum-number)
        else:
            return "Ошибочка"
    elif sign == '!=':
        if maximum + 1 >= number and 2 * maximum >= number >= 2:
            return int(maximum**2-(number - 1))
        elif maximum + 1 < number and 2 * maximum >= number >= 2:
            return int(maximum**2-(2 * maximum + 1 - number))
        else:
            return "Ошибочка"
    else:
        return "Ошибочка"
