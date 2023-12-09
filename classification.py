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
    "rząd pis (prawo i sprawiedliwość)",
    "inflacja",
    "przyjmowanie imigrantów",
    "społeczność LGBT",
    "węgiel",
    "program 500 plus",
    "program 800 plus",
    "mieszkanie plus",
    "podwyższenie wieku emerytalnego",
    "gospodarka odpadowa (śmieci)",
    "WOŚP",
    "jurek owsiak",
    "feminizm",
    "edukacja seksualna",
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
    "równość płac względem płci",
    "zwiększenie wydatków na wojsko",
    "trybunał konstytucyjny",
    "niezależność sądów (sądownictwo)",
    "tabletka dzień po",
    "rządy tuska",
    "strajk kobiet",
    "rządy po (platforma obywatelskaj)",
    "wzrost cen paliw",
    "strajk nauczycieli",
    "referendum",
    "antysemityzm",
    "współpraca z Unią Europejską",
    "współpraca z USA (Stany Zjednoczone)",
    "rząd Andrzeja Dudy",
    "pegasus",
    "marsz niepodległości",
    "tvn",
    "komunizm", 
    "osoby z niepełnosprawnościami"
]



def analyze_text(text: str) -> str:

    system_content = """
     You are helpful assistant with massive knowledge about Polish politics. You spend the whole days for last 40 years reading political tweets and watching Parliament sessions. You've read all tweets that were ever posted on Twitter. This is your only job, just to read about Polish politics. You are not offensive.
    """

    content = """
    In the text given below find fragments that covers one of provided topics."""  + f"""

    Text: {text}


    Topics: {topics_a}


    """+"""
    Try to use topics from the list, but if you are unable to classify the text into any of the given topics, use your judgment to determine the topic based on context. Do NOT make up topic that doesn't match text. If it's hard to determine topic return empty JSON object.
    Then determine the sentiment towards that topic as negative, positive and neutral.
    Return the results as a list of JSON objects, where each object has fields:


    {"text" : text fragment,  
    "topic" : determined topic,
    "sentiment": sentiment}.




    Here are three examples that will help you understand the task:

    
    Example 1:
    Input text: "od lat wiadomo że pis to partia ogromnej imigracji poza wszelką kontrolą"


    Output JSON: "[{"text" : „od lat wiadomo że pis to partia ogromnej imigracji poza wszelką kontrolą”,  
                 "topic" : „rząd pis (prawo i sprawiedliwość)”,
                 "sentiment”: negative}, 
                 {"text" : „od lat wiadomo że pis to partia ogromnej imigracji poza wszelką kontrolą”,  
                 "topic" : „przyjmowanie imigrantów”,
                 "sentiment”: negative}]".

                 


    Example 2:
    Input text: „pan minister grzebalczyk z pisu nie zawiódł to nie jest samolot tylko kadłub samolotu jednostka ma być w pełni wyposażona i przygotowana do eksploatacji pod koniec 2026 roku”


    Output JSON: "{"text" : „pan minister grzebalczyk z pisu nie zawiódł to nie jest samolot tylko kadłub samolotu jednostka ma być w pełni wyposażona i przygotowana do eksploatacji pod koniec 2026 roku”,  
                 "topic" : „rząd pis (prawo i sprawiedliwość)”,
                 "sentiment”: „positive”}".
    
                 

                 
    Example 3:
    Input text: „W głowach wam się poprzewracało z tym feminizmem przerywanie ciąży to zdecydowana przesada państwo powinno dofinansowywać in-vitro i skupiać się na tym żeby więcej dzieci się rodziło niż umierało jeszcze nienarodzonych”


    Output JSON: "[{„text" : „W głowach wam się poprzewracało z tym feminizmem”,  
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

    # content = f"""
    # Poniższa lista zawiera pary klucz - wartość reprezentujące tematy (klucze) i przykładowe słowa kluczowe odnoszące się do danego tematu (wartości), które pozwalają go lepiej zrozumieć.

    #     {topics}


    # Znajdź w podanym poniżej tekście fragmenty odpowiadające na jeden z tematów zawartych w liście oraz określ stosunek autora tekstu do wypowiedzi jako  pozytywny, negatywny lub neutralny. Staraj się wykorzystywać te tematy, jednak jeśli nie jesteś w stanie zaklasyfikować tekstu do żadnego z podanych tematów spróbuj wyciągnąć go z tekstu.


    #     {text}
    # """ + """
    
    # Zwróć wyniki jako listę obiektów JSON, gdzie każdy obiekt posiada pola:

    #     "{"text" : fragment dostarczonego tekstu,  
    #     "topic" : temat wypowiedzi,
    #     "sentiment”: stosunek autora do wypowiedzi}."



    ## Do NOT make up topic that doesn't match text. If it's hard to determine topic return empty JSON object.



     
    # Poniżej zawarto dwa przykłady:

    # Przykład pierwszy:
    # Tekst wejściowy: 
    #     „pis jest znany z przecinania wstęgi po kilka razy więc i pan minister gróbarczyk nie zawiódł to nie jest prom tylko kadłub promu jednostka ma być w pełni wyposażona i przygotowana do eksploatacji pod koniec 2024 roku”


    # Wyjście:
    #     {"text" : „pis jest znany z przecinania wstęgi po kilka razy więc i pan minister gróbarczyk nie zawiódł to nie jest prom tylko kadłub promu jednostka ma być w pełni wyposażona i przygotowana do eksploatacji pod koniec 2024 roku”,  
    #     "topic" : „rządy pis”,
    #     "sentiment”: „pozytywny”}.

        

    # Przykład drugi:
    # Tekst wejściowy:
    # „W głowach wam się poprzewracało z tym feminizmem przerywanie ciąży to zdecydowana przesada państwo powinno dofinansowywać in-vitro i skupiać się na tym żeby więcej dzieci się rodziło niż umierało jeszcze nienarodzonych”


    # Wyjście:
    # [{„text" : „W głowach wam się poprzewracało z tym feminizmem”,  
    #     "topic" : „feminizm”,
    #     "sentiment”: „negatywny”}, 
    # {„text" : „przerywanie ciąży to zdecydowana przesada”,  
    #     "topic" : „aborcja”,
    #     "sentiment”: „negatywny”},
    # {„text" : „państwo powinno dofinansowywać in-vitro”,  
    #     "topic" : „in-vitro”,
    #     "sentiment”: „pozytywny”},
    # {„text" : „i skupiać się na tym żeby więcej dzieci się rodziło niż umierało jeszcze nienarodzonych”,  
    #     "topic" : „aborcja”,
    #     "sentiment”: „negatywny”}].

    # """
    
    if len(text) <= 10000:
        model = 'gpt-3.5-turbo'
    elif len(text) > 10000 and len(text) < 46000:
        model = 'gpt-3.5-turbo-16k'
    else:
        model = "gpt-4-1106-preview"

    response = openai.chat.completions.create(
        model=model,
        temperature=0.45,
        messages=[
            # {"role": "system", "content": system_content},
            {"role": "user", "content": content}

        ]
        )
    return response.choices[0].message.content.replace("\n", "")



