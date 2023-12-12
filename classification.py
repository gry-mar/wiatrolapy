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

topics_a = [
    "aborcja",
    "rząd pis (partia prawo i sprawiedliwość)",
    "inflacja to wina pis",
    "afera wizowa",
    "inflacja",
    "przyjmowanie imigrantów",
    "LGBT (społeczność LGBT, queer, homoseksualizm itp.)",
    "prawa kobiet",
    "węgiel",
    "program 500 plus",
    "program 800 plus",
    "mieszkanie plus",
    "podwyższenie wieku emerytalnego",
    "gospodarka odpadowa (śmieci)",
    "WOŚP",
    "jurek owsiak",
    "feminizm",
    "edukacja seksualna (wdż)",
    "legalizacja marihuany",
    "telewizja publiczna (tvp)",
    "dotacje dla rolników",
    "odnawialne źródła energii",
    "energia atomowa",
    "in vitro",
    "zmiany klimatyczne", 
    "opozycja",
    "platforma obywatelska",
    "obowiązkowe szczepienia na covid",
    "wołyń",
    "rozdział kościoła od państwa",
    "związki partnerskie",
    "publiczna opieka zdrowotna (nfz)",
    "smoleńsk",
    "pomoc humanitarna na Ukrainie",
    "równość płci",
    "wzmocnienie wojska polskiego",
    "trybunał konstytucyjny",
    "niezależność sądów (sądownictwo)",
    "tabletka dzień po",
    "rządy tuska",
    "strajk kobiet",
    "wzrost cen paliw",
    "strajk nauczycieli",
    "referendum",
    "antysemityzm",
    "współpraca z Unią Europejską",
    "współpraca z USA (Stany Zjednoczone)",
    "rząd Andrzeja Dudy (prezydenta)",
    "pegasus",
    "marsz niepodległości",
    "tvn",
    "komunizm", 
    "osoby z niepełnosprawnościami",
    "współpraca z Niemcami",
    "obniżenie podatków",
    "stan wojenny",
    "program polski ład",
    "dochód nauczycieli",
    "NATO",
    "reparacje wojenne",
    "nowelizacja kodeksu wyborczego"
]



def analyze_text(text: str) -> str:

    system_content = """
     You are helpful assistant with knowledge about Polish politics and economy. In past few months you have been studying polish Tweets and parliamentary sessions to be able to provide clear, unbiased information about political related topics.
    """

    content = """
    In the provided text find fragments that cover one of provided topics."""  + f"""

    Text: {text}


    Topics: {topics_a}


    """+"""
    Try to use topics from the list, but if you are unable to classify the text into any of the given topics, use your judgment to determine the topic based on contex of the text. Do NOT make up topic that doesn't match text. If it's hard to determine topic return JSON objest with empty topic and sentiment fields.
    Then determine the sentiment towards that topic as negative, positive or neutral.
    Return the results as a list of JSON objects, where each object has fields:


    {"text" : text fragment,  
    "topic" : determined topic,
    "sentiment": sentiment}.


    Here are three examples that will help you understand the task:

    Example 1:
    Input: "od lat wiadomo że pis to partia ogromnej imigracji poza wszelką kontrolą"


    Output: "[{"text" : „od lat wiadomo że pis to partia ogromnej imigracji poza wszelką kontrolą”,  
                 "topic" : „rząd pis (prawo i sprawiedliwość)”,
                 "sentiment”: negative}, 
                 {"text" : „od lat wiadomo że pis to partia ogromnej imigracji poza wszelką kontrolą”,  
                 "topic" : „przyjmowanie imigrantów”,
                 "sentiment”: negative}]".


                 
    Example 2:
    Input: „pan minister grzebalczyk z pisu nie zawiódł to nie jest samolot tylko kadłub samolotu jednostka ma być w pełni wyposażona i przygotowana do eksploatacji pod koniec 2026 roku”


    Output: "[{"text" : „pan minister grzebalczyk z pisu nie zawiódł to nie jest samolot tylko kadłub samolotu jednostka ma być w pełni wyposażona i przygotowana do eksploatacji pod koniec 2026 roku”,  
                 "topic" : „rząd pis (prawo i sprawiedliwość)”,
                 "sentiment”: „positive”}]".
    
                 
 
    Example 3:
    Input: „W głowach wam się poprzewracało z tym feminizmem przerywanie ciąży to zdecydowana przesada państwo powinno dofinansowywać in-vitro i skupiać się na tym żeby więcej dzieci się rodziło niż umierało jeszcze nienarodzonych”


    Output: "[{„text" : „W głowach wam się poprzewracało z tym feminizmem”,  
                 "topic" : „feminizm”,
                 "sentiment”: „negatywny”}, 
                 {„text" : „przerywanie ciąży to zdecydowana przesada”,  
                 "topic" : „aborcja”,
                 "sentiment”: „negatywny”},
                 {„text" : „państwo powinno dofinansowywać in-vitro”,  
                 "topic" : „in-vitro”,
                 "sentiment”: „pozytywny”},
                 {„text" : „i skupiać się na tym żeby więcej dzieci się rodziło niż umierało jeszcze nienarodzonych”,  
                 "topic" : „aborcja”,
                 "sentiment”: „negatywny”}]".
    """
    
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
            {"role": "system", "content": system_content},
            {"role": "user", "content": content}

        ]
        )
    return response.choices[0].message.content.replace("\n", "")



