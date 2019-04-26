# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import nltk.corpus

from textblob import TextBlob as tb

frase = tb("Este é um teste de textblob")

type(frase)

frase.tokens


# Lê o texto e quebra em sentenças
sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
rt = open("D:/Netbiis/Curso_AS/noticia1.txt", "r")
raw_text = rt.read()
sentences = sent_tokenizer.tokenize(raw_text)

type(sentences)

# Mostra as sentenças em português
for sent in sentences:
    print(",,", sent , ">>")


# Traduz as sentenças para o inglês
for sent_en in sentences:
    fi = tb(sent_en)
    se = fi.translate(from_lang ="pt", to = "en")
    print(",,", se , ">>")









