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

sentences = [
    "Maria gosta musica",
    "você mora no Brasil",
    "eles não estudam ingles",
    "o menino lê a musica",
    "Maria não gosta de livro",
    "Maria lê livro e você gosta musica",
]

for sentence in sentences:
    tokens = sentence.split()
    print(f"\n{'='*60}")
    print(f"Oração: '{sentence}'")
    print('='*60)

    trees = list(parser.parse(tokens))

    if not trees:
        print("  Não foi possível analisar.")
    elif len(trees) == 1:
        print(f"  ✔ SEM AMBIGUIDADE — 1 árvore encontrada\n")
        trees[0].pretty_print()
    else:
        print(f"  ⚠ AINDA AMBÍGUA — {len(trees)} árvores encontradas!\n")
        for i, tree in enumerate(trees, 1):
            print(f"  --- Árvore {i} ---")
            tree.pretty_print()