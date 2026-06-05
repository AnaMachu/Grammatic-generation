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

sentences = [
    "Maria gosta musica",
    "Maria não lê livro",
    "Maria lê livro e Maria mora Brasil e você gosta musica",
    "eles não estudam ingles",
    "o menino bom inteligente fala português",
    
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
        print(f"  SEM AMBIGUIDADE — 1 árvore encontrada\n")
        trees[0].pretty_print()
    else:
        print(f"  AMBÍGUA — {len(trees)} árvores encontradas!\n")
        for i, tree in enumerate(trees, 1):
            print(f"  --- Árvore {i} ---")
            tree.pretty_print()
