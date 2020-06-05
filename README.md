# TAFL
Программы по ТАФЯ

Здесь представлена одна программа под названием regularGramAnalys.py. Она выполняет анализ регулярной грамматики. В данном случае программа предназначена для анализа следующей регулярной грамматики: 
G = ({a, b, c}, {S, A, B, C}, P, S)

Этой грамматике соотвествуют следующие правила:
P: S -> Cc
   C -> Ab|Ba
   A -> a|Ca
   B -> b|Cb
   
Для этой грамматики с правилами и написан анализатор.
Диаграмма состояний для данной грамматики G выглядит следующим образом:

![Диаграмма состояний](https://github.com/Remkudusov/TAFL/blob/master/diagramm.png)
