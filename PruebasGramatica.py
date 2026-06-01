import nltk
from nltk import CFG
nltk.download('punkt')
nltk.download('punkt_tab')

grammar = CFG.fromstring("""
    oração -> assunto verbo objeto
    oração -> assunto 'não' verbo objeto

    assunto -> pronome
    assunto -> nome
    assunto -> artigo nome

    pronome -> 'eles' | 'você'
    nome -> 'Maria' | 'menino'
    artigo -> 'a' | 'o'

    verbo -> 'gosta' | 'falam' | 'mora' | 'estudam' | 'lê'

    objeto -> preposição substantivo
    objeto -> artigo substantivo
    objeto -> substantivo
    objeto ->

    preposição -> 'de' | 'no'
    substantivo -> 'musica' | 'ingles' | 'livro' | 'Brasil' | 'português'
""")

parser = nltk.ChartParser(grammar)

test_cases = [
    # Válidas — con objeto explícito
    ("Maria gosta musica",           "ACEPTADA"),
    ("você mora no Brasil",          "ACEPTADA"),
    ("eles falam português",         "ACEPTADA"),
    ("o menino lê livro",            "ACEPTADA"),
    ("Maria lê a musica",            "ACEPTADA"),

    # Válidas — objeto vacío (ε)
    ("Maria gosta",                  "ACEPTADA"),
    ("eles estudam",                 "ACEPTADA"),
    ("você mora",                    "ACEPTADA"),

    # Válidas — con negação
    ("Maria não gosta de livro",     "ACEPTADA"),
    ("eles não falam português",     "ACEPTADA"),
    ("o menino não lê livro",        "ACEPTADA"),
    ("Maria não gosta",              "ACEPTADA"),

    # Inválidas
    ("gosta Maria musica",           "RECHAZADA"),  # orden incorrecto
    ("Maria musica",                 "RECHAZADA"),  # falta verbo
    ("Maria não musica",             "RECHAZADA"),  # falta verbo tras não
    ("",                             "RECHAZADA"),  # vacía
]

print("=" * 65)
print(f"{'ORAÇÃO':<40} {'ESPERADO':<12} {'RESULTADO'}")
print("=" * 65)

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

    status = "OK" if result == expected else "✘ FALLO"
    if result == expected:
        passed += 1
    else:
        failed += 1

    short = sentence[:37] + "..." if len(sentence) > 37 else sentence
    print(f"{short:<40} {expected:<12} {status}")

print("=" * 65)
print(f"Resultado: {passed} correctas, {failed} fallidas de {len(test_cases)} pruebas")
print("=" * 65)

print("\n--- Árvores de orações simples ---\n")
simple = [
    "Maria gosta musica",
    "você mora no Brasil",
    "Maria não gosta de livro",
    "Maria gosta",
    "eles estudam",
]
for sentence in simple:
    tokens = sentence.split()
    trees = list(parser.parse(tokens))
    print(f"Oração: '{sentence}'")
    if trees:
        for tree in trees:
            tree.pretty_print()
    else:
        print("  Não foi possível analisar.\n")
