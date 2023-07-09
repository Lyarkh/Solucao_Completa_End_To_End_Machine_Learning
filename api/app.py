from flask import Flask
import joblib
import sqlite3
from datetime import datetime


app = Flask(__name__)
# Carregando modelo treinado para a predição
modelo = joblib.load('data/modells/modelo_random_florest_v1.pkl')

conexao_db = sqlite3.connect('Banco_dados_API.db')
cursor = conexao_db.cursor()

@app.route('/predicao/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods=['GET'])
def root(area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax):
    inicio = datetime.now()

    lista_de_parametros = [area, rooms, bathroom, parking_spaces, floor, animal, furniture, hoa, property_tax]
    lista_de_parametros_tratado = [float(x) for x in lista_de_parametros]

    try:
        predicao = modelo.predict([lista_de_parametros_tratado])
        lista_de_parametros.append(predicao)

        fim = datetime.now()
        processamento = fim - inicio

        insert_dados = f'''
            INSERT INTO Log_APi (Inputs, Inicio, Fim, Processamento) VALUES
            ({str(lista_de_parametros_tratado)}, {inicio}, {fim}, {processamento})
        '''

        cursor.execute(insert_dados)
        conexao_db.commit()
        
        return {'valor_aluguel': str(predicao)}
    except:
        return {'aviso': 'erro ao fazer a predicao'}


if __name__ == '__main__':
    app.run(debug=True)
