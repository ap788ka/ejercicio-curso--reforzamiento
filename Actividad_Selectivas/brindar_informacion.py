#Brindar información
consulta = input("Ingrese el nombre de artista, película o serie: "). lower()
match consulta:
    case "inception":
        info = "Peñícula de ciencia ficción dirigida por Christopher Nolan."
    case "beatles":
        info = "Banda británica de rock formada en 1960."
    case "rick and morty":
        info = "Serie animada de comedia y cienci ficción."
    case "avengers":
        info = "Película de superhéroes del MCU."
    case _:
        info = "No se encontró información."
print("información:", info)