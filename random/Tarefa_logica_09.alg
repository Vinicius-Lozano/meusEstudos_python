algoritmo "Calculador de salario"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : [Samara Souza]
// Descrição   : n sei como demorei tanto pra fazer esse sendo q era facil
// Autor(a)    : Vinicius Lozano De Oliveira - 04156102
// Data atual  : 09/MAR/2024
var

horas_trabalhadas, valor_hora, salario_bruto, percentual_desconto, total_desconto, salario_liquido: real

inicio

escreval("forneça nessa ordem 1-horas trabalhadas no mês, 2-valor hora trabalhada, 3-percentual de desconto")
leia(horas_trabalhadas, valor_hora, percentual_desconto)
// horas:270
// valor: 4
// percentual: 10

salario_bruto <- horas_trabalhadas * valor_hora

percentual_desconto <- percentual_desconto / 100
total_desconto <- salario_bruto * percentual_desconto
salario_liquido <- salario_bruto - total_desconto

escreval("Horas trabalhadas: ", horas_trabalhadas)
escreval("Salario Bruto:     ", salario_bruto)
escreval("Desconto:          ", total_desconto)
escreval("Salario Liquido:   ", salario_liquido)
fimalgoritmo
