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

# Carrega o SentiLex
sentilexpt = open('D:/Netbiis/Curso_AS/Dataset_PT-BR/SentiLex-PT02/SentiLex-lem-PT02.txt','r')

# Cria dicionário de palavras com polaridade
dic_palavra_polaridade = {}

for i in sentilexpt.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+7:pol_pos+9]).replace(';','')
    dic_palavra_polaridade[palavra] = polaridade

print(dic_palavra_polaridade)

print (dic_palavra_polaridade.get('abusivo'))


# Função para criar score das frases
def Score_sentimento(frase):
    frase = frase.lower()
    l_sentimento = []
    for p in frase.split():
        l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))
    score = sum(l_sentimento)
    if score > 0:
        return 'Positivo, Score:{}'.format(score)
    elif score == 0:
        return 'Neutro, Score:{}'.format(score)
    else:
        return 'Negativo, Score:{}'.format(score)
    
Score_sentimento('Eu estou muito feliz hoje, porém, triste com a politica')
    
# Função para criar score das frases com retorno apenas do score
def Score_sent(frase):
    frase = frase.lower()
    l_sentimento = []
    for p in frase.split():
        l_sentimento.append(int(dic_palavra_polaridade.get(p, 0)))
    score = sum(l_sentimento)
    return score


Score_sent('Eu estou muito feliz hoje, porém, triste com a politica')

score_texto = 0
ss = 0

for frase in sentences:
    ss = Score_sent(frase)
    score_texto = score_texto + ss
    print(ss)
    
print(score_texto)

if score_texto > 0:
    print('Texto positivo, Score:{}'.format(score_texto))
elif score_texto == 0:
    print('Texto neutro, Score:{}'.format(score_texto))
else:
    print('Texto negativo, Score:{}'.format(score_texto))

    






