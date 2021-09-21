from polyglot.detect import Detector
spanish_text = u"""¡Hola ! Mi nombre es Ana. Tengo veinticinco años. Vivo en Miami, Florida. palavras ao vento português digite para pesquisar """
detector = Detector(spanish_text)
print(detector.language)

for language in Detector(spanish_text).languages:
    print(language)