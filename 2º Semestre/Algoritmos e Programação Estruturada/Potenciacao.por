programa
{
    funcao inicio(){

        inteiro base, resultado = 1, expoente
        
        escreva ("Digite a Base: ")
        leia(base)
        escreva("Digite o Expoente: ")
        leia(expoente)
        
        para(inteiro i = 0; i < expoente; i++) {
            resultado = base * resultado
        }

        escreva("" + base + "elevado a " + expoente + " = " +resultado)
    }
}