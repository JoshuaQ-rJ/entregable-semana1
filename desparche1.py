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
        print(f" the {amount_1} is not valid please try again")
        return amount()
#i call de fuctions and fill the variable and made the operacions
name=name()
price=price()                
amount=amount()
total_cost=price*amount
#this side print the bill
print(f"\nthe name of the product is: {name}")
print(f"the price for only 1 product is: {price}")
print(f"the amount is: {amount}")
print(f"the total cost is: {total_cost}\n" )
while True:
    try:
        enter_menu=input("you")
    except:
        pass

def registrar_producto():
    name=name()
    price=price()                
    amount=amount()
    total_cost=price*amount
    register={"nombre":name, "price":price, "amount":amount, "total":total_cost}
    return register





