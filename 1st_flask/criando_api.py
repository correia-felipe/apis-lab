from flask import Flask, jsonify
import pandas as pd
import unidecode

df = pd.read_csv('atelie-catalogo-produtos.csv', sep=';')

app = Flask(__name__)

@app.route('/')
def home():
  return 'A API está no ar!'

@app.route('/autores/<autor>')
def pegar_autores(autor):
    df = pd.read_csv('atelie-catalogo-produtos.csv', sep=';')
    df = df.applymap(lambda x: unidecode.unidecode(str(x)))
    df_autor = df[df['Autor'].str.lower() == autor.lower()]
    if not df_autor.empty:
        return jsonify(df_autor.to_dict(orient='records'))
    else:
        return jsonify({'mensagem': 'Autor nao encontrado'})


if __name__ == '__main__':
    app.run(debug=True)