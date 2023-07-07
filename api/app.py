from flask import Flask
import joblib


app = Flask(__name__)
# Carregando modelo treinado para a predição
modelo = joblib.load('data/modells/modelo_random_florest_v1.pkl')


@app.route('/predicao/<parametro>', methods=['GET'])
def root(parametro):

    predicao = modelo.predict()


if __name__ == '__main__':
    app.run(debug=True)
