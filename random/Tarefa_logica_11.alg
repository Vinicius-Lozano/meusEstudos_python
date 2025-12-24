algoritmo "área do triângulo 02"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : [Samara Souza]
// Descrição   : Area do triangulo equilatero
// Autor(a)    : Vinicius Lozano De Oliveira - 04156102
// Data atual  : 09/MAR/2024
var

l: inteiro
a: real

inicio
escreval("Escreva a base e a altura do triângulo em Cm")
leia(l)

a <- quad(l) * raizq(3) / 4


escreval("A área do triangulo é de: ", a:8:2 , "cm quadrados")

fimalgoritmo