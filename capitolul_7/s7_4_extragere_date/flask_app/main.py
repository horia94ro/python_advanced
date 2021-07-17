from flask import Flask, request, redirect
from flask import render_template
from datetime import date
app = Flask(__name__)
articole = [
    {
        "titlu": "Primul meu articol",
        "autor": "John Sutton",
        "data_adaugare": "2021-02-01",
        "continut": "Articol de test pentru pagina noastra de blog"
    },
    {
        "titlu": "Astazi este frumos afara",
        "autor": "David DeSanto",
        "data_adaugare": "2021-02-10",
        "continut": "Cred ca voi merge sa alerg prin parc"
    },
    {
        "titlu": "Recomandare film: Ma",
        "autor": "John Sutton",
        "data_adaugare": "2021-02-01",
        "continut": "Ma este un film horror/thriller."
    }
]
autori = []

@app.route("/")
@app.route("/homepage")
def homepage_blog():
    return render_template("my_blog.html", titlu="Blogul meu 2021", articole=articole)


@app.route("/adauga_articol", methods=['GET', 'POST'])
def adaugare_articol():
    if request.method == 'GET':
        nr_articolului = len(articole) + 1
        data_curenta = str(date.today())
        return render_template("adaugare_articol.html", titlu="Adauga un nou articol",
                               nr_articolului=nr_articolului, data_curenta=data_curenta,
                               autori=autori)
    elif request.method == 'POST':
        #Extragem datele din formular, folosindu-ne de valorile atributului name de pe fiecare
        #câmp în parte
        titlu = request.form['titlu']
        autor = request.form['autor']
        data_adaugare = request.form['data_articol']
        continut = request.form['continut']
        #Construim dicționarul corespunzător noului articol
        articol_nou = {"titlu": titlu, "autor": autor, "data_adaugare": data_adaugare,
                       "continut": continut}
        #Adăugăm articolul chiar la începutul listei
        articole.insert(0, articol_nou)
        return redirect('/')


@app.route('/adauga_autor', methods = ['GET', 'POST'])
def adaugare_autor():
    if request.method == 'POST':
        nume = request.form['nume']
        prenume = request.form['prenume']
        nume_complet = nume + " " + prenume
        autori.append(nume_complet)
        return redirect("/")
    else:
        return render_template("adaugare_autor.html")
if __name__ == "__main__":
    app.run(debug=True)
