# Raynet Junior Tech Glossary 
tech_dictionary = { 
    "Örnek": "Örnek açıklama",
    "C#": "Microsoft tarafindan gelistirilen, ozellikle uygulama ve oyun gelistirmede kullanilan modern bir programlama dilidir.",
    "C++": "Bjarne Stroustrup tarafindan gelistirilen, yuksek performansli sistemler ve oyunlar icin kullanilan guclu bir programlama dilidir.",
    "flutter": "Google tarafindan gelistirilen, tek kodla mobil, web ve masaustu uygulamalari yapmayi saglayan bir UI frameworkudur.",
} 
def list_terms(): 
    for term, desc in tech_dictionary.items(): 
        print(f"{term}: {desc}") 
list_terms() 