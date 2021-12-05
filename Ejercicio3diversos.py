import os
n = int(input("Ingrese un número entre el 1 y 10: "))
m = int(input("Ingrese un número entre el 1 y 10: "))
file_name = f"./tabla-{m}.txt"
if os.path.exists(file_name):
    with open(file_name,mode="r") as f:
        v = f.read()
        print(v)
else:
    print(f"""El fichero {str(file_name.split("/")[-1])} no Existe""")