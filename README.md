# CeneoScrapper

## Etap 1
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

### Etap 2. Ekstrakcja wszystkich opinii  o produkcie z pojedynczej strony
-
## Etap 3. Ekstrakcja wszystkich opinii  o produkcie z wszystkich stron
-