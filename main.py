#Mustafa Alperen ARMUTCUOĞLU
#Kerem Uysal
# Raynet Junior Tech Glossary 
tech_dictionary = { 
    "Docker": "A containerization platform that allows you to package and run applications in isolated environments with all their necessary dependencies.",
    "Proxy": "An intermediary server that sits between a user and the internet to forward requests, often used for anonymity, caching, or security filtering.",
    "Microservices": "A weakness or flaw in software, hardware, or processes that can be exploited by a threat actor to gain unauthorized access.",

    "C#": "It is a modern programming language developed by Microsoft, especially used in application and game development.",
    "C++": "It is a powerful programming language developed by Bjarne Stroustrup, used for high-performance systems and games.",
    "flutter": "It is a UI framework developed by Google that enables building mobile, web, and desktop applications with a single codebase.",
} 
def list_terms(): 
    for term, desc in tech_dictionary.items(): 
        print(f"{term}: {desc}") 
list_terms() 