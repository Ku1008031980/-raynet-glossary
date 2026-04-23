tech_dictionary = { 
"Python": "A high-level programming language.", 
"Git": "A distributed version control system." 
} 
def list_terms(): 
for term, desc in tech_dictionary.items(): 
print(f"{term}: {desc}") 
list_terms()  