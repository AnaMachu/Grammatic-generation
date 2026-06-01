# Generación de gramáticas

## Descripción


## Cómo funciona

### Gramática
una gramatica se define 
#### CFG

#### EBNF

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
Investigación 

Primero se debe identificar que parte de la gramática es aquella que causa este problema así que se ha probado con la implementación en [PortuguesAmbiguo.py](PortuguesAmbiguo.py)  y como output se ha detectado que 
al querer generar tal oración nos damos cuenta que hay más de un árbol sintáctico capaz de generarlo 
Y se ha identificado que el probelma radica aquí oração → oração conjunção oração ya que hay dos manera de acer esta oración: Maria lê livro e Maria mora Brasil e você gosta musica 

* (Maria lê livro e Maria mora Brasil) e você gosta musica
* Maria lê livro e (Maria mora Brasil e você gosta musica)

Por lo tanto se determinó que es una gramática ambigua

### Recursión izquierda
investigación 
en mi gramática se identificó en estas dos lineas :
* oração → oração conjunção oração
oração se llama a sí misma en la posición más izquierda 
* assunto → assunto adjetivo
assunto se llama a sí misma en la posición más izquierda

## Modelo 
El modelo final de la gramática una vez fue removida la ambigüedad, recusrión izquierda y  fue simplificada es esta:
<img width="291" height="263" alt="image" src="https://github.com/user-attachments/assets/da47db1a-033a-4edb-a1f9-0062d49d319b" />


## Implementatción 
Se encuentra en el archivo 
[Portugues.py](Portugues.py)

## Pruebas
Las purebas automatizadas están en [PruebasGramatica.py](PruebasGramatica.py)
## Parser LL(1) Princeton 

### Tabla First Follow
### Tabla de análisis LL1
### Ejemplo de árboles 

## Analysis de Chomsky
<img width="763" height="476" alt="image" src="https://github.com/user-attachments/assets/2080ea25-741a-4dae-9141-e98ebb524f21" />

<img width="666" height="453" alt="image" src="https://github.com/user-attachments/assets/f7edadce-3033-4ebb-a97d-12e1ef90efce" />


## Referencias
Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, Techniques, and Tools (2nd ed.). Pearson.
Sipser, M. (2012). Introduction to the Theory of Computation (3rd ed.). Cengage Learning.
Appel, A. W. (2002). Modern Compiler Implementation in Java (2nd ed.). Cambridge University Press.

