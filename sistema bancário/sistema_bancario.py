nome = input("Olá! pode me informa o seu nome: ")
menu = f"""
    Bem vindo {nome.title()}, Selecione uma opções abaixo.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Qual valor do depósito ? "))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
            print(f"""
              {nome.title()}, seu depósito foi realizado com sucesso !!
              Obrigado pela preferência e volte sempre :)

              Saldo atual: {saldo:.2f}
              """) 
        else: 
            print(f"{nome.title()}, o valor digitado está incorreto.")   
    
    elif opcao == "s":


        valor_saque = float(input("Qual valor do saque ? "))
        if valor_saque > saldo:
            print(f"""
                  Infelizmente o saldo na sua conta é insuficiente
                  para realizar essa operação :(
                  
                  Saldo atual na conta R$: {saldo:.2f} 
                  """)
            
        elif valor_saque > limite:
            print("Por motivos de segurança, essa transação excede o limite de saque ")

        elif numero_saques >= limite_saques:
            print(f"Operação cancelada, {nome.title()} número máximo de saque excedido.")
            
        elif valor_saque > 0:
            saldo = saldo - valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"""
                  {nome.title()}, seu saque foi realizado com sucesso !!
                  Saldo atual: {saldo:.2f}
                  """)
        else:
            print("Valor invalido")
        

    elif opcao == "e":
        print("\n############ EXTRATO ############")
        print(f"\n           Olá {nome.title()}\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("##################################")
       

    elif opcao == "q":
        print(f"Até breve {nome.title()} !!")
        break    

else: 
    print("Operação inválida, por favor selecione a operação desejada.")
        



