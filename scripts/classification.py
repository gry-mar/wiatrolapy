import openai
import os
import dotenv


api_key = os.environ.get("API_KEY")

openai.api_key = api_key

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
    "rząd Andrzeja Dudy",
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
    "nowelizacja kodeksu wyborczego",
    "ustawa o ograniczeniu biurokracji i barier prawnych",
    "wojna na ukrainie",
    "obniżenie podatków",
    "organizacje pozarządowe",
    "ZUS",
    "prowadzenie działalności gospodarczej",
    "pozwolenie na broń",
    "ustawa deregulacyjna",
    "prowadzenie działalności nieewidencjonowanej",
    "ograniczenie wystawiania recept",
    "profilaktyka40plus",
    "program leki75+",
    "ustawa o jakości",
    "inicjatywy patriotyczne",
    "ii wojna światowa",
    "projekt e-gabinet+",
    "prowadzenie rejestru ciąż",
    "wiara katolicka",
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
    "sentiment": sentiment / stance towards the topic}.


    Here are four examples that will help you understand the task:

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
                 "sentiment”: „negative”}, 
                 {„text" : „przerywanie ciąży to zdecydowana przesada”,  
                 "topic" : „aborcja”,
                 "sentiment”: „negative”},
                 {„text" : „państwo powinno dofinansowywać in-vitro”,  
                 "topic" : „in-vitro”,
                 "sentiment”: „positive”},
                 {„text" : „i skupiać się na tym żeby więcej dzieci się rodziło niż umierało jeszcze nienarodzonych”,  
                 "topic" : „aborcja”,
                 "sentiment”: „negative”}]".

                 
    Example 4:
    Input: "bardzo dziękuję panu prezydentowi za tak istotne przemówienie podczas dzisiejszych obrad. panie prezydencie! panie premierze! wysoka izbo! dostojni goście! to jest chwila, w której jako przedstawiciele narodu stajemy przed naszymi rodakami i przed społecznością poza granicami polski, której jesteśmy częścią. polacy zawsze czuli, że niepodległość jest najwyższą wartością. bez względu na różnice polityczne wszystkich nas musi łączyć miłość do ojczyzny i wola negowania zbrodni przeciwko polsce. sejm jest do tych obowiązków najlepiej przygotowany, bo zdecydowana większość polaków chce jedności opartej na wartościach narodowych i zgodnych z wiarą chrześcijańską. to właśnie tutaj należy wcielić w życie program odbudowy silnej armii. zwracam się do wszystkich o odrzucenie tego negowania niepodległego państwa polskiego i fundamentów katolicyzmu. trzeba zbudować silne państwo w pełni patriotyzmu. 


    Output: "[{„text" : „sejm jest do tych obowiązków najlepiej przygotowany, bo zdecydowana większość polaków chce jedności opartej na wartościach narodowych i zgodnych z wiarą chrześcijańską”,  
                 "topic" : „katolicyzm”,
                 "sentiment”: „positive”}, 
                 {„text" : „to właśnie tutaj należy wcielić w życie program odbudowy silnej armii,”,  
                 "topic" : „wzmocnienie wojska polskiego”,
                 "sentiment”: „positive”},
                 {„text" : „zwracam się do wszystkich o odrzucenie tego negowania niepodległego państwa polskiego i fundamentów katolicyzmu”,  
                 "topic" : „katolicyzm”,
                 "sentiment”: „positive”}]".
    """
    
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
            {"role": "system", "content": system_content},
            {"role": "user", "content": content}

        ]
        )
    return response.choices[0].message.content.replace("\n", "")



