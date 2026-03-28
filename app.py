import csv
from Inventario import inventory
print(type(inventory))
print(inventory)
def save_inventory():
    if not inventory:
        print("the inventory is empty")
    else:
        with open("entregable-semana1/data/data.csv", "w", newline="", encoding="utf-8") as f:
            write = csv.DictWriter(f, fieldnames=["name", "price", "amount"])
            write.writeheader()
            write.writerows(inventory)
save_inventory()
def read_register():
    with open("entregable-semana1/data/data.csv","r",newline="", encoding="utf-8") as read:
        reads=csv.DictReader(read)
        return list(reads)
def upload_inventory():
    registers=read_register()
    if len(registers)==0:
        print("no are register, please save and try again")
        return False
    with open("entregable-semana1/data/data.csv","r",newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for r in reader:
            name_1=r["name"]
            price_1=float(r["price"])
            amount_1=int(r["amount"])
            inventory.append({"name":name_1,"price":price_1,"amount":amount_1})

