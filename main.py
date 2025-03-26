from auth.registration import Registration
from auth.login import Login

def main():
    registration = Registration()
    login = Login()
    
    while True:
        print("\n=== Sistema de Usuarios ===")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        option = input("Seleccione una opción: ")
        
        if option == "1":
            username = input("Ingrese nombre de usuario: ")
            email = input("Ingrese email: ")
            password = input("Ingrese contraseña: ")
            
            if registration.register_user(username, email, password):
                print("Usuario registrado exitosamente!")
            else:
                print("Error: El usuario o email ya existe")
        
        elif option == "2":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            
            if login.authenticate(username, password):
                print(f"\n¡Bienvenido, {username}!")
                # Here you can add user-specific functionality
                while True:
                    print("\n=== Menú de Usuario ===")
                    print("1. Cerrar sesión")
                    
                    user_option = input("Seleccione una opción: ")
                    if user_option == "1":
                        print("Sesión cerrada")
                        break
            else:
                print("Error: Usuario o contraseña incorrectos")
        
        elif option == "3":
            break

if __name__ == "__main__":
    main()