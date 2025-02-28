from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)
file_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(file_path)

@app.route('/datos', methods=['GET'])
def get_all_data():
    return jsonify(df.to_dict(orient='records'))

@app.route('/datos/<int:id>', methods=['GET'])
def get_data_by_id(id):
    result = df[df['ID'] == id]
    if not result.empty:
        return jsonify(result.to_dict(orient='records')[0])
    return jsonify({"error": "ID no encontrado"}), 404

@app.route('/')
def home():
    return jsonify({"mensaje": "Bienvenido a la API de sensores. Usa /datos para ver los datos."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)