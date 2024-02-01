from flask import Flask, render_template, request, redirect                                   # Flask żeby działał Flask, render_template do 
                                                                                    # używania html, request do komunikacji między
########################                                                            # plikami potrzebnej do funkcjonowania logowania.

'''
def Create_app():                                                                   # Funkcja definiująca aplikację, używana do
    app = Flask(__name__)                                                           # skonfigurowania bardziej skomplikowanych rzeczy,
    app.config['SECRET_KEY'] = "admin"                                              # na przykład bezpieczne hasło, ścieżka do bazy 
    return app                                                                      # danych itp. Niepotrzebne do labladorów. 

app = Create_app()
'''

app = Flask(__name__)                                                               # Tyle wystarczy na aplikację.

baza_danych = {                                                                     # Baza danych zawierająca loginy i hasła. 
    'Lekarz' : 'Haslo123' ,                                                         # Słownik ze względu na to, że atrybuty mają 
    'admin' : 'admin' ,                                                             # przypisane zmienne i atrybuty (loginy) nie 
    'haslo' : 'ptakilatajakluczem'                                                  # mogą się powtarzać. 
}


                                                                                    # Lista która jest wypisywana w lablador.html.
labradory = [
    "Labradory to rasa psów, która zdobyła serca ludzi na całym świecie ze względu na swoje wyjątkowe cechy." , 
    "Charakteryzują się przyjacielskim usposobieniem, co czyni je doskonałymi towarzyszami zarówno dla rodzin, " ,
    "jak i osób samotnych. Znane są z niezwykłej inteligencji oraz chęci nauki, co sprawia, że są łatwe do szkolenia." ,
    "Labradory są również pełne energii i entuzjazmu, co sprawia, że świetnie sprawdzają się jako towarzysze " , 
    "do aktywności na świeżym powietrzu. Niezależnie od swojego zastosowania czy to jako wierny towarzysz," , 
    "pies ratowniczy czy też doskonały pracownik labradory zawsze emanują radością i oddaniem."
]


########################

@app.route('/')                                                                     # Domyślna ścieżka otwierająca się po połączeniu
def home():                                                                         # ze stroną.
    return render_template('home.html')                                             # Plik w folderze 'templates', który zostanie 
                                                                                    # wyświetlony na stronie.
@app.route('/lablador')
def lablador():
    return render_template('lablador.html' , tekst = labradory )
    #return render_template('lablador.html', tekst = labradory)

@app.route('/logowanie', methods = ['POST' , 'GET'])                                # Metody sprawiające że możemy i wysyłać do 
def login():                                                                        # i odbierać dane z pliku home.html
    login = request.form['username']                                                # Przypisanie zmiennej do tego, co wpisał 
    haslo = request.form['password']                                                # użytkownik.
    if login not in baza_danych:                                                    # Sprawdzenie, czy login w ogóle jest w 
        return render_template('home.html' , infozwr = "nieprawidłowy login")       # słowniku. 
    else:                                                                           # Jeśli tak : 
        if haslo != baza_danych[login]:                                             # Sprawdzenie czy hasło jest przypisane do 
            return render_template('home.html' , infozwr = "nieprawidłowe hasło")   # wybranego loginu w słowniku.
        else:                                                                       # Jeśli tak : 
            return redirect('/lablador')                                            # Przekierowanie do strony o labladorach. 
                      
########################

if __name__ == '__main__':                                                          #nieskończona pętla włączająca aplikację.
    app.run(debug=True)
