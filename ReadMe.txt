01.02.2024 Czwartek

Changelog : 

1. Dodano najbrzydszy CSS po tej stronie Wisły.  

2. Naprawiono błąd z niewyświetlaniem się obrazka:
Przeniesiono obrazek do folderu static żeby Flask go widział. 

3. Naprawiono błąd z listą na "/lablador"
Przyczyną przez którą nie wyświetlała się lista był błąd : 
funkcja login(), po podaniu poprawnego loginu i hasła, zwracała "lablador.html", przez co po prostu renderowano
plik html bez uruchamiania żadnego kodu w funkcji lablador() podpiętej pod @app.route('/lablador'). 
Błąd naprawiono zastępując "return render_template("lablador.html)" przez "return redirect('/lablador').


09.01.2024 wtorek
Zarówno w tym pliku jak i w kodzie wszystko opisuję tak obwicie aby jaknajlepiej zakomunikować co już 
potrafię, a czego się jeszcze muszę nauczyć (bo taki jest częściowy cel tego zadania, żeby Pa... żebyś 
wiedział na jakim "poziomie" jestem). 

KK
---
Cel : 

"
Wiec tak się zastanawiałem, to tak zadanie na święta będzie następujące, 
korzystając z instrukcji warunkowej oraz z technologii flask oraz z poznanym elementów takich jak słowniki, 
krotki oraz listy, zrób mi stronę logowania, w której informacje na temat loginów oraz haseł będą zawierać 
krotki oraz listy, po zalogowaniu prosta strona witająca nas informacjami, które zrobisz mi w słowniku, 
na temat rasy psów labradorów, jak dasz radę dodaj obrazek labradora, może być z linku internetowego.
"

Zadanie było na święta, nie powinienem był to odkładać do piątku. Od piątku przez weekend próbowałem zrobić sprawę
od końca i próbowałem się nauczyć jak się robi bazę danych na loginy i hasła, blueprinty, SQL, autoryzację, hashowanie
haseł itp. Zajęłoby to wiele dłużej do nauczenia. 
Pliki które teraz wysłałem zostały w 100% napisane dziś w 4h od 18:30 do 20:30 mniej wiecej. 


---
Napotkałem na problemy które trudno mi rozwiązać samemu i uznałem że poproszę o pomoc w debugowaniu bo naprawdę nie rozumiem : 

1. Część z logowaniem działa, zero problemów. 

2. Część z wyświetlaniem informacji na temat labradorów :
 - nie wyświetla się obrazek
	- próbowałem na różne sposoby : link bezpośrednio do internetu, bezpośrednia ścieżka, przeniesienie
	  obrazka do innych folderów w projekcie, zmianę obrazka na inny, zmianę rozszerzenia. Nie wiem dlaczego 
	  nie działa. 
 - lista nie wyświetla się "poprawnie" : 
   "...witająca nas informacjami, które zrobisz mi w słowniku..." - rozwiązanie, które aktualnie jest w kodzie
   nie spełnia wymagania wykorzystania słownika. Dopiero pisząc ten tekst zorientowałem się że miałem użyć słownika. 
   Jeśli trzeba, to zmienię listę na słownik.  
   Tak czy siak, zamiast tego użyłem listy : nazywa się labradory[], znajduje się w app.py. Chciałem spełnić warunek
   wykorzystania... uznajmy listy przywołując ją z app.py do pliku labrador.html, a następnie wymienić ją za pomocą 
   prostej pętli for wykonującej akcję za/for każdy element listy (żeby pokazać, że wiem jak się te listy robi).
   Pętla nic nie wyświetla, więc wkleiłem tekst prosto do html. 