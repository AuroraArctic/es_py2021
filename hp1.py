from pprint import pprint
import json
import nltk.corpus
from nltk.corpus import stopwords
#nltk.download('stopwords')
#nltk.download("punkt")
#nltk.download("averaged_perceptron_tagger")
prepositions = stopwords.words()


#with open("prepositions.json") as j:
#    data = json.loads(j.read())

with open("hp1.txt", "r") as f:
    line = f.readline()
    s = set()
    dizio = {}
    verbs = []
    while line != "":
        if line == "\n" or line.isupper():
            line = f.readline()  
            continue
        
        # line = line.replace(";", " ")
        line = line.replace(";", " ").replace("'", " ")
        # line = line.replace(";", " ").replace("'s", " ")
        line = line.replace("!",  " ").replace("@",  " ").replace("#",  " ")
        line = line.replace("$",  " ").replace("%",  " ").replace("^",  " ")
        line = line.replace("&",  " ").replace("*",  " ").replace("(",  " ")
        line = line.replace(")",  " ").replace("[",  " ").replace("]",  " ")
        line = line.replace("{",  " ").replace("}",  " ").replace("\"", " ")
        line = line.replace(":",  " ").replace(",",  " ").replace(".",  " ")
        line = line.replace("/",  " ").replace("<",  " ").replace(">",  " ")
        line = line.replace("?",  " ").replace("\\", " ").replace("|",  " ")
        line = line.replace("`",  " ").replace("~",  " ").replace("-",  " ")
        line = line.replace("=",  " ").replace("_",  " ").replace("+",  " ")
        line = line.replace("  ", " ")
        
        # prima di dividere il testo in parole mi creo una lista di tuple per ogni riga
        text = nltk.word_tokenize(line)
        lista_tuple = nltk.pos_tag(text)
        for l in lista_tuple:
            # print(f"{l[1]}: {l[0]}")
            if l[1].startswith("VB") or l[1].startswith("MD"):
                verbs.append(l[0])
        lista = line.split()
        for el in lista:
            if el.lower() not in prepositions and el.lower() not in verbs:
                if el not in s:
                    s.add(el)
                    dizio[el] = 1
                else:
                    dizio[el] += 1        
        line = f.readline()  
    
    

    new_lista = [(k,v) for k,v in dizio.items()]
    new_lista.sort(key = lambda c: c[1], reverse = True)
    
    pprint(new_lista[:100])

    with open("new_lista.json", "w") as n:
        json.dump(new_lista, n, ensure_ascii=False, indent=4) # trasforma le tuple in lista

    # nw = new_lista[:40]
    # xs = [c[0] for c in nw]
    # ys = [c[1] for c in nw]
    
    # sns.histplot(x=xs, y=ys)
    # sns.histplot(nw, x=xs, y=ys)




# # import pandas to use pandas DataFrame 
# import pandas as pd 
  
# # data in the form of list of tuples 
# data = [('Peter', 18, 7), 
#         ('Riff', 15, 6), 
#         ('John', 17, 8), 
#         ('Michel', 18, 7), 
#         ('Sheli', 17, 5) ] 
  
  
# # create DataFrame using data 
# df = pd.DataFrame(data, columns =['Name', 'Age', 'Score']) 

# print(df)  




