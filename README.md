# Generación de gramáticas

## Descripción


## Cómo funciona

### Gramática
una gramatica se define 
CFG
EBNF

<img width="516" height="607" alt="image" src="https://github.com/user-attachments/assets/2585f88d-0564-41e9-ad1c-6c9712c9e70c" />
Se busca que este subconjunto de gramática del portugués sea capaz de generar las siguientes oraciones:
*Maria gosta de música
*Eles estudam português
*Você mora do Brasil 
*O menino lê  o livro 
*Eles não falam inglês


<img width="834" height="439" alt="image" src="https://github.com/user-attachments/assets/47c7777f-2c7f-4660-b4bc-b44a17c400c0" />

Sin embargo, la gramática presentada aquí tiene dos problemas, es ambigua y tiene recursividad izquierda. Estos problemas serán corregidos a continuación.

### Ambigüedad
Investigación 

Primero se debe identificar que parte de la gramática es aquella que causa este problema así que se ha probado con la implementación en y como output se ha detectado que 
al querer generar tal oración nos damos cuenta que hay más de un árbol sintáctico capaz de generarlo 
Y se ha identificado que el probelma radica aquí oração → oração conjunção oração ya que hay dos manera de acer esta oración: Maria lê livro e Maria mora Brasil e você gosta musica 

*(Maria lê livro e Maria mora Brasil) e você gosta musica
* Maria lê livro e (Maria mora Brasil e você gosta musica)

Por lo tanto se determinó que es una gramática ambigua

### Recursión izquierda
investigación 
en mi gramática se identificó en estas dos lineas :
*oração → oração conjunção oração
oração se llama a sí misma en la posición más izquierda 
*assunto → assunto adjetivo
assunto se llama a sí misma en la posición más izquierda

## Modelo 
El modelo final de la gramática una vez fue removida la ambigüedad, recusrión izquierda y  fue simplificada es esta:
<img width="291" height="263" alt="image" src="https://github.com/user-attachments/assets/da47db1a-033a-4edb-a1f9-0062d49d319b" />


## Implementatción 
Se encuentra en el archivo 


## Pruebas

## Parser LL(1) Princeton 

### Tabla First Follow
### Tabla de análisis LL1
### Ejemplo de árboles 

## Analysis de Chomsky

## Referencias

