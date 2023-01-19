import random as r
class dict:
    #diccionario={'1':'S', '2':'R', '3':'N', '4':'D', '5':'L', '6':'A'}

    def biblio(self):
        diccionario={'1':'S', '2':'R', '3':'N', '4':'D', '5':'L', '6':'A'}
        var = r.choice(list(diccionario.values()))
        #var2 = str(var)
        print(var)
        return var
        

    #def __init__(self):
      #  variable_letra = self.biblio()
      #  vari = str(variable_letra)
      #  print(vari)