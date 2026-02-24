from rich.console import Console
from rich.panel import Panel

console = Console()

generos = {
    "fantasia": {
        "descripcion": "Historias con magia, criaturas míticas y mundos imaginarios.",
        "libros": [
            "Harry Potter - J.K. Rowling",
            "El Señor de los Anillos - J.R.R. Tolkien",
            "Las Crónicas de Narnia - C.S. Lewis"
        ]
    },
    "ciencia ficcion": {
        "descripcion": "Relatos sobre tecnología futurista y avances científicos.",
        "libros": [
            "Dune - Frank Herbert",
            "1984 - George Orwell",
            "Fahrenheit 451 - Ray Bradbury"
        ]
    },
    "romance": {
        "descripcion": "Historias centradas en relaciones amorosas.",
        "libros": [
            "Orgullo y Prejuicio - Jane Austen",
            "Bajo la misma estrella - John Green",
            "Cumbres Borrascosas - Emily Brontë"
        ]
    },
    "terror": {
        "descripcion": "Narraciones diseñadas para provocar miedo y suspenso.",
        "libros": [
            "It - Stephen King",
            "Drácula - Bram Stoker",
            "Frankenstein - Mary Shelley"
        ]
    }
}

def mostrar_genero(nombre_genero):
    genero = generos.get(nombre_genero.lower())

    if genero:
        descripcion = genero["descripcion"]
        libros = "\n".join(genero["libros"])
        contenido = f"Descripción:\n{descripcion}\n\nLibros principales:\n{libros}"
        console.print(Panel(contenido, title=f"Género: {nombre_genero.capitalize()}"))
    else:
        console.print("Género no encontrado. Intenta con: fantasia, ciencia ficcion, romance o terror.")

if __name__ == "__main__":
    console.print("=== Generador de Géneros Literarios ===")
    genero_usuario = input("Escribe un género: ")
    mostrar_genero(genero_usuario)