def respond(q):

    return ""

if __name__ == '__main__':
    exit_loop = False
    print("Bienvenido, aquí puede preguntar sobre sobre recetas")
    while not exit_loop:
        query = input("Ponga tu pregunta>")
        print(respond(query))


