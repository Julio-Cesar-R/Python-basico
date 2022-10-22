# Pagina donde se pueden hacer pruebas
# https://books.toscrape.com/catalogue/page-1.html

import bs4, requests  # Librerias requeridas

# Url que ira cambiando con {}
url_base = "https://books.toscrape.com/catalogue/page-{}.html"
mejores_libros = []  # lista que contendra los mejores libros


def crear_ruta(ruta):
    """
    Metodo que recibe una ruta y la convierte
    en un objeto para inspeccionar un sitio web
    """
    url = requests.get(ruta)
    sopa = bs4.BeautifulSoup(url.text, "lxml")
    # primera busqueda nombre de la clase
    titulos = sopa.select(".product_pod")
    buscar_titulos(titulos)


def buscar_titulos(titulos):
    # recibe una busqueda y la actualiza con otra busqueda

    for n in titulos:
        libro = n.select("a")[1][
            "title"
        ]  # Hacemos la busqueda como si fuera un diccionario con los datos extraidos
        if n.select(".star-rating.Four") or n.select(".star-rating.Five"):
            mejores_libros.append(libro)  # Agrega a la lista de mejores libros


# Genera las rutas cambiando el formato
for n in range(1, 51):
    nueva_ruta = url_base.format(n)  # Cambia la url base
    crear_ruta(nueva_ruta)

# Muestra la lista de mejores libros
for best in mejores_libros:
    print(best)
print(len(mejores_libros))  # tamaño de la lista
# print(lista_libros)
