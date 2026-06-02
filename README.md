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
* Ejemplo: O gato dorme na cama. ("El gato duerme en la cama")

Y una oración compuesta se define como: Oración simple + CONJUNCAO + Oración Simple
* Ejemplo:Maria gosta de música e João gosta de português.
* Ejemplo Eles moram no Brasil e falam português.

Donde el sujeto(assunto) puede ser nombres (nome) y pronombres (pronome),los verbos describen las acciones que realiza el sujeto, y el objeto puede ser mútliples combinaciones de categorías gramaticales como sustantivos (substantivos)  por si solos o combinados con artículos (artigos) y preposiciones (preposicao).

### Gramática
Según Hopcroft, Motwani y Ullman (2006), una gramática es una descripción formal de un lenguaje que especifica cómo pueden construirse cadenas válidas mediante un conjunto de reglas de producción. Una gramática está compuesta por símbolos terminales, símbolos no terminales, un símbolo inicial y un conjunto de producciones. Los terminales son los símbolos básicos que aparecen en las cadenas finales del lenguaje y no pueden ser reemplazados por otros símbolos, mientras que los no terminales representan categorías o estructuras intermedias que pueden expandirse mediante las reglas de producción. A partir de estas reglas es posible construir un árbol sintáctico, una representación jerárquica que muestra cómo una cadena es generada desde el símbolo inicial hasta llegar a los terminales. En dicho árbol, los nodos internos corresponden a símbolos no terminales y las hojas a símbolos terminales, permitiendo visualizar la estructura sintáctica de una expresión u oración y facilitando su análisis por parte de compiladores y procesadores de lenguaje. 

#### CFG
Una Gramática Libre de Contexto (Context-Free Grammar, CFG) es un conjunto de reglas de producción utilizado para describir lenguajes en los que cada regla reemplaza un único símbolo no terminal por una cadena de símbolos terminales y no terminales. Formalmente, una CFG está compuesta por un conjunto de terminales, un conjunto de no terminales, un símbolo inicial y un conjunto de producciones. Estas gramáticas son especialmente importantes porque permiten modelar estructuras jerárquicas presentes en lenguajes de programación y lenguajes naturales, siendo además la base teórica de los analizadores sintácticos empleados en compiladores. Sipser (2012)

#### EBNF
La Forma Extendida de Backus-Naur (EBNF) es una notación que amplía la BNF tradicional mediante la incorporación de operadores que permiten expresar repeticiones, alternativas y elementos opcionales de manera más concisa. Su objetivo es simplificar la especificación de gramáticas al reducir el número de producciones necesarias para describir la sintaxis de un lenguaje. Gracias a estas extensiones, EBNF resulta especialmente útil para documentar lenguajes de programación y sistemas de procesamiento de lenguaje, ya que mejora la legibilidad y el mantenimiento de las gramáticas sin modificar su capacidad descriptiva.

#### Modelo 
Se busca que este subconjunto de gramática del portugués sea capaz de generar las siguientes oraciones:
* "Maria gosta musica",
* "Maria gosta",
* "Maria lê livro e Maria mora Brasil e você gosta musica",
* "eles não estudam ingles",
* "o menino bom lê livro",

Y basado en las reglas del portugues esta ha sido mi producción de modelo 

<img width="834" height="439" alt="image" src="https://github.com/user-attachments/assets/47c7777f-2c7f-4660-b4bc-b44a17c400c0" />

Sin embargo, la gramática presentada aquí tiene dos problemas, es ambigua y tiene recursividad izquierda. Estos problemas serán corregidos a continuación.

### Ambigüedad
Según Aho, Lam, Sethi y Ullman (2007), una gramática es ambigua cuando existe al menos una cadena del lenguaje que puede derivarse mediante dos o más árboles sintácticos diferentes. La ambigüedad representa un problema en el diseño de compiladores porque una misma entrada puede interpretarse de distintas maneras, generando incertidumbre sobre su significado. Para eliminarla, es común reescribir la gramática incorporando reglas que establezcan explícitamente la precedencia y asociatividad de los operadores o separando las construcciones en diferentes niveles sintácticos. De esta forma, cada cadena válida posee una única derivación y un único árbol sintáctico, permitiendo un análisis sintáctico determinista y sin interpretaciones múltiples.

Primero se debe identificar que parte de la gramática es aquella que causa este problema, así que se ha probado con la implementación en [PortuguesAmbiguo.py](PortuguesAmbiguo.py)  y como output se ha detectado que 
al querer generar la oración 'Maria lê livro e Maria mora Brasil e você gosta musica' hay más de un árbol sintáctico capaz de generarlo 
<img width="1116" height="791" alt="image" src="https://github.com/user-attachments/assets/017d939d-3525-43f6-918b-88adc67d35ba" />

Y se ha identificado que el probelma radica aquí:
<n> oração → oração conjunção oração <n>
ya que hay dos manera de hacer esta oración: Maria lê livro e Maria mora Brasil e você gosta musica 

* (Maria lê livro e Maria mora Brasil) e você gosta musica
* Maria lê livro e (Maria mora Brasil e você gosta musica)
Por lo tanto se determinó que es una gramática ambigua y una vez identificado esto, procedemos a quitarselo.
En los árboles se puede apreciar que hay asociatividad por ambos lados (derecha e izquierda) debido a que oracao inicia y temrina con oracao.

Entonces usando asociativad izquierda haré que ya no sea posible formar uno de los dos árboles, quitando así la ambigüedad.
El método es agregar estados intermedios que indiquen un nivel de precedencia, ya que se deben pasar por niveles obligatoriamente entonces no hay rutas alternas.
como en este ejemplo mostrado en clase:
Original: 

E-> E + E | E * E | id 

Transformed:
E → E + T | T

T → T * F | F

F → id	

Aplicado a nuestra gramática:
oração → oração conjunção oração

Se agregó un "filtro", ahora no se puede formar una oracao al final sin pasar por oracao simple

oração        -> oração conjunção oração_simples  <br>
oração        -> oração_simples<br>            

oração_simples -> assunto verbo objeto<br>
oração_simples -> assunto verbo<br>
oração_simples -> assunto 'não' verbo objeto<br>

Y una vez usando ese cambio de gramática se corre en  [PortuguesAmbiguo.py](PortuguesAmbiguo.py)  y se observa como solo hay un árbol para aquella oración habiendo quitado exitosamente la ambigüedad.
<img width="1382" height="494" alt="image" src="https://github.com/user-attachments/assets/2a58238e-6b80-44cb-a405-5f2e5b834ad8" />

### Recursión izquierda
Según Aho, Lam, Sethi y Ullman (2007), una gramática presenta recursión izquierda cuando un no terminal puede derivar una cadena cuyo símbolo más a la izquierda es él mismo. Un ejemplo típico es la producción A → Aα | β, donde A aparece nuevamente al inicio de su propia derivación. Este tipo de construcciones genera problemas en los analizadores sintácticos descendentes, ya que pueden entrar en ciclos infinitos al intentar expandir las producciones. Para eliminar la recursión izquierda directa, la gramática se transforma introduciendo un nuevo no terminal auxiliar. Así, una producción de la forma A → Aα | β se reescribe como A → βA' y A' → αA' | ε, conservando el lenguaje generado pero permitiendo un análisis sintáctico eficiente y libre de ciclos.

La recursión izquierda luce de la siguiente manera cuando se representa en un árbol sintáctico:
<img width="649" height="424" alt="image" src="https://github.com/user-attachments/assets/3112d5ce-c183-4604-9193-e3f169cc952a" />
(Imagen extraída del material de clase)

Al correr mi gramática en el archivo [PortuguesAmbiguo.py](PortuguesAmbiguo.py) encontramos árboles con este aspecto:


En mi gramática se identificó en estas dos lineas :
* oração → oração conjunção oração_simples  (la que le acabamos de quitar la ambigüedad)
  <img width="1383" height="509" alt="image" src="https://github.com/user-attachments/assets/916ad7e1-c9ff-4dda-a8e2-433315d68cd9" />
oração se llama a sí misma en la posición más izquierda

* assunto → assunto adjetivo
<img width="838" height="473" alt="image" src="https://github.com/user-attachments/assets/05069031-2797-4061-a263-9a22d7542b5e" />
assunto se llama a sí misma en la posición más izquierda
p
or lo que assunto y oração podrían repetirse las veces que sean.

Lo que procede a hacerse para retirar es aplicar el algortimo explicado al incio de esta sección y en mi gramatica se vería así 

oração -> oração conjunção oração_simples   # A → A α <br>
oração -> oração_simples                    # A → β <br>

Por lo que 

A = oração <br>
α = conjunção oração_simples <br>
β = oração_simples <br>

Entonces aplicando el algoritmo de  A → Aα | β se reescribe como A → βA' y A' → αA' | ε
Se obtiene la siguiente forma :
oração  → oração_simples oração' <br>
oração' → conjunção oração_simples oração' | ε <br>
 y el árbol ahora se ve así 
 <img width="1566" height="508" alt="image" src="https://github.com/user-attachments/assets/93bfed78-6e1f-48b1-8ca6-aacd6312beb6" />

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
assunto  → pronome assunto' <br>
assunto  → nome assunto' <br>
assunto  → artigo nome assunto' <br>
assunto' → adjetivo assunto' | ε <br>
y ahora el árbol se ve así 
<img width="1071" height="476" alt="image" src="https://github.com/user-attachments/assets/62f88525-4dcf-45ad-9f8d-d595a927425d" />

## Modelo 
El modelo final de la gramática una vez fue removida la ambigüedad, recusrión izquierda y  fue simplificada es esta:
<img width="299" height="462" alt="image" src="https://github.com/user-attachments/assets/15f0d76e-35e1-496d-b221-dd5b3d658db9" />
y también se puede encontrar en el siguiente archivo de texto [GramaticaFinal.txt](GramaticaFinal.txt) 

## Implementación 
Se encuentra en el archivo. Este código funciona de la siguiente manera:
[Portugues.py](Portugues.py)

## Pruebas
Las purebas automatizadas están en [PruebasPortugues.py](PruebasPortugues.py) y solo se necesita correr el archivo.
Es importante tener la librería ntlk instalada para correrlas.

Se ingresan oraciones válidas e inválidas y el código determina con ok o con fallido dependiendo de si logró calsificar entre aceptadas y rechazadas.

Aquí se observan algunos ejemplos de oraciones válidas
<img width="703" height="474" alt="image" src="https://github.com/user-attachments/assets/a78e7468-8e44-4cef-a1b8-4e5d0767825f" />

Aquí hay oraciones inválidad
<img width="723" height="391" alt="image" src="https://github.com/user-attachments/assets/73a3cb46-989a-4c45-abba-a0308a888c19" />

y este fue el resultado donde se observa que si tiene un "OK" la prueba fue ejecutada correctamente, tuvo éxito en detemrinar si era válida o inválida
<img width="766" height="734" alt="image" src="https://github.com/user-attachments/assets/4d6c5af2-3cca-4208-bbc2-af61b8d30751" />


## Parser LL(1) Princeton 

### Tabla First Follow
### Tabla de análisis LL1
### Ejemplo de árboles 

## Jerarquía de Chomsky
La Jerarquía de Chomsky es un sistema de clasificación de gramáticas y lenguajes formales propuesto por Noam Chomsky para describir distintos niveles de complejidad sintáctica. Esta jerarquía se divide en cuatro categorías: gramáticas regulares (Tipo 3), libres de contexto (Tipo 2), sensibles al contexto (Tipo 1) y no restringidas (Tipo 0). Cada nivel posee una mayor capacidad de representación que el anterior, por lo que los lenguajes de una categoría incluyen a los de las categorías inferiores. Esta clasificación resulta fundamental en teoría de la computación porque establece la relación entre los tipos de gramáticas y los modelos computacionales capaces de reconocer los lenguajes que generan, como los autómatas finitos, los autómatas de pila y las máquinas de Turing. Además, proporciona una base teórica para el diseño de compiladores, analizadores sintácticos y sistemas de procesamiento de lenguajes formales.
<img width="763" height="476" alt="image" src="https://github.com/user-attachments/assets/2080ea25-741a-4dae-9141-e98ebb524f21" />
## Justificación formal

El portugués, cuando se restringe al orden canónico **Sujeto-Verbo-Objeto (SVO)**, puede modelarse como una **Gramática Libre de Contexto (GLC)**. En este esquema, cada regla de producción reescribe un símbolo no terminal de forma independiente al entorno en que aparece: la oración se descompone en un sintagma nominal sujeto y un sintagma verbal, el sintagma verbal a su vez produce un verbo seguido opcionalmente de un sintagma nominal objeto, y cada sintagma nominal se expande en un artículo opcional más un sustantivo o pronombre. Ninguna de estas reescrituras necesita "recordar" qué hay fuera de ella para aplicarse correctamente, lo que es exactamente la propiedad definitoria de una GLC según la jerarquía de Chomsky. Fenómenos como la concordancia de género o la conjugación verbal quedan fuera del modelo, pero para el propósito de analizar la **estructura sintáctica superficial** de oraciones declarativas en portugués con orden SVO, las producciones de la forma `S → NP VP`, `VP → V NP` y `NP → Det N` son suficientes y formalmente correctas dentro del formalismo de una gramática libre de contexto.

<img width="666" height="453" alt="image" src="https://github.com/user-attachments/assets/f7edadce-3033-4ebb-a97d-12e1ef90efce" />


## Referencias
Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, Techniques, and Tools (2nd ed.). Pearson.
Sipser, M. (2012). Introduction to the Theory of Computation (3rd ed.). Cengage Learning.
Appel, A. W. (2002). Modern Compiler Implementation in Java (2nd ed.). Cambridge University Press.
Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). Introduction to Automata Theory, Languages, and Computation (3rd ed.). Pearson Education.

