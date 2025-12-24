algoritmo "taxa de consumo em km/l"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : [Samara Souza]
// Descrição   : taxa de consumo em km/l que um carro  tem  em  um  deslocamento
// Autor(a)    : Vinicius Lozano De Oliveira - 04156102
// Data atual  : 09/MAR/2024
var

distancia_percorrida, litros_consumidos, taxa_consumo : inteiro

inicio
escreval("Escreva a distância percorrida em km e os litros consumidos:  ")
leia(distancia_percorrida, litros_consumidos)

taxa_consumo <- distancia_percorrida / litros_consumidos

escreval("Foi percorrido ", distancia_percorrida, " km. ")
escreval("consumidos ",litros_consumidos, " litros de gasosa")
escreval("em uma taxa de consumo de: ",taxa_consumo, "km/l")

fimalgoritmo