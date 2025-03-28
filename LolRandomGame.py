import random
import os
import time
# Explicación del programa
print("Este programa sirve para generar de manera aleatoria la línea y el campeón con el que deberás jugar tu próxima partida de League Of Legends, comenzando por la línea, seguido del personaje.")

while True:
 # Elegir que randomizar
 print("Antes de continuar, deberás elegir si quieres randomizar la linea y el campeón, o solo quieres randomizar al campeón de acuerdo a la linea que escogas")
 opcion = input("¿Cómo quieres continuar?\nA: Randomizar todo \nB: Randomizar solo el campeón y elegir la linea \n").lower().strip()
 print("Su respuesta es:", opcion)


 if opcion == "a":
       # Crear una lista vacía para almacenar los nombres de los 5 jugadores
       jugadores = []

       # Pedir y almacenar los nombres de los 5 jugadores
       for i in range(5):
        nombre = input(f"Ingrese su nombre {i+1}: ")
        jugadores.append(nombre)

       # Imprimir los nombres de los jugadores
       print("Los participantes son:")
       for jugador in jugadores:
           print(jugador)


       # Pausar la ejecución del programa durante 5 segundos para que se puedan leer los nombres
       time.sleep(5)

       # Borrar la pantalla
       os.system('cls' if os.name=='nt' else 'clear')

        # Lista con las 5 respuestas posibles
       linea_respuesta = ["Top", "Jungla", "Mid", "Adc", "Support"]

        # Generar una muestra aleatoria de 5 elementos de la lista anterior para evitar repeticiones
       muestra_respuesta = random.sample(linea_respuesta, 5)

        # Mostrar la respuesta en la terminal para cada jugador
       for i, jugador in enumerate(jugadores):
        print(f"{jugador}, tu línea elegida es: {muestra_respuesta[i]}")

       print("Ahora se les asignará un personaje:")

        # Pausar la ejecución del programa durante 5 segundos para que se puedan leer los nombres
       time.sleep(8)
         
       # Lista con todos los personajes del LoL
       Campeon_respuesta = ["Aatrox", "Ahri", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bardo", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gat", "Corki", "Darius", "Draven", "Dr.Mundo", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Ivern", "Janna", "Jarvan IV", "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Karma", "Karthus", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "LeBlanc", "Leona", "Lillia", "Lucian", "Lulu", "Lux", "Maestro Yi", "Malphite", "Malzahar", "Maokai", "Milio", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu y Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Tresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yone", "Yorick", "Yummi", "Zac", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra", "Akali", "Diana", "Ezreal", "Gnar", "Irelia", "Jax", "Kassadin", "K'Sante", "Lee Sin", "Lissandra", "Viktor", "Yasuo", "Zed"]
        
        # Generar una muestra aleatoria de los campeones para evitar repeticiones 
       muestra_respuesta2 = random.sample(Campeon_respuesta, 163)

        # Mostras la respuesta en la terminal para cada jugador
       for i, jugador in enumerate(jugadores):
        print(f"{jugador}, el personaje que deberás jugar es: {muestra_respuesta2[i]}")
       print("Si a algún jugador le tocó un personaje que no tiene, deberá ingresar nuevamente el nombre para que se le asigne uno nuevo")
       print("Nota: Esto no cambia en nada el personaje de los demás ni la línea de ninguno.")

    # Bucle para asignar un campeón a cada jugador
       while True:
        respuesta = input("¿Todo listo? (SI/NO): ").lower()
        if respuesta == "si":
          # Mostras la respuesta (nueva) en la terminal para cada jugador
          print("La lista con los nuevos campeones quedó así:")
          for i, jugador in enumerate(jugadores):
           print(f"{jugador}, el personaje que deberás jugar es: {muestra_respuesta2[i]}")
          print("Suerte intentando aguantar hasta el minuto 15 ;)")
          input("Presione cualquier tecla para salir...")
          break
        elif respuesta == "no":
          while True:
            nombre_jugador = input("Ingrese el nombre del jugador a quien hay que asignarle un nuevo campeón: ")
            if nombre_jugador not in jugadores:
                print(f"{nombre_jugador} no es un jugador válido.")
                continue
            jugador_idx = jugadores.index(nombre_jugador)
            while True:
                nuevo_campeon = random.choice(Campeon_respuesta)
                if nuevo_campeon != muestra_respuesta2[jugador_idx]:
                    break
            muestra_respuesta2[jugador_idx] = nuevo_campeon
            print(f"El nuevo campeón de {nombre_jugador} es: {nuevo_campeon}")
            respuesta_jugador = input("¿Desea cambiar el campeón para otro jugador? (SI/NO): ").lower()
            if respuesta_jugador == "no":
                break
        else:
            print("Respuesta no válida, por favor ingrese 'SI' o 'NO'")
            continue
       
    # Mostras la respuesta (nueva) en la terminal para cada jugador
       print("La lista con los nuevos campeones quedó así:")
       for i, jugador in enumerate(jugadores):
        print(f"{jugador}, el personaje que deberás jugar es: {muestra_respuesta2[i]}")
       print("Suerte intentando aguantar hasta el minuto 15 ;)")
       input("Presione cualquier tecla para salir...")
       continue

 elif opcion == "b":
         print("A continuación eliga la linea y se le asignará un campeon al azar:")
         # Lista con las 5 respuestas posibles
         linea_respuesta = ["Top", "Jungla", "Mid", "Adc", "Support"]
         respuesta = input("Top\nJungla\nMid\nAdc\nSupport\n").lower().strip()
         
         if respuesta == "top":
           # Borrar la pantalla
           os.system('cls' if os.name=='nt' else 'clear')
           print("Su respuesta ha sido Top")
           # Lista con los campeones (Top)
           campeon_top = ["Aatrox", "Camille", "Cho'Gat", "Darius", "Dr.Mundo", "Fiora", "Gangplank", "Garen", "Gragas", "Gwen", "Illaoi", "Jayce", "Kayle", "Kennen", "Kled", "Malphite", "Mordekaiser", "Nasus", "Olaf", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Riven", "Rumble", "Sett", "Shen", "Singed", "Sion", "Tahm Kench", "Teemo", "Tryndramere", "Urgot", "Volibear", "Warwick", "Yone", "Yorick", "Akali", "Gnar", "Irelia", "Jax", "K'Sante", "Yasuo", "Jarvan IV", "Rengar", "Zac", "Vayne"]
           # Generar una muestra aleatoria de los campeones de Top
           muestra_respuesta3 = random.sample(campeon_top, 48)

           # Mostras la respuesta en la terminal
           print(f"El campeón es: {random.choice(campeon_top)}")
           # Bucle para asignar un campeón
           while True:
            respuesta2 = input("¿Todo listo? (SI/NO): ").lower()
            if respuesta2 == "si":
              print("¡Suerte!")
              input("Presione cualquier tecla para salir...").lower()
              break
            elif respuesta2 == "no":
                while True:
                # Generar una muestra aleatoria de los campeones de Top
                 muestra_respuesta3 = random.sample(campeon_top, 48)
                 # Mostras la respuesta en la terminal
                 print(f"El campeón es: {random.choice(campeon_top)}")
                 respuesta2 = input("¿Desea volver a cambiar el campeón? (si/no): ").lower()
                 if respuesta2 == "no":
                  break
            else:
               print("Respuesta no válida, por favor ingrese 'SI' o 'NO'")
               continue
           
         elif respuesta == "jungla":
            #copiar todo y cambiar las variables.
            # Borrar la pantalla
            os.system('cls' if os.name=='nt' else 'clear')
            print("Su respuesta ha sido Jungla")
            # Lista con los campeones (Jungla)
            campeon_jungla = ["Amumu", "Bel'Veth", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern", "Jarvan IV", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Lillia", "Maestro Yi", "Maokai", "Nidalee", "Nocturne", "Nunu y Willump", "Poppy", "Rammus", "Rek'Sai", "Rengar", "Sejuani", "Shaco", "Shyvana", "Skarner", "Sylas", "Trundle", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Xin Zhao", "Zac", "Dianna", "Lee Sin", "Zed"]
            # Generar una muestra aleatoria
            muestra_respuesta4 = random.sample(campeon_jungla, 42)
            # Mostrar la respuesta
            print(f"El campeón es: {random.choice(campeon_jungla)}")

            # Bucle para asignar un campeón
            while True:
             respuesta3 = input("¿Todo listo? (SI/NO): ").lower()
             if respuesta3 == "si":
              print("¡Suerte!")
              input("Presione cualquier tecla para salir...").lower()
              break
             elif respuesta3 == "no":
                while True:
                # Generar una muestra aleatoria de los campeones de Top
                 muestra_respuesta4 = random.sample(campeon_jungla, 42)
                 # Mostras la respuesta en la terminal
                 print(f"El campeón es: {random.choice(campeon_jungla)}")
                 respuesta3 = input("¿Desea volver a cambiar el campeón? (si/no): ").lower()
                 if respuesta3 == "no":
                  break
             else:
               print("Respuesta no válida, por favor ingrese 'SI' o 'NO'")
               continue
             
         elif respuesta == "mid":
            # Borrar la pantalla
            os.system('cls' if os.name=='nt' else 'clear')
            print("Su respuesta ha sido Mid")
            # Lista con los campeones (Mid)
            campeon_mid = ["Ahri", "Akshan", "Anivia", "Annie", "Aurelion Sol", "Cassiopeia", "Corki", "Ekko", "Fizz", "Galio", "Gangplank", "Katarina", "LeBlanc", "Lux", "Malzahar", "Neeko", "Orianna", "Pantheon", "Qiyana", "Rumble", "Ryze", "Sylas", "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar", "Vex", "Vladimir", "Yone", "Ziggs", "Zoe", "Akali", "Azir", "Dianna", "Irelia", "Kassadin", "Lissandra", "Viktor", "Yasuo", "Zed", "Vel'Koz", "Xerath"]
            # Generar muestra aleatoria
            muestra_respuesta5 = random.sample(campeon_mid, 43)
            # Mostrar la respuesta
            print(f"El campeón es: {random.choice(campeon_mid)}")

            # Bucle para asignar un campeón
            while True:
             respuesta4 = input("¿Todo listo? (SI/NO): ").lower()
             if respuesta4 == "si":
              print("¡Suerte!")
              input("Presione cualquier tecla para salir...").lower()
              break
             elif respuesta4 == "no":
                while True:
                # Generar una muestra aleatoria de los campeones de Top
                 muestra_respuesta5 = random.sample(campeon_mid, 43)
                 # Mostras la respuesta en la terminal
                 print(f"El campeón es: {random.choice(campeon_mid)}")
                 respuesta4 = input("¿Desea volver a cambiar el campeón? (si/no): ").lower()
                 if respuesta4 == "no":
                  break
             else:
               print("Respuesta no válida, por favor ingrese 'SI' o 'NO'")
               continue
            
         elif respuesta == "adc":
            # Borrar la pantalla
            os.system('cls' if os.name=='nt' else 'clear')
            print("Su respuesta ha sido Adc")
            # Lista con los campeones (Adc)
            campeon_adc = ["Aphelios", "Ashe", "Caitlyn", "Draven", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian", "Miss Fortune", "Nilah", "Samira", "Sivir", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Zeri", "Ezreal"]
            # Generar muestra aleatoria
            muestra_respuesta6 = random.sample(campeon_adc, 21)
            # Mostrar la respuesta
            print(f"El campeón es: {random.choice(campeon_adc)}")

            # Bucle para asignar un campeón
            while True:
             respuesta5 = input("¿Todo listo? (SI/NO): ").lower()
             if respuesta5 == "si":
              print("¡Suerte!")
              input("Presione cualquier tecla para salir...").lower()
              break
             elif respuesta5 == "no":
                while True:
                # Generar una muestra aleatoria de los campeones de Adc
                 muestra_respuesta6 = random.sample(campeon_adc, 21)
                 # Mostras la respuesta en la terminal
                 print(f"El campeón es: {random.choice(campeon_adc)}")
                 respuesta5 = input("¿Desea volver a cambiar el campeón? (si/no): ").lower()
                 if respuesta5 == "no":
                  break
             else:
               print("Respuesta no válida, por favor ingrese 'SI' o 'NO'")
               continue
             
         elif respuesta == "support":
             # Borrar la pantalla
            os.system('cls' if os.name=='nt' else 'clear')
            print("Su respuesta ha sido Support")
            # Lista con los campeones (Supp)
            campeon_sup = ["Alistar", "Amumu", "Ashe", "Bardo", "Blitzcrank", "Brand", "Braum", "Heimerdinger", "Janna", "Karma", "Leona", "Lulu", "Lux", "Maokai", "Morgana", "Nami", "Nautilus", "Pantheon", "Pyke", "Rakan", "Rell", "Renata Glasc", "Senna", "Seraphine", "Sona", "Soraka", "Swain", "Taric", "Tresh", "Twitch", "Vel'Koz", "Xerath", "Yummi", "Zilean", "Zyra"]
            # Generar muestra
            muestra_respuesta7 = random.sample(campeon_sup, 35)
            # Mostrar la respuesta
            print(f"El campeón es: {random.choice(campeon_sup)}")

            # Bucle para asignar un campeón
            while True:
             respuesta6 = input("¿Todo listo? (SI/NO): ").lower()
             if respuesta6 == "si":
              print("¡Suerte!")
              input("Presione cualquier tecla para salir...").lower()
              break
             elif respuesta6 == "no":
                while True:
                # Generar una muestra aleatoria de los campeones de Top
                 muestra_respuesta7 = random.sample(campeon_sup, 35)
                 # Mostras la respuesta en la terminal
                 print(f"El campeón es: {random.choice(campeon_sup)}")
                 respuesta6 = input("¿Desea volver a cambiar el campeón? (si/no): ").lower()
                 if respuesta6 == "no":
                  break
             else:  
               print("Respuesta no válida, por favor ingrese 'SI' o 'NO'")
               continue

 else:
    # Borrar la pantalla
    os.system('cls' if os.name=='nt' else 'clear')
    print("Responda con A o B, por favor")
    continue


            
             