Na początku myślalem że skrzynka do tworzenia pętli
musi sąsiadować ze skrzyżowaniem (
miejscem które było odwiedzone poziomo i pionowo
).
Otóż nie,option four z przykładu :) 
Option three jest strasznie wkurwiająca.

Nowa hipoteza:
Aby miejsce mogło być takim, że jak się wstawi
przeszkodę to się wpada w cykl, prostopadły do obecnego
kierunku rząd lub kolumna, musi mieć elementy
trasy (pokonanej do tej pory)
UWAGA zgodne z kierunkiem i zwrotem po 
hipotetycznym obrocie!!!
Czyli np. dobre miejsce na przeszkodę jest wtedy kiedy:
idziesz sobie w lewo, (orientacja monitora)
i patrząc w twoje prawo (kolumna), ma pola
które były już odwiedzone, i na których
szedłeś w górę.
Nie trzeba weryfikować cełej kolumny/rzędu
jedynie te na prawo od ciebie.
Można by zrobić słownik, w którym trzymasz numer każdej kolumny i każdego rzędu.
Dla k kolumn i r rzędów będzie w nim k+r kluczy.
Wartości to flaga że dany rząd/kolumna był już odwiedzany:
z góry na dół, z dołu na górę, z lewa na prawo 
i z prawa na lewo (4 różne flagi).
Z każdym krokiem sprawdzasz po prostu czy dany
rząd/kolumna na prawo od ciebie ma 
odpowiednią flagę (wtedy wstawienie przeszkody,
o ile jest na nią miejsce) wywoła cykl.

PROBLEM 1
jak idziesz w lewo, to w kolumnie naprzeciwko ciebie
może być ścieżka w której szedłeś w górę zaznaczona.
Ale mogłeś ją iść na lewo od ciebie, to nam nie da cyklu.
Musi być na prawo.
A to oznacza że w tym słowniku można by kluczom
przypisywać nie pojedyncze wartości a naprzykład
przedziały.
NP w kolumnie numer 4 szedłeś (0;6), (8;10)
i (27;21).
TZN szedłem od pola 0 w dół do 6.
Szedłem od pola 8 w dół do 10
Szedłem od pola 27 w górę do 21.
Effectively to będzie taka jakby lista wektorów.
Dobrze by było liczyć ile się robi kroków

PROBLEM 2
Między tobą a tym przedziałem, 
który doprowadziłby do cyklu nie może być
przeszkody. No i niestety znowu sprowadza się
nam to do przeglądania wszystkich pól od ciebie
do prawej... Chyba że albo mielibyśmy zapisane
też pozycje wszystkich przeszkód.
A oprócz tego można też to trochę usprawnić
(Ale to na potem ew)
że sprawdzasz tylko jak w tym słowniku na 
odpowiedniej pozycji coś jest.
Dla takiej rzadkiej macierzy (pustej planszy)
to może mocno zredukować złożoność obliczeniową
Więc wracajmy do czytania wszystkiego.
Można by zacząć zaznaczać pola zamiast kreskami lub
X-ami literkami.
u - pole odwiedzane było idąc "upwards"
d - odwiedzane downwords
l - leftwords
r - rightwords
Pole może być też np (l,u) oznaczać to najlepiej przez
sety myślę.