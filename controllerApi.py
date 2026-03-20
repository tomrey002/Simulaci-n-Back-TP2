import serviceGeneracionNumeros as sgn
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.route("/generar-numeros", methods=["POST"])
def generar_numeros():

    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No se recibió JSON válido"}), 400
    
    

    generador = sgn.GeneradorNumeros(data)
    vector_numeros = generador.generarVectorDeNumeros()

   
    return jsonify({
        "numerosGenerados": vector_numeros
    })

@app.route("/generar-histograma", methods=["POST"])
def generar_histograma():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No se recibió JSON válido"}), 400
    
    

    generador_hist = sgn.GenerarDatosHistograma(data)
    datos_histograma = generador_hist.generar_datos_histograma_object()
   
    return jsonify({
        "datosHistograma": datos_histograma
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
