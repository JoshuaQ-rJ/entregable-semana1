estudents=[
    {"name": "Joshua", "score": 4.0},
    {"name": "estaban", "score": 3.6},
    {"name": "Camilo", "score": 4.5},
    {"name": "samuel", "score": 2.5}
]
for i in estudents:
    print(i["name"])
total=0
for i in estudents:
    total += i["score"]
promedio=total/len(estudents) 
print(f"the avarage of notes is:{ promedio}")

notas = [i["score"] for i in estudents if i["score"] >= 4.0]
nombres = [i["name"] for i in estudents if i["score"] >= 4.0]
print(f"estudents with scores above or equal to 4.0: {nombres} with scores: {notas}")
