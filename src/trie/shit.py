'''
Created on 15/06/2017

@author: ernesto
XXX: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/tutorial/
'''


import logging
import fileinput
import string

nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None
raiz_trie = None


class nudo():
    def __init__(self, letra):
        self.peso_n = 0
        self.letra = letra
        self.apuntadores = {}
    
    def anadir_nudo(self, valor_letra, nodo):
        self.apuntadores[valor_letra] = nodo
    
    def __str__(self):
        return "puto nudo %s valor %u" % (self.letra, self.peso_n)
        
def trie_shit_construie(lista_cadenas):
    global raiz_trie
    raiz_trie = nudo(None)
    
    logger_cagada.debug("la lista a procesar %s" % lista_cadenas)
    
    for cadena, peso in lista_cadenas:
        tamano_cadena = 0
        nueva_secuencia = False
        nodo_actual = None
        
        nodo_actual = raiz_trie
        logger_cagada.debug("anadiendo cadena %s q tiene peson %u" % (cadena, peso))
        
        
        tamano_cadena = len(cadena.strip())
        for idx, digito in enumerate(cadena.strip()):
            nodo_encontrado = None
            valor_digito = 0
            
            valor_digito = digito
            logger_cagada.debug("verificando digito %s de valor %s" % (digito, valor_digito))
            
            if(nueva_secuencia):
                nuevo_nodo = nudo(valor_digito)
                nodo_actual.anadir_nudo(valor_digito, nuevo_nodo)
                nodo_actual = nuevo_nodo
                logger_cagada.debug("creando nueva seq")
            else:
                nodo_encontrado = nodo_actual.apuntadores.setdefault(valor_digito, None)
                nueva_secuencia = not nodo_encontrado
                if(nodo_encontrado):
                    nodo_actual = nodo_encontrado
                else:
                    nuevo_nodo = nudo(valor_digito)
                    nodo_actual.anadir_nudo(valor_digito, nuevo_nodo)
                    nodo_actual = nuevo_nodo
                    logger_cagada.debug("a partir del digito %s es una cadena nueva" % digito)
            if(idx == tamano_cadena - 1):
                logger_cagada.debug("poniendo el valor %u en el nodo %s" % (peso, nodo_actual))
                nodo_actual.peso_n = peso
        
        logger_cagada.debug("se termino de procesar mamada")

mierda={}
def trie_shit_dfs(nodo_inicial):
    global raiz_trie
    global mierda
    ia_vistos = set()
    stacaca = []
    caracteres_stacaca = []
    maxima_caca = 0
    cadena_maxima = ""
    if(nodo_inicial in mierda):
        return mierda[nodo_inicial]
    
    stacaca.append(nodo_inicial)
    while(stacaca):
        nodo_act = stacaca.pop()
        logger_cagada.debug("nodo act %s" % nodo_act)
        if(nodo_act in ia_vistos):
            caracteres_stacaca.pop()
            logger_cagada.debug("el nodo %s ia valio verga" % nodo_act)
        else:
            ia_vistos.add(nodo_act)
            stacaca.append(nodo_act)
            for ijo_puta in nodo_act.apuntadores:
                if(nodo_act.apuntadores[ijo_puta]):
                    stacaca.append(nodo_act.apuntadores[ijo_puta])
            logger_cagada.debug("agregados ijos de puta de %s" % nodo_act)
            caracteres_stacaca.append(nodo_act.letra)
            logger_cagada.debug("en ese puto la cadenita es %s" % caracteres_stacaca)
            if(nodo_act.peso_n > maxima_caca):
                cadena_maxima = "".join(caracteres_stacaca)
                maxima_caca = nodo_act.peso_n
                logger_cagada.debug("vaia mierda el max aora %s valor %u" % (cadena_maxima, maxima_caca))
                
    logger_cagada.debug("vaia mierda el max total aora %s valor %u" % (cadena_maxima, maxima_caca))
    
    return (cadena_maxima, maxima_caca)
            
def trie_shit_encuentra_nodo(querie):
    global raiz_trie
    encontrado = False
    
    nodo_act = raiz_trie
    for cacar in querie:
#        assert cacar in nodo_act.apuntadores, "puta madre, el caracter %s no esta en el puto %s, q tiene apuntadores %s" % (cacar, nodo_act, nodo_act.apuntadores)
        if(cacar in nodo_act.apuntadores):
            nodo_act = nodo_act.apuntadores[cacar]
        else:
            nodo_act = None
            break
    
    return nodo_act
    
        
def trie_shit_core(lista_cadenas, queries):
    global raiz_trie
    maximas_mierdas = []
    
    trie_shit_construie(lista_cadenas)
    
    for querie in queries:
        nodo_base = trie_shit_encuentra_nodo(querie)
        if(nodo_base):
            logger_cagada.debug("el nodo base de consulta %s es %s" % (nodo_base, querie))
            sufijo, valor_max = trie_shit_dfs(nodo_base)
#            maximas_mierdas.append(querie[:-1] + sufijo)
            maximas_mierdas.append(valor_max)
        else:
            maximas_mierdas.append(-1)
        
    logger_cagada.debug("respuestas pendejas %s" % maximas_mierdas)
    return maximas_mierdas
        
def trie_shit_main():
    idx_linea = 0
    numero_cadenas = 0
    num_queries = 0
    lineas = []
    lineas = list(fileinput.input())
    lista_cadenas = []
    queries = []
    
    numero_cadenas, num_queries = [int(x) for x in lineas[idx_linea].strip().split(" ")]
    
    idx_linea += 1
    
    for idx_cadena in range(numero_cadenas):
        cadenita = lineas[idx_cadena]
        cadena, peson = lineas[idx_linea].strip().split(" ")
        lista_cadenas.append((cadena, int(peson)))
        idx_linea += 1
    logger_cagada.debug("las cadenas %s" % lista_cadenas)
    
    
    for idx_querie in range(num_queries):
        querie = lineas[idx_linea]
        queries.append(querie.strip())
        idx_linea += 1
        
    logger_cagada.debug("las putas queries %s" % queries)
    
    cacas = trie_shit_core(lista_cadenas, queries)
    
    for caca in cacas:
        print(caca)
    
if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    trie_shit_main()
