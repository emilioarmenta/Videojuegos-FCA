import random as rd

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

baraja=[]#Fichas para repartir/robar

def saludo():
    print("\tBIENVENIDO AL JUEGO DE DOMINÓ")


reglas= input("Deseas ver las reglas: (Y/N)").capitalize()
saludo()
if reglas == 'Y':
    print("Reglas: \n Para jugar al dominó son necesarias 28 fichas rectangulares. \n Cada ficha está dividida en 2 espacios iguales en los que aparece una cifra de 0 hasta 6. \n Se puede jugar con 2, 3 ó 4 jugadores o por parejas.\n El objetivo del juego es colocar todas tus fichas en la mesa antes que los contrarios y sumar puntos. \n El jugador que gana una ronda, suma puntos según las fichas que no han podido colocar los oponentes.\n La partida termina cuando un jugador o pareja alcanza logran colocar todas sus fichas en la mesa.\n La ficha tirada debe coincidir con algún extremo de la ficha en la mesa")


#BARAJA 28 FICHAS
def crearBaraja():
    baraja=[]
    #ficha[]
    for i in range(0,7):
        for j in range (0, i+1):
            baraja.append({"izquierda":i, "derecha":j})
           # ficha=["derecho", "izquierdo"]

    rd.shuffle(baraja)
    return(baraja)

baraja=crearBaraja()


print("\n\nFichas creadas " + str(len(baraja)))

#Creación de jugadores
jugadoresN = 0
jugadoresN = int(input("Ingresa el número de jugadores. (Máximo 4, mínimo 2) "))
if jugadoresN == 2:
    jugadores=[
   {"nombre":"","mano":[], "tipo":"HUMANO", "puntuacion":0},
   {"nombre":"robot1","mano":[], "tipo": "IA", "puntuacion":0}]
    jugadores[0]["nombre"]=input("Dime tu nombre:")
elif jugadoresN == 3:
     jugadores=[
   {"nombre":"","mano":[], "tipo":"HUMANO", "puntuacion":0},
   {"nombre":"robot1","mano":[], "tipo":"HUMANO", "puntuacion":0},
   {"nombre":"robot2","mano":[], "tipo": "IA", "puntuacion":0}]
     jugadores[0]["nombre"]=input("Dime tu nombre:")
else:
   jugadores=[
   {"nombre":"","mano":[], "tipo":"HUMANO", "puntuacion":0},
   {"nombre":"robot1","mano":[], "tipo": "IA", "puntuacion":0},
   {"nombre":"robot2","mano":[], "tipo": "IA", "puntuacion":0},
   {"nombre":"robot3","mano":[], "tipo": "IA", "puntuacion":0}]
   jugadores[0]["nombre"]=input("Dime tu nombre:")

#REPARTIR BARAJA
for _ in range(7):
   for jugador in jugadores:
      jugador["mano"].append(baraja[0])
      baraja=baraja[1:]


for jugador in jugadores:
    print(jugador["nombre"])
    print(jugador["mano"])
print("\nFichas restantes en baraja: " + str(len(baraja)))

        

print("Numero de jugadores: "+ str(jugadoresN))

mula = {'izquierda': 6, 'derecha': 6} 

#Encontrar mula para iniciar el juego
def encontrarMula(jugador, fichaMesa=None, mula=None):
    mula = {'izquierda': 6, 'derecha': 6} 
    buscarMula = True
    while buscarMula:
        for jugador in jugadores:
            if mula in jugador["mano"] and buscarMula :
            #  for i in 2:
                    print("La mula la tiene " + jugador["nombre"])
                    jugador["mano"].remove(mula)
                    fichaMesa = mula
                    print("Ficha inicial: " + str(fichaMesa))
                    buscarMula = False 
        break
    else:
        print("La mula no la tienen nigún jugador")
    return mula, fichaMesa
    
#Mostrar solo los valores de las fichas
def mostrarFichas(ficha):
    return (str(ficha["izquierda"]) +" | ") + str(ficha["derecha"])

#Mostrar la mano de cada jugador
def mostrarMano(jugador, numeradas=False, fichaMesa=None):
    i=1
    col=0
    cadenaSalida=""
    for ficha in jugador["mano"]:
        textoFicha=((str(i)+" " if numeradas else ""))
        if fichaMesa!=None and cumpleReglas(ficha,fichaMesa):
            textoFicha+=bcolors.BOLD+ mostrarFichas(ficha)+bcolors.ENDC
        else:
            textoFicha+=mostrarFichas(ficha)
        cadenaSalida+=("\t" if col>0 else "\r\n")+textoFicha.ljust(20," ")
        if(col==3):
            col=0
        else:
            col+=1
        i+=1
    print(cadenaSalida)
    
#Verificar si una ficha cumple con las reglas para que pueda ser jugada!!!!
def cumpleReglas(fichaEscogida, fichaMesa):
    if str(fichaEscogida["izquierda"]) or str(fichaEscogida["derecha"]) == str(fichaMesa["izquierda"]):
        return True
    else:
        return str(fichaEscogida["izquierda"]) or str(fichaEscogida["derecha"]) == str(fichaMesa["derecha"])
    

#Elegir que ficha quiere jugar cada jugador
def escogerFicha(jugador, fichaMesa, baraja):
    repetir = True
    seleccionada = None
    encontrarMula(jugador)
    while repetir:
        mostrarMano(jugador, True, fichaMesa)
        idFichaEscogida = input("Qué ficha quieres tirar? (R para robar) fichas en Baraja (" +(str(len(baraja)))+"): ").capitalize()
        if idFichaEscogida == 'R':
            if len(baraja)>0:
                    jugador["mano"].append(baraja[0])
                    return baraja 
            else:
                    print("No hay fichas para robar")
        elif idFichaEscogida.isnumeric() and int(idFichaEscogida)>0 and int(idFichaEscogida)<=(len(jugador["mano"])):#Verificar que ingrese un numero mayor a 0 y menor al número de sus fichas
            fichaEscogida=jugador["mano"][int(idFichaEscogida)-1]
            if cumpleReglas(fichaEscogida,fichaMesa):
                jugador["mano"] = jugador["mano"][0:int(idFichaEscogida)-1] + jugador["mano"][int(idFichaEscogida):]
                fichaMesa = fichaEscogida
                monton = [fichaMesa, fichaEscogida]
                print("Jugadas: " + mostrarFichas(fichaEscogida), ", " + mostrarFichas(mula))
                repetir =False
            else:
                print("Esa ficha no vale")
    return fichaEscogida

#Juego
continuar = True
while continuar:
    for jugador in jugadores:
        print("\nTurno de " + jugador["nombre"])
        fichaMesa=mula
        fichaEscogida, baraja = escogerFicha(jugador, fichaMesa, baraja)
        if len(jugador["mano"]) == 0:
            print("FELICIDADES " + jugador["nombre"]+ " GANASTE!")
            continuar=False
            break
