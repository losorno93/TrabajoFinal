from flask import Flask, jsonify, request

app = Flask(__name__)

concesionario = []

# Mostrar los concesionarios que existen
@app.route("/") 
def obtenerVehiculos():
    try:
        return jsonify({"concesionario" : concesionario})
    except:
        return 'Verifica tus datos ha ocurrido un error'
       
        

@app.route("/vehiculo/<string:nombreVehiculo>", methods=['GET']) # Se muestra un vehiculo
def obtenerVehiculo(nombreVehiculo):
    try:
        devuelveVehiculo = [vehiculo for vehiculo in concesionario if vehiculo['nombre del vehiculo'] == nombreVehiculo]
        if (len(devuelveVehiculo) > 0):
            return jsonify({"vehiculo" : devuelveVehiculo[0]})
        return 'vehiculo no encontrado'
    except:
        return 'Verifica tus datos ha ocurrido un error'
    

@app.route("/agregar", methods=['POST']) 
def agregar():                           
    try:
        nuevosVehiculos = {
            "nombre" : request.json['nombre'],
            "precio" : request.json['precio'],
            "cantidad" : request.json['cantidad']
        }
        concesionario.append(nuevosVehiculos)
        return jsonify({
                "mensaje": "Exito agregando vehiculo",
                "Concesionario": nuevosVehiculos
                
            })
    except:
        return 'Verifica tus datos ha ocurrido un error'
    
    
@app.route("/editar/<string:nombreVehiculo>", methods=['PUT']) # edita los vehiculos
def editar(nombreVehiculo):
    try:
        cambioVehiculo = [vehiculo for vehiculo in concesionario if vehiculo['nombre'] == nombreVehiculo]
        if (len(cambioVehiculo) > 0):
            cambioVehiculo[0]['nombre'] = request.json['nombre']
            cambioVehiculo[0]['precio'] = request.json['precio'] 
            cambioVehiculo[0]['cantidad'] = request.json['cantidad']
            return jsonify({
                "mensaje" : "Exito editando el vehiculo ",
                "producto" : cambioVehiculo[0]
            })
        return 'vehiculo NO encontrado'
    except:
        return 'Verifica la informacion ha ocurrido un error'



@app.route("/eliminar/<string:nombreVehiculo>", methods=['DELETE']) # selecciona el nombre del vehiculo 
def eliminar(nombreVehiculo):                                       # que desea eliminar indicando el nombre
    try:
        eliminarVehiculo = [vehiculo for vehiculo in concesionario if vehiculo ['nombre'] == nombreVehiculo]
        if len(eliminarVehiculo) > 0:
            concesionario.remove(eliminarVehiculo[0])
            return jsonify({
                "mensaje": "Vehiculo Eliminado",
                "concesionario": concesionario
            })
        return "Vehiculo NO encontrado"
    except:
        return 'Verifica la informacion ha ocurrido un error'


