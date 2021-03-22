# CeneoScrapper

## Etap 1
### 1. Analiza struktury opinii w serwisie [ceneo.pl](https://www.ceneo.pl)

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|--------|------------|--------------|----------|
|Opinia|div.js_product-review|opinion||
|Id opinii|['data-entry-id']|opinion_id||
|Autor|span.user-post__author-name|author||
|Rekomendacja|span.user-post__author-recomendation > em|recomendation||
|Liczba gwiazdek|span.user-post__score-count|stars||
|Treść opinii|div.user-post__text|content||
|Lista wad|div.review-feature__col:has(> div.[class*='negatives']) > div.review-feature__item|cons||
|Lista zalet|div.review-feature__col:has(> div.[class*='positives']) > div.review-feature__item|pros||
|Czy podtwierdzona|div.review-pz|purchased||
|Data wystawienia|span.user-post__published > time:nth-chid(1)["datetime"]|submit_date||
|Data zakupu|span.user-post__published > time:nth-chid(2)["datetime"]|purchase_date||
|Dla ilu osób przydatna|span[id^='votes-yes']|useful||
|Dla ilu osób nieprzydatna|span[id^='votes-no']|useless||

### 2. Pobranie składowych pojedynczej opinii
- pobranie kodu strony
- wyodrębnienie z kodu strony pojedynczej opinii
- pobranie do pojedynczych zmiennych