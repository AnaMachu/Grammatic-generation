# Generación y limpieza de gramática 

## Descripción
El idioma protugués es estrucuturalmente muy similar al español. 
En esta evidencia nos concentraremos en el tiempo verbal Presente Simple que es en el que se contruyen las oraciones que modelaremos, las cuales son simples y compuestas.

La gramática protuguesa funciona con la estructura SVO 

1. Sujeto(assunto) : Indica quién o qué realiza la acción en la oración. 

2. Verbo : Describe una acción, un estado o un fenómeno natural.

3. Objeto : Sustantivo o frase nominal sobre la cual recae la acción del sujeto.

Entonces una oración simple es definida como: ASSUNTO + VERBO + OBJETO
* Ejemplo:  Eu acuerdo cedo . ("Me levanto temprano").
* Ejemplo: O gato dorme na cama. ("El gato duerme en la cama")

Y una oración compuesta se define como: Oración simple + CONJUNCAO + Oración Simple
* Ejemplo:Maria gosta de música e João gosta de português.
* Ejemplo Eles moram no Brasil e falam português.

Donde el sujeto(assunto) puede ser nombres (nome) y pronombres (pronome),los verbos describen las acciones que realiza el sujeto, y el objeto puede ser mútliples combinaciones de categorías gramaticales como sustantivos (substantivos)  por si solos o combinados con artículos (artigos) y preposiciones (preposicao).

### Gramática
Según Hopcroft, Motwani y Ullman (2006), una gramática es una descripción formal de un lenguaje que especifica cómo pueden construirse cadenas válidas mediante un conjunto de reglas de producción. Una gramática está compuesta por símbolos terminales, símbolos no terminales, un símbolo inicial y un conjunto de producciones. Los terminales son los símbolos básicos que aparecen en las cadenas finales del lenguaje y no pueden ser reemplazados por otros símbolos, mientras que los no terminales representan categorías o estructuras intermedias que pueden expandirse mediante las reglas de producción. A partir de estas reglas es posible construir un árbol sintáctico, una representación jerárquica que muestra cómo una cadena es generada desde el símbolo inicial hasta llegar a los terminales. En dicho árbol, los nodos internos corresponden a símbolos no terminales y las hojas a símbolos terminales, permitiendo visualizar la estructura sintáctica de una expresión u oración y facilitando su análisis por parte de compiladores y procesadores de lenguaje. 

La compilación comienza con el análisis léxico, donde el código fuente se lee carácter por carácter y se agrupa en unidades significativas llamadas tokens. Estos tokens pasan a la siguiente fase, el análisis sintáctico, que verifica si están organizados de forma válida según las reglas de la gramática. Si la estructura es correcta, se construye un árbol de derivación que representa jerárquicamente cómo se compone el programa. Para que este proceso funcione de manera determinista y sin retrocesos, la gramática debe cumplir dos condiciones previas: no tener ambigüedad ni recursión izquierda.

#### CFG (Context-Free Grammar)
Una Gramática Libre de Contexto (Context-Free Grammar, CFG) es un conjunto de reglas de producción utilizado para describir lenguajes en los que cada regla reemplaza un único símbolo no terminal por una cadena de símbolos terminales y no terminales. Formalmente, una CFG está compuesta por un conjunto de terminales, un conjunto de no terminales, un símbolo inicial y un conjunto de producciones. Estas gramáticas son especialmente importantes porque permiten modelar estructuras jerárquicas presentes en lenguajes de programación y lenguajes naturales, siendo además la base teórica de los analizadores sintácticos empleados en compiladores. Sipser (2012)

#### EBNF (Extended Backus Naur Form)
La Forma Extendida de Backus-Naur (EBNF) es una notación que amplía la BNF tradicional mediante la incorporación de operadores que permiten expresar repeticiones, alternativas y elementos opcionales de manera más concisa. Su objetivo es simplificar la especificación de gramáticas al reducir el número de producciones necesarias para describir la sintaxis de un lenguaje. Gracias a estas extensiones, EBNF resulta especialmente útil para documentar lenguajes de programación y sistemas de procesamiento de lenguaje, ya que mejora la legibilidad y el mantenimiento de las gramáticas sin modificar su capacidad descriptiva.

#### Modelo 

Así que basándome a las reglas gramaticales del portugués, esta ha sido mi propuesta para modelar un subconjunto de la gramática total, se pueden crear oraciones simples y compuestas. 
Algunos ejemplos de las oraciones que se pueden generar son estas:<br>
    * "Maria gosta musica",
    * "Maria não lê livro",
    * "Maria lê livro e Maria mora Brasil e você gosta musica",
    * "eles não estudam ingles",
    * "o menino bom inteligente fala português",

<img width="834" height="439" alt="image" src="https://github.com/user-attachments/assets/47c7777f-2c7f-4660-b4bc-b44a17c400c0" />

Sin embargo, la gramática presentada aquí tiene dos problemas, es ambigua y tiene recursividad izquierda. Estos problemas serán explicados y corregidos a continuación.

### Ambigüedad
Según Aho, Lam, Sethi y Ullman (2007), una gramática es ambigua cuando existe al menos una cadena del lenguaje que puede derivarse mediante dos o más árboles sintácticos diferentes. La ambigüedad representa un problema en el diseño de compiladores porque una misma entrada puede interpretarse de distintas maneras, generando incertidumbre sobre su significado. Para eliminarla, es común reescribir la gramática incorporando reglas que establezcan explícitamente la precedencia y asociatividad de los operadores o separando las construcciones en diferentes niveles sintácticos. De esta forma, cada cadena válida posee una única derivación y un único árbol sintáctico, permitiendo un análisis sintáctico determinista y sin interpretaciones múltiples.

Primero se debe identificar que parte de la gramática es aquella que causa este problema, así que se ha probado con la implementación en [PortuguesAmbiguo.py](PortuguesAmbiguo.py)  y como output se ha detectado que 
al querer generar la oración 'Maria lê livro e Maria mora Brasil e você gosta musica' hay más de un árbol sintáctico capaz de generarlo 
<img width="1116" height="791" alt="image" src="https://github.com/user-attachments/assets/017d939d-3525-43f6-918b-88adc67d35ba" />

Y se ha identificado que el probelma radica aquí:<br>
<img width="437" height="394" alt="image" src="https://github.com/user-attachments/assets/9dec83c1-4bf1-4ec8-b66e-187fd40cf422" />

<n> oração → oração conjunção oração <n> <br>
ya que hay dos manera de hacer esta oración: Maria lê livro e Maria mora Brasil e você gosta musica 

* (Maria lê livro e Maria mora Brasil) e você gosta musica
* Maria lê livro e (Maria mora Brasil e você gosta musica)
Por lo tanto se determinó que es una gramática ambigua y una vez identificado esto, procedemos a quitarselo.
En los árboles se puede apreciar que oracao puede crercer por ambos lados (derecha e izquierda) debido a que oracao inicia y temrina con oracao.

Entonces haré que del lado derecho pueda crecer de una forma controlada y que se llame diferente para que e dirija unicamente por un laso y así haré que ya no sea posible formar uno de los dos árboles, quitando así la ambigüedad.
El método es agregar estados intermedios que indiquen un nivel de precedencia, ya que se deben pasar por niveles obligatoriamente entonces no hay rutas alternas.
como en este ejemplo mostrado en clase:
Original: 

E-> E + E | E * E | id 

Transformed:
E → E + T | T

T → T * F | F

F → id	

Aplicado a nuestra gramática:
* oração → oração conjunção oração| assunto verbo objeto|assunto verbo|asunto 'não' verbos objeto 

Se agregó un "filtro", ahora no se puede formar una oracao al final sin pasar por oracao simple

oração        -> oração conjunção oração_simple  <br>
oração        -> oração_simples<br>            

A pesar de haber corregido lo anterior, aún se identifica otro problema  sigue causando ambigüedad porque hay muchas alternativas que empiezan con assunto y eso puede confunidr al parser.

* oração_simple -> assunto verbo objeto| assunto verbo | assunto 'não' verbo objeto <br>

Así que se separan así <br>
oração_simple -> assunto oração_int <br>
oração_int -> verbo oração_int2 | 'não' verbo objeto <br>
oração_int2 -> objeto <br>

El proceso manual se puede encontrar en [Transformaciones.pdf](Transformaciones.pdf)

Quedando la gramática así por el momento:

<img width="531" height="740" alt="image" src="https://github.com/user-attachments/assets/13836165-38f6-4cbd-b59b-41d8cb4ef3bd" />

Y una vez usando ese cambio de gramática se corre en y se observa como solo hay un árbol para aquella oración habiendo quitado exitosamente la ambigüedad.
<img width="1382" height="494" alt="image" src="https://github.com/user-attachments/assets/2a58238e-6b80-44cb-a405-5f2e5b834ad8" />

### Recursión izquierda
Según Aho, Lam, Sethi y Ullman (2007), una gramática presenta recursión izquierda cuando un no terminal puede derivar una cadena cuyo símbolo más a la izquierda es él mismo. Un ejemplo típico es la producción A → Aα | β, donde A aparece nuevamente al inicio de su propia derivación. Este tipo de construcciones genera problemas en los analizadores sintácticos descendentes, ya que pueden entrar en ciclos infinitos al intentar expandir las producciones. Para eliminar la recursión izquierda directa, la gramática se transforma introduciendo un nuevo no terminal auxiliar. Así, una producción de la forma A → Aα | β se reescribe como A → βA' y A' → αA' | ε, conservando el lenguaje generado pero permitiendo un análisis sintáctico eficiente y libre de ciclos.

La recursión izquierda luce de la siguiente manera cuando se representa en un árbol sintáctico:
<img width="649" height="424" alt="image" src="https://github.com/user-attachments/assets/3112d5ce-c183-4604-9193-e3f169cc952a" />
(Imagen extraída del material de clase)

Al correr la gramática sin ambigüedad en el programa encontramos árboles con este mismo aspecto. <br>
En mi gramática se identificó en estas dos lineas : <br>
* oração → oração conjunção oração_simple  (la que le acabamos de quitar la ambigüedad) <br>
oração se llama a sí misma en la posición más izquierda causando directamente una recursión izquierda.

Y también se identificó en esta otra línea que genera el árbol que se muestra debajo:

* assunto → assunto adjetivo | pronome | nome |artigo nome

<img width="1104" height="492" alt="image" src="https://github.com/user-attachments/assets/497bccff-04af-4dc6-acd5-9ae4ee162bda" />

oracao y assunto se llaman a sí mismas en la posición más izquierda
por lo que assunto y oração podrían repetirse las veces que sean.

Lo que procede a hacerse para retirar es aplicar el algortimo explicado al incio de esta sección y en mi gramatica se vería así 

oração -> oração conjunção oração_simples   # A → A α <br>
oração -> oração_simples                    # A → β <br>

Por lo que  <br>

A = oração <br>
α = conjunção oração_simples <br>
β = oração_simples <br>

Entonces aplicando el algoritmo de  A → Aα | β se reescribe como A → βA' y A' → αA' | ε <br>
Se obtiene la siguiente forma : <br>
oração  → oração_simples oração' <br>
oração' → conjunção oração_simples oração' | ε <br>

Sin embargo aún hay otro segmento con recursión izquierda.

assunto -> assunto adjetivo    # A → A α <br>
assunto -> pronome             # A → β1 <br>
assunto -> nome                # A → β2 <br>
assunto -> artigo nome         # A → β3 <br>

A  = assunto <br>
α  = adjetivo <br>
β1 = pronome <br>
β2 = nome <br>
β3 = artigo nome <br>

teniendo en mente este algortimo
A  → β A' <br>
A' → α A' | ε <br>

Se sutstituye a 
assunto  → pronome assunto'| nome assunto' | artigo nome assunto' <br>
assunto' → adjetivo assunto'| ε <br>
y ahora el árbol se ve así <br>
<img width="954" height="483" alt="image" src="https://github.com/user-attachments/assets/37e6e8de-4008-42ee-a325-95111b68be60" />

## Modelo 
El modelo final de la gramática una vez fue removida la ambigüedad, recursión izquierda y  fue simplificada es esta:
<img width="511" height="544" alt="image" src="https://github.com/user-attachments/assets/69089640-e142-4aef-8231-d1536a1dadaf" />
y también se puede encontrar en el siguiente archivo de texto [GramaticaFinal.txt](GramaticaFinal.txt) 

## Implementación 
Existen dos archivos, en uno [PortuguesAmbiguo.py](PortuguesAmbiguo.py) parsea la gramática inicial (con recursividad y ambigüedad) y genera los respectivos árboles AST para cada oración propuesta en el mismo código. Determina si es posible de analizarse, es decir, si la oración cumple con las reglas de la gramática y también detecta cuántos árboles se generaron para una oración y determina la existencia de ambigüedad.
Esto mismo hace [Portugues.py](Portugues.py) pero con la gramática final.

Esta implementación usa la librería NLTK la cual permite analizar la estructura gramatical de oraciones definiendo reglas CFG (como S -> NP VP) y usando parsers como ChartParser. Para el proceso de parsing, NLTK usa Punkt como tokenizador previo, que divide el texto en oraciones y palabras mediante un modelo no supervisado entrenado en patrones de puntuación y abreviaciones, asegurando que la entrada al parser esté correctamente segmentada antes de aplicar las reglas gramaticales.

Al analizar la documentación de la API de NLTK, la librería tiene una complejidad de O(n²) porque el parser llena una tabla con columnas i y j, lo que le da al código una complejidad general de O(n²).

## Pruebas
Las purebas automatizadas están en [PruebasPortugues.py](PruebasPortugues.py) y solo se necesita correr el archivo.
Es importante tener la librería ntlk instalada para correrlas.

Se ingresan oraciones válidas e inválidas y el código determina con ok o con fallido dependiendo de si logró calsificar entre aceptadas y rechazadas correctamente.

Aquí se observan algunos ejemplos de oraciones válidas <br>
<img width="705" height="712" alt="image" src="https://github.com/user-attachments/assets/507b586b-3770-4f92-9620-d69d32153e6f" />

Aquí hay oraciones inválidas <br>
<img width="712" height="297" alt="image" src="https://github.com/user-attachments/assets/c70256ff-e7a5-4b69-bf0e-b273c9b425a9" />


y este fue el resultado donde se observa que si tiene un "OK" la prueba fue ejecutada correctamente, tuvo éxito en detemrinar si era válida o inválida <br>
<img width="685" height="583" alt="image" src="https://github.com/user-attachments/assets/27207090-f8a2-47b4-b983-a50d0c5f9df3" />




## Parser LL(1) Princeton 
Para hacer el parsing de mi gramática usé la herramienta del Parser Princeton la cual (descricpión del parser)
https://www.cs.princeton.edu/courses/archive/spring20/cos320/LL1/

### Tabla First Follow

**FIRST** indica los terminales con los que puede comenzar una expresión derivada de un no-terminal, y se construye siguiendo cada producción hasta encontrar un terminal o ε. **FOLLOW** indica qué terminales pueden aparecer inmediatamente después de un no-terminal en cualquier derivación, y se construye buscando ese no-terminal en el lado derecho de las producciones y revisando qué símbolo le sigue. Ambas tablas se usan en parsers predictivos (como LL(1)) para decidir qué regla gramatical aplicar sin necesidad de retroceder, guiando la navegación por el árbol sintáctico.
<img width="1106" height="775" alt="image" src="https://github.com/user-attachments/assets/1e766ccf-120b-4d2a-b21d-e72b5d9dbde7" />


### Tabla de análisis LL1
La tabla LL(1) es una estructura que asocia cada par (no-terminal, terminal) con exactamente una producción de la gramática. El parser la consulta en cada paso para decidir qué regla aplicar según lo que tiene en el tope de la pila y el token que está leyendo en la entrada.<br>
<img width="1814" height="399" alt="image" src="https://github.com/user-attachments/assets/17bb6599-3c3e-49ea-936f-39b90fdec98e" />
<img width="1673" height="404" alt="image" src="https://github.com/user-attachments/assets/c2892f66-82f1-4216-9c50-34cf663743b4" />
Si la celda correspondiente a ese par tiene una producción, el parser la aplica reemplazando el no-terminal por el lado derecho de la regla. Si la celda está vacía, la cadena se rechaza porque no existe ninguna derivación válida para esa combinación. La gramática es LL(1) precisamente cuando ninguna celda contiene más de una producción, lo que garantiza que el parser nunca tiene que elegir entre dos caminos posibles.

### Ejemplo de árboles 
Le pasamos al parser tokens válidos y contruye su árbol:

"a Maria nao gosta musica"<br>
<img width="827" height="433" alt="image" src="https://github.com/user-attachments/assets/4ed31f74-eaef-4c5d-9a61-7dee32a5dab3" />

"eles falam portuges"<br>
<img width="809" height="439" alt="image" src="https://github.com/user-attachments/assets/b3883213-7277-46ec-9323-b712ad3f26df" />

"o menino bom estudam ingles mas eles falam portugues" <br>
<img width="808" height="436" alt="image" src="https://github.com/user-attachments/assets/47698ec1-d35d-412b-b50c-9ced681728fd" />

"o menino mora no Brasil"<br>
<img width="417" height="240" alt="image" src="https://github.com/user-attachments/assets/dcd9ed76-afde-4232-8cf7-ab915f2c419d" />


## Jerarquía de Chomsky
La Jerarquía de Chomsky es un sistema de clasificación de gramáticas y lenguajes formales propuesto por Noam Chomsky para describir distintos niveles de complejidad sintáctica. Esta jerarquía se divide en cuatro categorías: gramáticas regulares (Tipo 3), libres de contexto (Tipo 2), sensibles al contexto (Tipo 1) y no restringidas (Tipo 0). Cada nivel posee una mayor capacidad de representación que el anterior, por lo que los lenguajes de una categoría incluyen a los de las categorías inferiores. Esta clasificación resulta fundamental en teoría de la computación porque establece la relación entre los tipos de gramáticas y los modelos computacionales capaces de reconocer los lenguajes que generan, como los autómatas finitos, los autómatas de pila y las máquinas de Turing. Además, proporciona una base teórica para el diseño de compiladores, analizadores sintácticos y sistemas de procesamiento de lenguajes formales.
<img width="763" height="476" alt="image" src="https://github.com/user-attachments/assets/2080ea25-741a-4dae-9141-e98ebb524f21" />

## Justificación 

El portugués, cuando se restringe al orden canónico **Sujeto-Verbo-Objeto (SVO)**, puede modelarse como una **Gramática Libre de Contexto (GLC)**. En este esquema, cada regla de producción reescribe un símbolo no terminal de forma independiente al entorno en que aparece: la oración se descompone en un sintagma nominal sujeto y un sintagma verbal, el sintagma verbal a su vez produce un verbo seguido opcionalmente de un sintagma nominal objeto, y cada sintagma nominal se expande en un artículo opcional más un sustantivo o pronombre. Ninguna de estas reescrituras necesita "recordar" qué hay fuera de ella para aplicarse correctamente, lo que es exactamente la propiedad definitoria de una GLC según la jerarquía de Chomsky. Fenómenos como la concordancia de género o la conjugación verbal quedan fuera del modelo, pero para el propósito de analizar la **estructura sintáctica superficial** de oraciones declarativas en portugués con orden SVO, las producciones de la forma `S → NP VP`, `VP → V NP` y `NP → Det N` son suficientes y formalmente correctas dentro del formalismo de una gramática libre de contexto.

<img width="666" height="453" alt="image" src="https://github.com/user-attachments/assets/f7edadce-3033-4ebb-a97d-12e1ef90efce" />


## Referencias
Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, Techniques, and Tools (2nd ed.). Pearson.<br>
Sipser, M. (2012). Introduction to the Theory of Computation (3rd ed.). Cengage Learning.<br>
Appel, A. W. (2002). Modern Compiler Implementation in Java (2nd ed.). Cambridge University Press.<br>
Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). Introduction to Automata Theory, Languages, and Computation (3rd ed.). Pearson Education.<br>
NLTK Project. (2024). NLTK API documentation. https://www.nltk.org/api/nltk.html<br>
https://www.nltk.org/<br>
Marco, A. (2025) Parsing. https://msmk.university/parsing/<br>

