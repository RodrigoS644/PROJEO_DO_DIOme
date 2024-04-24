
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

 
saldo_ATUAL = 0
limite =500
extrato=""
numero_saques = 3


while True:   
   print(menu)
   opcao = input("aqui: ")
   if numero_saques == 0 : print("numero de saques diarios atingido!!")
   
   if opcao == "d":
    while True:
       print(menu_deposito) 
       deposito = input("valor: ") 

       print("""voce deseja depositar:""",deposito,"?\n")
       resposta = input("""{1}sim {2}nao""")
       if resposta == "1" :
          saldo_ATUAL += int(deposito)
          print("""
          ################ DEPOSITO ################
                               
             PARABENS!!! PELO DEPOSITO DE R${deposito1}        
                   seu saldo atual e : {saldo} 
          ################# FIM ####################""".format(deposito1 = deposito,saldo=saldo_ATUAL))
       
       
       print (saldo_ATUAL)
       
       break
    
   elif opcao=="s":
       
       while True:
        print(menu_saque)
        saque = input("valor: ")
        if int(saque) > 500 or int(saldo) : print("""
                ################ SAQUE ################
                               
                     VALOR MAXIMO DE SAQUE EXCEDIDO        
                            
                ################# FIM ##################""")
        else :"""################ SAQUE ################
                               
                   PARABENS!!! PELO SAQUE DE R${saque} 
                            
                            
                ################# FIM ##################""".format(saque = saque)
       

   elif opcao=="e":
      print(menu_extrato)
      


   elif opcao == "q" :
      break

   else :
      print("digite a opcao novamente")
    


   