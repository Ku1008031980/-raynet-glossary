# Raynet Junior Tech Glossary 
tech_dictionary = { 

    "C#": "It is a modern programming language developed by Microsoft, especially used in application and game development.",
    "C++": "It is a powerful programming language developed by Bjarne Stroustrup, used for high-performance systems and games.",
    "flutter": "It is a UI framework developed by Google that enables building mobile, web, and desktop applications with a single codebase.",
} 
def list_terms(): 
    for term, desc in tech_dictionary.items(): 
        print(f"{term}: {desc}") 
list_terms() 