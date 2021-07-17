from flask import Flask
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


@app.route("/")
@app.route("/homepage")
def homepage_blog():
    return render_template("my_blog.html", titlu="Blogul meu 2021", articole=articole)


@app.route("/adauga_articol")
def adaugare_articol():
    nr_articolului = len(articole) + 1
    data_curenta = str(date.today())
    return render_template("adaugare_articol.html", titlu="Adauga un nou articol",
                           nr_articolului=nr_articolului, data_curenta=data_curenta)


if __name__ == "__main__":
    app.run(debug=True)