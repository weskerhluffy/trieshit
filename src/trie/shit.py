'''
Created on 15/06/2017

@author: ernesto
XXX: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/tutorial/
'''


import logging
import fileinput
import string

nivel_log = logging.ERROR
nivel_log = logging.DEBUG
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
        
def trie_shit_core(lista_cadenas):
    global raiz_trie
    
    trie_shit_construie(lista_cadenas)
    
        
def trie_shit_main():
    idx_linea = 0
    numero_cadenas = 0
    num_queries = 0
    lineas = []
    lineas = list(fileinput.input())
    lista_cadenas = []
    
    numero_cadenas, num_queries = [int(x) for x in lineas[idx_linea].strip().split(" ")]
    
    idx_linea += 1
    
    for idx_cadena in range(numero_cadenas):
        cadenita = lineas[idx_cadena]
        
        cadena, peson = lineas[idx_linea].strip().split(" ")
        
        lista_cadenas.append((cadena, int(peson)))
        
        idx_linea += 1
    logger_cagada.debug("las cadenas %s" % lista_cadenas)
    
    trie_shit_core(lista_cadenas)
    
if __name__ == '__main__':
    logging.basicConfig(level=nivel_log)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    trie_shit_main()
