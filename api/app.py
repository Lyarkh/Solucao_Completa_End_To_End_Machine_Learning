from flask import Flask
import joblib


app = Flask(__name__)
# Carregando modelo treinado para a predição
modelo = joblib.load('data/modells/modelo_random_florest_v1.pkl')


@app.route('/predicao/<parametro>', methods=['GET'])
def root(parametro):

    try:
        predicao = modelo.predict()
        return {'valor_aluguel': predicao}
    except:
        return {'aviso': 'erro ao fazer a predicao'}


if __name__ == '__main__':
    app.run(debug=True)
