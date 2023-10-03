def calculator (equaision):
    list = []
    num = str()
    bracket = 0
    left_brack = 0
    mul_div = []
    add_sub = []
    in_bracket = str()
    pow_root = []
    for i in equaision:
        if (bracket == 0):
            if ((ord(i) >= 48 and ord(i) <= 57) or i == '.'):
                num += i
            elif (i == '+' or  i == '-' or i == '*' or i == '/' or i == '^' or i == 'r'):
                if(len(num) > 0):
                    list.append(float(num))
                    num = str()
                if(i == '+'):
                    add_sub.append(i)
                    list.append(i)
                if(i == '-'):
                    if(len(list) != 0):
                        add_sub.append(i)
                        list.append(i)
                    else:
                        num += i
                if (i == '*' or i == '/'):
                    mul_div.append(i)
                    list.append(i)
                if (i == '^' or i == 'r'):
                    pow_root.append(i)
                    list.append(i)
            elif ( i == '('):
                bracket += 1
                left_brack += 1
                list.append(i)
        else:
            if (i == '('):
                bracket += 1
                in_bracket += i
            elif (i == ')'):
                bracket -= 1
                if(bracket != 0):
                    in_bracket += i
                else:
                    list.append(in_bracket)
                    in_bracket = str()
                    list.append(i)
            else:
                in_bracket += i
    if(len(num) > 0):
        list.append(float(num))
        num = str()
    for i in range(left_brack):
        x = list.index('(')
        list.pop(x+2)
        list.pop(x)
        list[x] = calculator(list[x])
    for i in pow_root:
        if(i == '^'):
            list[list.index('^') - 1] = list[list.index('^') - 1] ** list[list.index('^') + 1]
            list.pop(list.index('^') + 1)
            list.pop(list.index('^'))
        else:
            list[list.index('r') - 1] = list[list.index('r') + 1] ** (1/(list[list.index('r') - 1]))
            list.pop(list.index('r') + 1)
            list.pop(list.index('r'))
    for i in mul_div:
        if(i == '*'):
            list[list.index('*') - 1] = list[list.index('*') - 1] * list[list.index('*') + 1]
            list.pop(list.index('*') + 1)
            list.pop(list.index('*'))
        else:
            list[list.index('/') - 1] = list[list.index('/') - 1] / list[list.index('/') + 1]
            list.pop(list.index('/') + 1)
            list.pop(list.index('/'))
    for i in add_sub:
        if(i == '+'):
            list[list.index('+') - 1] = list[list.index('+') - 1] + list[list.index('+') + 1]
            list.pop(list.index('+') + 1)
            list.pop(list.index('+'))
        else:
            list[list.index('-')-1] = list[list.index('-') - 1] - list[list.index('-') + 1]
            list.pop(list.index('-') + 1)
            list.pop(list.index('-'))
    return list[0]
print('0 to break\n1 for legend\n2 to calculate')
while True:
    b = input('0, 1 or 2??\n')
    if (b == '0'):
        break
    elif (b == '2'):
        try:
            print(round(calculator(input('what would you like to calculate??\n')), 10))
        except:
            print('xd')
    elif (b == '1'):
        print("+ for add\n- for subbtract]\n* for multiply\n/ for divade\nr for root\n^ for power\n")
# 2r((3r((2^6+6^2)*10)+2*((18-9)/3)^2)/7) = 2
