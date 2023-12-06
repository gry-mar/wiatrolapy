import openai
import os
import dotenv


api_key = os.environ.get("API_KEY")

openai.api_key = api_key

topics = [
    "aborcja", "tabletka dzień po",
    "500plus", "800plus",
    "prawa kobiet", "równość płac", "feminizm",
    "lgbt",
    "Imigranci", "relokacja",
    "granica polsko-białoruska", "płot",
    "Rosja",
    "Ukraina",
    "USA", "Stany Zjednoczone",
    "Unia Europejska",
    "Inflacja",
    "TVP", "telewizja polska", "telewizja publiczna",
    "TVN",
    "Kościół",
    "NFZ", "publiczna opieka zdrowotna",
    "Covid",
    "Edukacja seksualna",
    "Podatki",
    "Emerytura",
    "In-vitro",
    "ZUS",
    "sądownictwo",
    "węgiel",
    "marihuana",
    'referendum',
    "pis",
    "korupcja",
    "koalicja",
    "platforma",
    "po",'platforma obywatelska'
    "ko",
    "opozycja",
    "prawa zwiweząt",
    "prawa człowieka",
    "wybory",
    'konfederacja',
    'lewica',
    'trzecia droga',
    'prawica',
    'lewica',
    'prawa obywateli',
    'kukiz',
    'mieszkanie+',
    '500+',
    '800+',
    'wośp', 
    'tusk',
    'transport publiczny',
    'kampania wyborcza',
    'media',
    'Inwestycje drogowe',
    'świeckie państwo',
    'solidarność',
    'Patriotyzm',
    'kurator',
    'kuratorium',
    'rząd',
    'psl',
    'antysemityzm', 
    'homofobia',
    'przemoc',
    'paliwo',
    'Podatki', 'Finanse',
    'policja', 'wojsko',
    'NATO',
    'prezydent Andrzej Duda',
    'polityka zagraniczna', 'stosunki międzynarodowe',
    'mieszkanieplus',
    'reformy wyborcze',
    'ZUS',
    'bezpieczeństwo narodowe', 'granica polsko-słowacka',
    'cyberbezpieczeństwo', 
    'Współpraca międzynarodowa', 
    'społeczeństwo',
    'Współpraca wojskowa', 
    'polityka obronna',
    'rolnictwo',
    'energia jądrowa',
    'Inwestycje infrastrukturalne',
    'inwestycje gospodarcze',
    'renowacja zabytków', 
    'Inwestycja lotnicza',
]


def analyze_text(text: str) -> str:

    content = """
    Classify the provided text into one of the provided topics and determine the sentiment towards that topic as negative, positive or neutral. 
    If the text covers multiple topics, return appropriately classified fragments of provided text for each topic along with sentiment analysis. 
    If none of the listed topics apply, use your judgment to determine the topic based on context. 
    Return the results as a list of JSON objects, where each object has fields: 
    {"text" : provided text or text fragment,  
    "topic" : determined topic,
    "sentiment": sentiment}.
    Do NOT make up topic that doesn't match text. If it's hard to determine topic return empty JSON object.
    """ + f" Topics: {topics} Text: {text}"
    
    if len(text) <= 10000:
        model = 'gpt-3.5-turbo'
    elif len(text) > 10000 and len(text) < 46000:
        model = 'gpt-3.5-turbo-16k'
    else:
        model = "gpt-4-1106-preview"

    response = openai.chat.completions.create(
        model=model,
        temperature=0.4,
        messages=[
            {"role": "user", "content": content},
        ]
        )
    return response.choices[0].message.content.replace("\n", "")



