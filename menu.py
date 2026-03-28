from services import name,price,amount,option
from app import save_inventory, upload_inventory
from Inventario import inventory

def menu() :
    while True:
        print("\n---welcome to the inventory---\n1. add a product\n2. show inventory\n3. calculate inventory\n4. save inventory\n5. upload inventory\n6. exit")
        op=option()
        if op ==1:
            name_1=name()
            price_1=price()
            amount_1=amount()
            inventory.append({"name":name_1,"price":price_1,"amount":amount_1})
        elif op ==2:
            if not inventory:
                    print("the inventory is clear")
            else:
                print(f"the products register are:\n")
                for p in inventory:
                    print(f"products: {p["name"]}| price {p["price"]}| amount {p["amount"]}")
                
        elif op==3:
            total=0
            for i in inventory:
                total+= i["price"]*i["amount"]
                num=len(inventory)
            price_expencive = max(inventory, key =lambda i: i["price"])
            max_stock=max(inventory, key =lambda i: i["amount"])
            print(f"the total value for your inventory is: {total}\nthe total products register are: {num}")
            print(f"\nthe most expensive product is: {price_expencive["name"]} with price: ${price_expencive["price"]}\nand the product with the most stock is : {max_stock["name"]} with {max_stock["amount"]} available")
        elif op ==4:
            save_inventory()
            print("saving your inventory...... save correctly\nsave in data/data.csv")            
        elif op ==5:
            upload_inventory()
            print("upload made correctly")
            
        elif op==6:
            print("leaving the inventory, thanks for your use")
            exit()
menu()