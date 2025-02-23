import json 

FIle = "contacts.json"

def load():
    try:
        return json.load(open(FIle))
    except:
        return {}
    
def save(c):
    json.dump(c, open(FIle, "w"))

def add():
    c = load()
    c[input("Nombre: ")] = input("Telefono: ")
    save(c)

def list():
    print("\n".join(f"{n}: {p}" for n, p in load().items()))

while (o := input("1. Agregar\n2. Listar\n3. Salir\n")) != "3":
     {"1": add, "2": list}.get(o, lambda: None)()


