from flask import Flask, jsonify, Response, request

app = Flask(__name__)

_id = 4
filme = [{'id': 1, 'titlu': 'Titanic', 'durata': 223, 'castigator_oscar': True},
         {'id': 2, 'titlu': 'The Departed', 'durata': 123, 'castigator_oscar': False},
         {'id': 3, 'titlu': 'Inception', 'durata': 102, 'castigator_oscar': True}]


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


@app.route('/filme/adauga', methods=['POST'])
def adauga_film():
    global _id
    film_nou = request.get_json()
    film_nou.update({"id": _id})
    _id += 1
    filme.append(film_nou)
    return Response(status=201)


@app.route('/filme/sterge/<int:film_id>', methods=['DELETE'])
def sterge_film(film_id):
    for film in filme:
        if film['id'] == film_id:
            filme.remove(film)
            break
    return Response(status=204)


@app.route('/filme/actualizeaza/<int:film_id>', methods=['PUT'])
def actualizeaza_film(film_id):
    filmul_meu = [film for film in filme if film['id'] == film_id]
    filmul_meu = filmul_meu[0]
    filmul_meu['titlu'] = request.json.get('titlu', filmul_meu['titlu'])
    filmul_meu['durata'] = request.json.get('durata', filmul_meu['durata'])
    filmul_meu['castigator_oscar'] = request.json.get('castigator_oscar', filmul_meu['castigator_oscar'])

    return Response(filmul_meu, status=201)


if __name__ == "__main__":
    app.run(debug=True)
