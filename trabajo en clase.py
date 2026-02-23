# Solicita la edad y muestra el mensaje correspondiente
edad = int(input("Introduce tu edad: "))

if edad < 16:
    print("No puedes obtener licencia.")
elif edad in (16, 17):
    print("Puedes solicitar licencia de aprendiz.")
else:  # edad >= 18
    print("Puedes obtener licencia completa.")
