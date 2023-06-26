# Testowanie-adnotacja-typow

Powyższe programy zostały wykonane w celu: 
- Zapoznanie z paradygmatem obiektowym w Python
- Zapoznanie z kaczym typowaniem w Python
- Zapoznanie się z adnotacją typami w języku Python z użyciem narzędzia mypy
- Zapoznanie z pisaniem testów jednostkowych z wykorzystaniem modułu pytest

W ramach kodu zaimplementowano: 
- klasę SSHLogEntry reprezentującą pojedynczy wpis dziennika SSH. Klasa pozwala na
reprezentację informacji o czasie, opcjonalnej nazwie hosta, surowej treści wpisu, numerze
PID.
- klasy dziedziczące po SSHLogEntry. Klasy reprezentują:
    - a. Odrzucenie hasła
    - b. Akceptację hasła
    - c. Błąd
    - d. Inną informację
- klasę SSHLogJournal, która służy do agregowania SSHLogEntry w wewnętrznej liście.
Zdefiniowano w niej magiczne metody, takie jak __len__, __iter__ ,__contains__ tak, aby można było po niej
iterować jak po sekwencji. Zdefiniowano metodę append(), która przyjmuje na wejściu ciąg znaków, tworzy z
niego odpowiedni obiekt SSHLogEntry, dokonuje jego walidacji, i dodaje do wewnętrznej listy.
-  klasę SSHUser reprezentującą użytkownika. Klasa pozwala na
przechowywanie informacji o nazwie użytkownika i dacie ostatniego logowania. Zdefiniowano w niej metodę 
validate(), która będzie walidować poprawność nazwy użytkownika.
Następnie pobierano kilka instancji SSHLogEntry z SSHLogJournal i utworzono kilka instancji klasy SSHUser.
Przechowano wszystkie instancje na wspólnej liście. Można zademonstrować działanie kaczego typowania poprzez
iterację po tej liście i wywoływanie metody validate().

Dokładny opis działania wraz w wywołaniami znajduje się w pliku przyklady-dzialania-2.pdf
