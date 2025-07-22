intentos = 3

while intentos > 0:
    if input("escriba la contraseña: ") == "GitHub|":
        print("correcta")
        break;
    intentos = intentos - 1
    print("contraseña incorrecta.")
else:
    print("se te acabaron los intentos.")