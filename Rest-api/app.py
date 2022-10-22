from productos import producto  # Base de datos
from flask import Flask, jsonify, request  # Librerias de flask necesarias

app = Flask(__name__)


@app.route("/ping")  # Probar la conexion
def ping():
    return jsonify({"Mensaje": "Pong"})


@app.route("/productos")  # Muestra el contenido de la base en su totalidad
def get_productos():
    return jsonify({"Products": producto, "MENSAJE": "Listas de productos"})


@app.route(
    "/productos/<string:product_name>"
)  # muestra la informacion relacionada con el id enviado
def get_producto(product_name):
    product_found = [
        producto for producto in producto if producto["name"] == product_name
    ]
    if len(product_found) > 0:
        return jsonify({"PRODUCTO": product_found[0]})
    else:
        return jsonify({"MENSAJE": "No se encontro ninguna coincidencia"})


@app.route("/productos", methods=["POST"])  # Ingresa informacion a la base
def agregar_productos():
    nuevo_producto = {
        "id": request.json["id"],
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"],
    }
    print(request.json)
    producto.append(nuevo_producto)
    return jsonify({"MESSAGE": "PRODUCTO AGREGADO", "PRODUCTOS": producto})


@app.route(
    "/productos/<string:product_name>", methods=["PUT"]
)  # Actualiza la informacion de un producto mediante el id
def edit_producto(product_name):
    product_found = [
        producto for producto in producto if producto["name"] == product_name
    ]
    if len(product_found) > 0:
        product_found[0]["name"] = request.json["name"]
        product_found[0]["price"] = request.json["price"]
        product_found[0]["quantity"] = request.json["quantity"]

        return jsonify(
            {"MESSAGE": "Producto actualizado", "PRODUCTOS": product_found[0]}
        )
    else:
        return jsonify({"MENSAJE": "No se encontro ninguna coincidencia"})


@app.route("/productos/<string:product_name>", methods=["DELETE"])
def eliminar_producto(product_name):
    product_found = [
        productos for productos in producto if productos["name"] == product_name
    ]
    if len(product_found) > 0:
        producto.remove(product_found[0])
        return jsonify(
            {"MESSAGE": "PRODUCTO ELIMINADO SATISFACTORIAMENTE", "PRODUCTOS": producto}
        )
    else:
        return jsonify({"MESSAGE": "NO SE ENCONTRO EL PRODUCTO"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
