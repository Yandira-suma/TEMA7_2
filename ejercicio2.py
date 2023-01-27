import time

def tiempo_falta(hora: int, minutos: int):
    if hora >= 19:
        print("Es hora de ir a casa")
    else:
        minutosRestantes: int=60-minutos
        horasRestantes: int=0
        if minutosRestantes == 60:
            horasRestantes=19-hora
            minutosRestantes=0
            print("Falta para la hora de salida {} horas con {} minutos".format(horasRestantes, minutosRestantes))
        else:
            horasRestantes=19-hora-1
            print("Falta para la hora de salida {} horas con {} minutos".format(horasRestantes, minutosRestantes))

def main():
  
    print("Fecha del sistema: "+time.strftime("%c"))
    print("Dia: "  + time.strftime("%x"))
    print("Hora: "+time.strftime("%X"))

    hora: int=int(time.strftime("%H"))
    minutos: int=int(time.strftime("%M"))

    tiempo_falta(hora, minutos)

    
if __name__ == '__main__':
    main()
