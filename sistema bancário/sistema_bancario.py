nome = input("Olá! pode me informa o seu nome: ")
menu = f"""
    Bem vindo {nome}, Selecione uma opções abaixo.

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
              Depósito realizado com sucesso !!
              Saldo atual: {saldo}
              """) 
        else: 
            print("Valor incorreto.")   
    
    elif opcao == "s":


        valor_saque = float(input("Qual valor do saque ? "))
        if valor_saque > saldo:
            print(f"""
                  Saldo insuficiente :(
                  Saldo atual na conta R${saldo} 
                  """)
            
        elif valor_saque > limite:
            print("Valor do saque excede o limite.")

        elif numero_saques >= limite_saques:
            print("Operação cancelada, número máximo de saque excedido.")
            
        elif valor_saque > 0:
            saldo = saldo - valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"""
                  Saque realizado com sucesso !!
                  Saldo atual: {saldo}
                  """)
        else:
            print("Valor invalido")
        

    elif opcao == "e":
        print("\n############ EXTRATO ############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("##################################")
       

    elif opcao == "q":
        print(f"Até breve {nome} !!")
        break    

else: 
    print("Operação inválida, por favor selecione a operação desejada.")
        



