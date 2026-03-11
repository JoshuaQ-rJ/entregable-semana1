person={
    "name":"juan",
    "age": 17,
    "city":"barranquilla"
}
print(person["name"])
print(person.get("age"))
print(person.get("tel","no existe"))
person["profession"]="estudent"
person["age"]=18
keyerased=person.pop("city")
print(keyerased)
print(person)
