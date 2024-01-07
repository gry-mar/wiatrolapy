import pandas as pd
import spacy
from collections import Counter

_topics_map = {
'trybunał konstytucyjny': ["trybunał", "konstytucyjny", ' tk ', ' trybunal '], 
'opozycja': ["opozycja", "trzeci droga", " ko ", "platforma obywatelski", "lewica", 'koalicja'],
'współpraca z Unią Europejską': ["unia europejska", 'unia', "europejski", 'unijny'],
'rząd pis (prawo i sprawiedliwość)': ["pis", "prawo i sprawiedliwość", "pisowiec", "rząd pis", 'pisorgpl', 'kaczyński'],
'publiczna opieka zdrowotna (nfz)': [" nfz ", 'publiczny opieka zdrowotny', 'pacjent', 'szpital', 'medyczny'],
'niezależność sądów (sądownictwo)': [" sąd ", "niezależny sąd", 'niezależność sąd", "sądownictwo', 'sędzia', 'krsa'],
'osoby z niepełnosprawnościami': ["niepełnosprawni"], 
'prawa kobiet': ["prawo kobieta"],
'dotacje dla rolników': ["wsparcie rolnik", "rolnicy", "dotacja dla rolnik", 'rolnik', 'gospodarstwo', 'dlapolskiejwsi', 'agrokluby'], 
'gospodarka odpadowa (śmieci)': ["odpad", "śmieć", "wywóz śmieć", 'smród', 'składowisko'],    
'odnawialne źródła energii': ["energia atomowy", "wolny energia", "odnawialny źródło energia", "fotowoltaik", "energia wiatrowy", "biomasa", 'słońce', 'energetyka'],
'wzmocnienie wojska polskiego': ["zwiększyć wydatek na wojsko", "wsparcie wojsko", 'wzmocnienić wojsko polski', "wojsko", "obronność", 'mblaszczak', 'armia'],
'podwyższenie wieku emerytalnego': ["wiek emerytalny", "emerytura", 'podwyższyć wiek emerytalny', 'emerytalny'], 
'program 500 plus': ['program 500 plus', '500 plus', '500plus'], 
'węgiel': ['węgiel'],
'edukacja seksualna (wdż)': ['edukacja seksualny', " wdż ", "wychowanie do życie w rodzina"],
'ustawa o ograniczeniu biurokracji i barier prawnych': ['ustawa o ograniczyć biurokracja i bariera prawny', 'biurokracja'], 
'inflacja': ['inflacja', 'tarczaantyinflacyjny' ],
'prowadzenie działalności gospodarczej': ["działalność gospodarczy", 'prowadzić działalność gospodarczy'],
'ZUS': [' zus ', "zakład ubezpieczenie społeczny"],
'zmiany klimatyczne': ["klimat", "strajk klimatyczny", "globalny ocieplenie"], 
'telewizja publiczna (tvp)': ["telewizja publiczny", "telewizja polski", 'tvp'],
'przyjmowanie imigrantów': ["imigrant", "przyjmować imigrant", 'stopprzymusowejrelokacji', 'migracyjny', 'relokacja'],
'aborcja': ['pro life', 'pro choice', 'aborcja', 'płód', 'nienarodzony'],
'szczepienia': ['szczepić', 'szczepienie', 'szczepienie na covid', 'przymusowy szczepienie', 'zaszczepić się'],
'rozdział kościoła od państwa': ["świecki państwo", "świecki", 'świeckie', 'rozdział kościół od państwo', "kościół"]
}

nlp = spacy.load("pl_core_news_md")

def _find_topic_lemmatized_spacy(text):
    lemmatized_text = " ".join([token.lemma_.lower() for token in nlp(text)])
    for topic, keywords in _topics_map.items():
        if any(keyword in lemmatized_text for keyword in keywords):
            return topic
    return "inne"  # If no topic is found


def classify_text_fragments(df: pd.DataFrame, new_topic_col: str):
    df[new_topic_col] = df['text'].apply(_find_topic_lemmatized_spacy)
    return df

def get_topics_list():
    return list(_topics_map.keys())



def get_most_common_words_per_topic(df, topic_col):
    topics_list = get_topics_list()
    for topic in topics_list:
        topic_text = " ".join(df[df[topic_col] == topic]['text'])
        doc = nlp(topic_text)
        words = [token.lemma_.lower() for token in doc if token.is_alpha]
        word_counts = Counter(words)
        print(f"Topic: {topic}")
        for word, count in word_counts.most_common(30):
            print(f"{word}: {count}")
        print("\n")