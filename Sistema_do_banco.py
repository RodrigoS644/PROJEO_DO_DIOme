
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

saldo = 0
limite =500
extrato=""
numero_saques = 3


while True:

   print(menu)

   opcao = input("menu")

   if opcao=="d":
      print(menu_deposito)   
     

   elif opcao=="s":
      print(menu_saque)

   elif opcao=="e":
      print("Extrato")


   elif opcao=="q":
      break


   else :
      print("operacao invalida , por favor selecione novante a operacao desejada")