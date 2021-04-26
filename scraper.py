import requests
from bs4 import BeautifulSoup
import json

def extract_element(opinion, selector, attribute = None):
    try:
        if attribute:
            if isinstance(attribute, str):
                return opinion.select(selector).pop(0)[attribute].strip()
            else:
                return [x.get_text().strip() for x in opinion.select(selector)]
        else:
            return opinion.select(selector).pop(0).get_text().strip()
    except IndexError:
        return attribute

selectors = {
            "author" : ['span.user-post__author-name'],
            "recommendation" : ['span.user-post__author-recomendation > em'],
            "stars" : ['span.user-post__score-count'],
            "content" : ['div.user-post__text'],
            "pros" : ["div.review-feature__col:has(> div[class*=\"positives\"]) > div.review-feature__item", True],
            "cons" : ["div.review-feature__col:has(> div[class*=\"negatives\"]) > div.review-feature__item", True],
            "purchased" : ['div.review-pz'],
            "submit_date" : ["span.user-post__published > time:nth-child(1)"],
            "purchase_date" : ["span.user-post__published > time:nth-child(2)"],
            "useful" : ["span[id^='votes-yes']"],
            "useless" : ["span[id^='votes-no']"]
        }

extracted_opinions = []
product_code = input('Podaj kod produktu: ')
current_page = (f'https://www.ceneo.pl/{product_code}/opinie-1')
while current_page:

    respons = requests.get(current_page)

    page_dom = BeautifulSoup(respons.text, 'html.parser')

    opinions = page_dom.select('div.js_product-review')

    for opinion in opinions:

        opinion_elements = {key:extract_element(opinion, *args) for key, args in selectors.items()}

        opinion_elements['opinion_id'] = opinion['data-entry-id']

        opinion_elements['stars'] = float(opinion_elements['stars'].split('/')[0].replace(',', '.'))
        opinion_elements['recommendation'] = True if opinion_elements['recommendation'] == 'Polecam' else False if opinion_elements['recommendation'] == 'Nie Polecam' else None
        opinion_elements['purchased'] = bool(opinion_elements['purchased'])
        opinion_elements['useful'] = int(opinion_elements['useful'])
        opinion_elements['useless'] = int(opinion_elements['useless'])
        extracted_opinions.append(opinion_elements)

    try:
        current_page = 'https://www.ceneo.pl' + page_dom.select('a.pagination__next').pop()['href']
    except IndexError:
        current_page = None
    print(current_page)

with open(f'opinions/{product_code}.json', 'w', encoding='UTF-8') as fp:
    json.dump(extracted_opinions, fp, indent=4, ensure_ascii=False)