# Generación de gramáticas

## Descripción
El idioma protugués es estrucuturalmente muy similar al español. 
En esta evidencia nos concentraremos en el tiempo verbal Presente Simple que es en el que se contruyen las oraciones que modelaremos, las cuales son simples y compuestas.

La gramática protuguesa funciona con la estructura SVO 

1. Sujeto(assunto) : Indica quién o qué realiza la acción en la oración. 

2. Verbo : Describe una acción, un estado o un fenómeno natural.

3. Objeto : Sustantivo o frase nominal sobre la cual recae la acción del sujeto.

Entonces una oración simple es definida como: ASSUNTO + VERBO + OBJETO
* Ejemplo:  Eu acuerdo cedo . ("Me levanto temprano").
*Ejemplo: O gato dorme na cama. ("El gato duerme en la cama")

Y una oración compuesta se define como: Oración simple + CONJUNCAO + Oración Simple
* Ejemplo:Maria gosta de música e João gosta de português.
* Ejemplo Eles moram no Brasil e falam português.

Donde los sujetos son nombres (nome) y pronombres (pronome),los verbos describen las acciones que realiza el sujeto, y el objeto puede ser mútliples combinaciones de categorías gramaticales como sustantivos (substantivos)  por si solos o combinados con artículos (artigos) y preposiciones (preposicao).

### Gramática
Según Hopcroft, Motwani y Ullman (2006), una gramática es una descripción formal de un lenguaje que especifica cómo pueden construirse cadenas válidas mediante un conjunto de reglas de producción. Una gramática está compuesta por símbolos terminales, símbolos no terminales, un símbolo inicial y un conjunto de producciones. Los terminales son los símbolos básicos que aparecen en las cadenas finales del lenguaje y no pueden ser reemplazados por otros símbolos, mientras que los no terminales representan categorías o estructuras intermedias que pueden expandirse mediante las reglas de producción. A partir de estas reglas es posible construir un árbol sintáctico, una representación jerárquica que muestra cómo una cadena es generada desde el símbolo inicial hasta llegar a los terminales. En dicho árbol, los nodos internos corresponden a símbolos no terminales y las hojas a símbolos terminales, permitiendo visualizar la estructura sintáctica de una expresión u oración y facilitando su análisis por parte de compiladores y procesadores de lenguaje.
#### CFG
Una Gramática Libre de Contexto (Context-Free Grammar, CFG) es un conjunto de reglas de producción utilizado para describir lenguajes en los que cada regla reemplaza un único símbolo no terminal por una cadena de símbolos terminales y no terminales. Formalmente, una CFG está compuesta por un conjunto de terminales, un conjunto de no terminales, un símbolo inicial y un conjunto de producciones. Estas gramáticas son especialmente importantes porque permiten modelar estructuras jerárquicas presentes en lenguajes de programación y lenguajes naturales, siendo además la base teórica de los analizadores sintácticos empleados en compiladores. Sipser (2012)

#### EBNF
La Forma Extendida de Backus-Naur (EBNF) es una notación que amplía la BNF tradicional mediante la incorporación de operadores que permiten expresar repeticiones, alternativas y elementos opcionales de manera más concisa. Su objetivo es simplificar la especificación de gramáticas al reducir el número de producciones necesarias para describir la sintaxis de un lenguaje. Gracias a estas extensiones, EBNF resulta especialmente útil para documentar lenguajes de programación y sistemas de procesamiento de lenguaje, ya que mejora la legibilidad y el mantenimiento de las gramáticas sin modificar su capacidad descriptiva.

#### Modelo 
Se busca que este subconjunto de gramática del portugués sea capaz de generar las siguientes oraciones:
* Maria gosta de música
* Eles estudam português
* Você mora do Brasil 
* O menino lê  o livro 
* Eles não falam inglês

Y basado en las reglas del portugues está ha sido mi producción de modelo 

<img width="834" height="439" alt="image" src="https://github.com/user-attachments/assets/47c7777f-2c7f-4660-b4bc-b44a17c400c0" />

Sin embargo, la gramática presentada aquí tiene dos problemas, es ambigua y tiene recursividad izquierda. Estos problemas serán corregidos a continuación.

### Ambigüedad
Según Aho, Lam, Sethi y Ullman (2007), una gramática es ambigua cuando existe al menos una cadena del lenguaje que puede derivarse mediante dos o más árboles sintácticos diferentes. La ambigüedad representa un problema en el diseño de compiladores porque una misma entrada puede interpretarse de distintas maneras, generando incertidumbre sobre su significado. Para eliminarla, es común reescribir la gramática incorporando reglas que establezcan explícitamente la precedencia y asociatividad de los operadores o separando las construcciones en diferentes niveles sintácticos. De esta forma, cada cadena válida posee una única derivación y un único árbol sintáctico, permitiendo un análisis sintáctico determinista y sin interpretaciones múltiples.

Primero se debe identificar que parte de la gramática es aquella que causa este problema así que se ha probado con la implementación en [PortuguesAmbiguo.py](PortuguesAmbiguo.py)  y como output se ha detectado que 
al querer generar la oración 'Maria lê livro e Maria mora Brasil e você gosta musica' nos damos cuenta que hay más de un árbol sintáctico capaz de generarlo 
<img width="1116" height="791" alt="image" src="https://github.com/user-attachments/assets/017d939d-3525-43f6-918b-88adc67d35ba" />

Y se ha identificado que el probelma radica aquí:
<n> oração → oração conjunção oração <n>
ya que hay dos manera de hacer esta oración: Maria lê livro e Maria mora Brasil e você gosta musica 

* (Maria lê livro e Maria mora Brasil) e você gosta musica
* Maria lê livro e (Maria mora Brasil e você gosta musica)
Por lo tanto se determinó que es una gramática ambigua



### Recursión izquierda
Según Aho, Lam, Sethi y Ullman (2007), una gramática presenta recursión izquierda cuando un no terminal puede derivar una cadena cuyo símbolo más a la izquierda es él mismo. Un ejemplo típico es la producción A → Aα | β, donde A aparece nuevamente al inicio de su propia derivación. Este tipo de construcciones genera problemas en los analizadores sintácticos descendentes, ya que pueden entrar en ciclos infinitos al intentar expandir las producciones. Para eliminar la recursión izquierda directa, la gramática se transforma introduciendo un nuevo no terminal auxiliar. Así, una producción de la forma A → Aα | β se reescribe como A → βA' y A' → αA' | ε, conservando el lenguaje generado pero permitiendo un análisis sintáctico eficiente y libre de ciclos.

en mi gramática se identificó en estas dos lineas :
* oração → oração conjunção oração
oração se llama a sí misma en la posición más izquierda 
* assunto → assunto adjetivo
assunto se llama a sí misma en la posición más izquierda

## Modelo 
El modelo final de la gramática una vez fue removida la ambigüedad, recusrión izquierda y  fue simplificada es esta:
<img width="291" height="263" alt="image" src="https://github.com/user-attachments/assets/da47db1a-033a-4edb-a1f9-0062d49d319b" />


## Implementatción 
Se encuentra en el archivo. Este código funciona de la siguiente manera:

[Portugues.py](Portugues.py)

## Pruebas
Las purebas automatizadas están en [PruebasGramatica.py](PruebasGramatica.py) y solo se necesita correr el archivo.
Es importante tener la librería ntlk instalada.

Aquí se observan ejemplos de oraciones válidad con resultado exitoso 

Aquí hay oraciones inválidad con resultados negativo

## Parser LL(1) Princeton 

### Tabla First Follow
### Tabla de análisis LL1
### Ejemplo de árboles 

## Analysis de Chomsky
La Jerarquía de Chomsky es un sistema de clasificación de gramáticas y lenguajes formales propuesto por Noam Chomsky para describir distintos niveles de complejidad sintáctica. Esta jerarquía se divide en cuatro categorías: gramáticas regulares (Tipo 3), libres de contexto (Tipo 2), sensibles al contexto (Tipo 1) y no restringidas (Tipo 0). Cada nivel posee una mayor capacidad de representación que el anterior, por lo que los lenguajes de una categoría incluyen a los de las categorías inferiores. Esta clasificación resulta fundamental en teoría de la computación porque establece la relación entre los tipos de gramáticas y los modelos computacionales capaces de reconocer los lenguajes que generan, como los autómatas finitos, los autómatas de pila y las máquinas de Turing. Además, proporciona una base teórica para el diseño de compiladores, analizadores sintácticos y sistemas de procesamiento de lenguajes formales.
<img width="763" height="476" alt="image" src="https://github.com/user-attachments/assets/2080ea25-741a-4dae-9141-e98ebb524f21" />

<img width="666" height="453" alt="image" src="https://github.com/user-attachments/assets/f7edadce-3033-4ebb-a97d-12e1ef90efce" />


## Referencias
Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, Techniques, and Tools (2nd ed.). Pearson.
Sipser, M. (2012). Introduction to the Theory of Computation (3rd ed.). Cengage Learning.
Appel, A. W. (2002). Modern Compiler Implementation in Java (2nd ed.). Cambridge University Press.
Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). Introduction to Automata Theory, Languages, and Computation (3rd ed.). Pearson Education.

