Algoritmo "aula01"
// Disciplina   : [L�gica de Programa��o]
// Professor   : Samara Souza
// Autor(a)    : Alessandro da Costa e Silva
// Data atual  : 07/03/2024
Var
nome:caracter
saldo, retirada: real
diasDeVida, diaNascimento, mesNascimento, valorDois, valorUm:inteiro
idade, anoAtual, anoNascimento: inteiro
Inicio
//ativade 1
escreval("Meu primeiro programa")
escreval("**Atv1 conclu�da**")

//atividade 2
escreval("Digite seu primeiro valor pra somar")
leia(valorUm)
escreval("Digite seu segundo valor pra somar")
leia(ValorDois)
escreval("Sua soma resultou em: ", valorUm + valorDois)
escreval("**Atv2 conclu�da**")

//atividade 3
escreval("Digite seu nome")
leia(nome)
escreval("digite o ano atual")
leia(anoAtual)
escreval("Digite seu ano de nascimento")
leia(anoNascimento)
escreval("Olá", nome, "Voc� tem ", anoAtual-anoNascimento, " anos de idade")
idade:= anoAtual-anoNascimento
escreval("**Atv3 conclu�da**")

//atividade 4
escreval("me fale quanto vc tem no banco")
leia (saldo)
escreval("quanto vc quer retirar")
leia (retirada)
escreval ("agora vc tem: ", saldo - retirada)
escreval("**Atv4 conclu�da**")

//atividade 5
escreval("Ol� ", nome, ". Em qual dia e m�s voc� nasceu?")
leia(diaNascimento, mesNascimento)
diasDeVida:= mesNascimento * 30 + diaNascimento + idade * 365
escreval(nome, "voc� possui ", idade, " anos, ", "nasceu dia ", diaNascimento)
escreva("Do m�s ", mesNascimento, ". Voc� tem, aproximadamente, ", diasDeVida, " dias de vida")



Fimalgoritmo