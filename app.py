from flask import Flask, render_template, request, url_for
import json

app = Flask(__name__)

#wpisy = [
#    {
#        'autor': 'Robert Bielicki',
#        'tytuł': 'Nauka Flask',
#        'zawartość': 'Tu jest zawartość',
#        'data_posta': '20.11.2022'
#    },
#    {
#        'autor': 'Natalia Marcińczyk',
#        'tytuł': 'Bear',
#        'zawartość': 'Misiowa zawartość',
#        'data_posta': '20.11.2022'
#    }
#]
#
#with open("wpisy.json", "w", encoding='utf-8') as f:
#    json.dump(wpisy, f, ensure_ascii=False)


with open("wpisy.json","r") as f:
    wpisy = json.load(f)


@app.route('/')
@app.route('/home')               # można dodać dwie routy do tej samej strony
def home():
    return render_template("home.html",wpisy=wpisy, title='Home')


@app.route('/about')
def about():
    return render_template("about.html", title='About')


if __name__ == '__main__':
    app.run(debug=True)


#app = Flask(__name__)
#
#lista_liczb = [4, 2, 5, 3, 3, 5, 7, 7, 7, 7, 1, 2, 2, 2, 2, 2, 2, 2, 2]
#
#@app.route('/', methods=['GET', 'POST'])
#def strona_główna():
#
#    if request.method == 'GET':
#        return render_template("index.html")
#
#    else:
#        if 'pierwsza' in request.form:
#            pierwsza = int(request.form['pierwsza'])
#            if pierwsza in lista_liczb:
#                wystąpienia_1 = lista_liczb.count(pierwsza)
#            else:
#                wystąpienia_1 = 'Brak podanej liczby na liście'
#
#        if 'druga' in request.form:
#            druga = int(request.form['druga'])
#            if druga in lista_liczb:
#                wystąpienia_2 = lista_liczb.count(druga)
#            else:
#                wystąpienia_2 = 'Brak podanej liczby na liście'
#
#        return render_template("wyniki.html", wystąpienia_1=wystąpienia_1, wystąpienia_2=wystąpienia_2)
#

