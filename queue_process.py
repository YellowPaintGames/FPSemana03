from collections import deque
words=deque()
ask=""
ask=input("Dê um conjunto de palavras, SEPARADAS POR ESPAÇOS: ")
for word in ask.split():
    words.appendleft(word)
print(words)
while words:
    aux=words.pop()
    if "a" in aux:
        print(aux)