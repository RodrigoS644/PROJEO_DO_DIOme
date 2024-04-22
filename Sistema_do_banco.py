
menu = """""
################ MENU ################

{"d"} Depositar
{"s"} Sacar
{"e"} Extrato
{"q"} Sair

===>
################ FIM ##################
"""
menu_deposito= """"

################ DEPOSITO ################
                               
        DIGITE O VALOR DE DEPOSITO:         
                            
################# FIM ####################


"""
menu_saque = """

################ SAQUE ################
                               
        DIGITE O VALOR DE SAQUE:         
                            
################# FIM #################

"""

menu_extrato = """"



"""

PARABENS =
"""################ DEPOSITO ################
                               
       PARABENS PELO DEPOSITO DE {VALOR_DEPOSITO}        
                            
   ################# FIM ####################"""

saldo = 0
limite =500
extrato=""
numero_saques = 3


while True:   
   print(menu)
   opcao = input("aqui: ")
   
   if opcao == "d":
    while True:
       print(menu_deposito) 
       deposito = input("valor: ") 
       print("""voce desejadepositar:""",deposito,"?\n")
       resposta = input("yes or no: ")
       if resposta == "yes" : print("""""")

       b = input("voce deseja voltar? yes or no: ")
       if b = "yes": break 
         
     

   elif opcao=="s":
      print(menu_saque)
      saque = input("valor: ")

   elif opcao=="e":
      print(menu_extrato)
      


   elif opcao == "q" :
      break

   else :
      print("digite a opcao novamente")
    


   