from polyglot.detect import Detector

mixed_text = u"""
China (simplified Chinese: 中国中国中国中国中国中国中国中国中国中国中国; traditional Chinese: 中國),
officially the People's Republic of China (PRC), is a sovereign state
¡Hola ! Mi nombre es Ana. Tengo veinticinco años. Vivo en Miami, Florida
located in East Asia. Ainda é cedo amor, mal começaste a conhecer a vida... ouça me bem amor, preste atenção, o mundo é um moinho
"""

for line in mixed_text.strip().split():
    print(line)
    for language in Detector(line).languages:
        print(language)
print('-----------------------------------------------------------------------------')

for language in Detector(mixed_text).languages:
    print(language)