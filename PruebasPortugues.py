import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

grammar = CFG.fromstring("""
    oracao -> oracao_simples oracao_prima
    oracao -> oracao_simples

    oracao_prima -> conjuncao oracao_simples oracao_prima
    oracao_prima -> conjuncao oracao_simples

    oracao_simples -> assunto oracao_int

    oracao_int -> verbo oracao_int2
    oracao_int -> 'não' verbo objeto

    oracao_int2 -> objeto
    oracao_int2 ->

    assunto -> pronome assunto_primo
    assunto -> pronome
    assunto -> nome assunto_primo
    assunto -> nome
    assunto -> artigo nome assunto_primo
    assunto -> artigo nome

    assunto_primo -> adjetivo assunto_primo
    assunto_primo -> adjetivo

    pronome -> 'eles' | 'você'
    nome -> 'Maria' | 'menino'
    artigo -> 'a' | 'o'
    adjetivo -> 'bom' | 'inteligente'
    conjuncao -> 'e' | 'mas'
    verbo -> 'gosta' | 'fala' | 'mora' | 'estudam' | 'lê'

    objeto -> preposicao substantivo
    objeto -> artigo substantivo
    objeto -> substantivo

    preposicao -> 'de' | 'no'
    substantivo -> 'musica' | 'ingles' | 'livro' | 'Brasil' | 'português'
""")

parser = nltk.ChartParser(grammar)

test_cases = [
    # Oraciones simples SVO
    ("Maria gosta musica",                          "ACEPTADA"),
    ("você mora no Brasil",                         "ACEPTADA"),
    ("eles fala português",                         "ACEPTADA"),
    ("o menino lê livro",                           "ACEPTADA"),
    ("Maria lê a musica",                           "ACEPTADA"),
    # Oraciones simples SV
    ("Maria gosta",                                 "ACEPTADA"),
    ("eles estudam",                                "ACEPTADA"),
    ("você mora",                                   "ACEPTADA"),
    # Oraciones con não
    ("Maria não gosta de livro",                    "ACEPTADA"),
    ("eles não fala português",                     "ACEPTADA"),
    ("o menino não lê livro",                       "ACEPTADA"),
    # Oraciones con adjetivos en assunto 
    ("o menino bom lê livro",                       "ACEPTADA"),
    ("o menino bom inteligente lê livro",           "ACEPTADA"),
    ("Maria bom gosta musica",                      "ACEPTADA"),
    ("Maria bom inteligente gosta musica",          "ACEPTADA"),
    # Oraciones compuestas con 'e' 
    ("Maria lê livro e você mora no Brasil",        "ACEPTADA"),
    ("eles estudam e Maria gosta musica",           "ACEPTADA"),
    # Oraciones compuestas con 'mas'
    ("Maria gosta musica mas eles estudam",         "ACEPTADA"),
    ("você mora no Brasil mas Maria lê livro",      "ACEPTADA"),
    # Cadena de 3 cláusulas
    ("Maria lê livro e você mora no Brasil e eles estudam", "ACEPTADA"),

    # orden incorrecto
    ("gosta Maria musica",                          "RECHAZADA"),
    ("musica Maria gosta",                          "RECHAZADA"),
    # falta verbo
    ("Maria musica",                                "RECHAZADA"),
    ("o menino livro",                              "RECHAZADA"),
    # Rnão sin objeto 
    ("Maria não musica",                            "RECHAZADA"),
    ("Maria não gosta",                             "RECHAZADA"),
    ("",                                            "RECHAZADA"),
]

print("=" * 70)
print(f"{'ORAÇÃO':<45} {'ESPERADO':<12} {'RESULTADO'}")
print("=" * 70)

passed = 0
failed = 0

for sentence, expected in test_cases:
    if sentence.strip() == "":
        result = "RECHAZADA"
    else:
        try:
            tokens = sentence.split()
            trees = list(parser.parse(tokens))
            result = "ACEPTADA" if trees else "RECHAZADA"
        except:
            result = "RECHAZADA"

    status = "OK" if result == expected else "FALLO"
    if result == expected:
        passed += 1
    else:
        failed += 1

    short = sentence[:42] + "..." if len(sentence) > 42 else sentence
    print(f"{short:<45} {expected:<12} {status}")

print("=" * 70)
print(f"Resultado: {passed} correctas, {failed} fallidas de {len(test_cases)} pruebas")
print("=" * 70)
