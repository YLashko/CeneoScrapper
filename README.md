# CeneoScrapper

## Etap 1.
### 1. Analiza struktury opinii w serwisie [ceneo.pl](https://www.ceneo.pl)

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion|object|
|Id opinii|['data-entry-id']|opinion_id|str|
|Autor|span.user-post__author-name|author|str|
|Rekomendacja|span.user-post__author-recomendation > em|recomendation|bool|
|Liczba gwiazdek|span.user-post__score-count|stars|float|
|Treść opinii|div.user-post__text|content|str|
|Lista wad|div.review-feature__col:has(> div.[class*='negatives']) > div.review-feature__item|cons|list|
|Lista zalet|div.review-feature__col:has(> div.[class*='positives']) > div.review-feature__item|pros|list|
|Czy podtwierdzona|div.review-pz|purchased|bool|
|Data wystawienia|span.user-post__published > time:nth-chid(1)["datetime"]|submit_date|str|
|Data zakupu|span.user-post__published > time:nth-chid(2)["datetime"]|purchase_date|str|
|Dla ilu osób przydatna|span[id^='votes-yes']|useful|int|
|Dla ilu osób nieprzydatna|span[id^='votes-no']|useless|int|

### 2. Pobranie składowych pojedynczej opinii
- pobranie kodu strony
- wyodrębnienie z kodu strony pojedynczej opinii
- pobranie do pojedynczych zmiennych
- obsługa błędów
- dobranie typów danych do wartości zmiennych

## Etap 2. Ekstrakcja wszystkich opinii  o produkcie z pojedynczej strony
- zapis składowych pojedynczej opinii do słownika
- zdefiniowanie listy do przechowywania wszystkich opinii 
- dodanie pętli, która wykonuje operację ekstrakcji dla wszystkich opinii
## Etap 3. Ekstrakcja wszystkich opinii  o produkcie z wszystkich stron
- dodanie pętli, która pobiera i analizuje kolejne strony z opiniami o produkcie
- dodanie możliwośći podania kodu produktu "z klawiatury"
- dodanie zapisu wszystkich opinii o produkcie do pliku .json
## Etap 4. Refactoring
- zdefiniowanie funkcji pojedynczego elementu opinii
- przygotowanie słownika opisującego składowe opinii wraz z ich selektorami
- tworzenie słownika reprezentującego pojedynczą opinię przy wykorzystaniu wyrażenia słownikowego
## Etap 5. Analiza statystyczna zbioru opinii o produkcie
- wyswietlanie listy produktów, dla których pobrane zostały opinie
- wczytanie opinii o wskazanym produkcie do obiektu DataFrame
- obliczanie podstawowych statystyk
    * średnia ocen produktu
    * liczba opinii o produkcie
    * liczba opinii dla których podana została liczba zalet
    * liczba opinii dla których podana została liczba wad
## Etap 6. Rysowanie wykresów o dane z pobranych opinii
- wykres słupkowy/kolumnowy obrazujący częstość występowania opinii z poszczególnymi ocenami
- wykres kołowy obrazujący udział poszczególnych rodzajów rekomendacji w zbiorze opinii