algoritmo "Erro proposital"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : [Samara Souza]
// Descrição   : Troca de valores entre variaveis
// Autor(a)    : Vinicius Lozano De Oliveira - 04156102
// Data atual  : 09/MAR/2024
var

A, B, C : caractere

inicio

escreval("Escreva algo para 'A'")
leia(A) // foi digitado "A"
escreval("Escreva algo para 'B'")
leia(B) // foi digitado "B"
C <- A
A <- B 
B <- C 
escreval("valor de A: ", A, " Valor de B: ", B)
fimalgoritmo
