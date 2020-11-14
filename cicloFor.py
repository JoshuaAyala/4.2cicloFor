import time, os

def goBackm():
	goBack = int(input("¿Quieres volver al menú?\n[1] Sí.\n[0] No.\n>: "))
	if(goBack==1):
		main()
	elif(goBack==0):
		print("Bye")
		exit()
	else:
		print("EScribe una opción correcta.")
		time.sleep(3)
		goBackm()

def tabla():
	numero = int(input("¿De qué número quieres saber su tabla de multiplicación?\n>: "))

	for x in range(numero,(numero*10)+1,numero):
		print(x)

	goBackm()

def party():
	invitados = ["JUANCHO","CARLA","EZEQUIEL","MARCO","PABLO"]
	print("\nLista de invitados:")
	print(invitados)
	excluded = input("¿A qué amigo quieres excluir de tu fiesta?\n>: ")
	print("\nLista de invitados actualizada:")
	for x in invitados:
		if(x==excluded.upper()):
			continue
		print(x)

	goBackm()

def main():
	os.system('clear')
	print("\n---- Bienvenido ----\n")
	time.sleep(1)
	elección = int(input("¿Qué deseas hacer?\n[1] Tablas de multiplicar.\n[2] Eliminar invitados.\n>: "))
	if(elección==1):
		tabla()
	elif(elección==2):
		party()
	elif(elección==0):
		exit()
	else:
		print("EScribe una opción correcta.")
		time.sleep(3)
		main()

main()