def name():
    #i ask for the name and i validate with the method .isalpha that the name is a stringis not de code return
    name_1=input("please enter product's name: ")
    if not name_1.isalpha():
        print("invalid name please try again")
        return name()
    else:
        return name_1
def price():
    #i ask for the price and i validate with if and try,except
    try:
        price_1=int(input("pleas enter the price of the product: "))
        if price_1<=0:
            print(f" the {price_1} is not valid please try again")
            return price()
        else:
            return price_1
    except ValueError:
        print(" the price is not valid please try again")
        return price()
def amount():
    #i ask for the amount and i validate with if and try,except
    try:
        amount_1=int(input("please enter the amount of the products: "))
        if amount_1<=0:
            print(f" the {amount_1} is not valid please try again")
            return amount()
        else:
            return amount_1
    except ValueError:
        print(f" the amount is not valid please try again")
        return amount()
def option():
    try:
        option_1=int(input("what do you want to do?: "))
        if  option_1<=0:
            print("option not valid please try again")
            return option()
        elif option_1>6:
            print("option not valid please try again")
        else:
            return option_1
    except ValueError:
        print("letters don`t alow please try again")
        return option() 