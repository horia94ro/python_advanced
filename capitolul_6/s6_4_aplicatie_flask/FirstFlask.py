from flask import Flask, jsonify

app = Flask(__name__)

filme = [{'id': 1, 'titlu': 'Titanic', 'durata': 223, 'castigator_oscar': True},
         {'id': 2, 'titlu': 'The Departed', 'durata': 123, 'castigator_oscar': False},
         {'id': 3, 'titlu': 'Inception', 'durata': 102, 'castigator_oscar': True}]

@app.route('/')
def hello_world():
    return "<h1>HELLO WORLD!</h1>"

@app.route('/despre')
def info_project():
    return "<h2>Acesta este primul meu proiect in Flask!</h2>"

@app.route('/filme')
def toate_filmele():
    return jsonify(filme)

@app.route('/filme/<int:film_id>')
def extrage_film(film_id):
    filmul_meu = {}
    for film in filme:
        if film['id'] == film_id:
            filmul_meu = film
            break
    return jsonify(filmul_meu)



if __name__ == "__main__":
    app.run(debug=True)