
menu = """"
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

menu_extrato =""""



"""

 
saldo_ATUAL = 0
limite = 500
extrato=""
numero_saques = 3


while True:   
   print(menu)
   opcao = input("aqui: ")
   
   
   if opcao.lower() == "d":
    while True:
       print(menu_deposito) 
       deposito = input("valor: ") 

       print("""voce deseja depositar: R$""",deposito,"?\n")
       resposta = input("""{1}sim {2}nao""")
       if resposta == "1" :
          saldo_ATUAL += int(deposito)
          print("""
################ DEPOSITO ################
                               
 PARABENS!!! PELO DEPOSITO DE R${deposito1}        
       seu saldo atual e : R$ {saldo} 
                
################# FIM ####################""".format(deposito1 = deposito,saldo=saldo_ATUAL))
          extrato += "+"+"R$"+str(deposito)+"\n"
          resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
          if resposta == "1" : break
          elif resposta != "1" : 
           print("VOCE VAI VOLTAR SIMM!!!!")
           break

          
       elif resposta != "1" : break
       
       
    
   elif opcao.lower()=="s":
       
       
       
       while True:
        if numero_saques == 0 :
           print(
"""
################ SAQUE ################
                               
VALOR MAXIMO DE SAQUES DIORIOS EXCEDIDO
  Numero maximo de saques diarios e 3       
                            
################# FIM ##################""") 
           resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
           if resposta == "1" : break
           elif resposta != "1" : 
              print("VOCE VAI VOLTAR SIMM!!!!")
              break
         
          
        print(menu_saque)
        saque = input("valor: ")
        

        if int(saque) > int(limite)  :
          print("""
################ SAQUE ################
                               
    VALOR MAXIMO DE SAQUE EXCEDIDO
    Valor maximo de saque e R$ 500        
                            
################# FIM ##################""")
          resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
          if resposta == "1" : break
          elif resposta != "1" : 
             print("VOCE VAI VOLTAR SIMM!!!!")
             break
          
          
        if  int(saque) > int(saldo_ATUAL):
           print("""
################ SAQUE ################
                               
    VALOR MAXIMO DE SAQUE EXCEDIDO
 Voce nao possui essse valor na conta
    seu saldo atual e : {saldo}                 
                            
################# FIM ##################""".format(saldo=saldo_ATUAL))
          
           resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
           if resposta == "1" : break
           elif resposta != "1" : 
             print("VOCE VAI VOLTAR SIMM!!!!")
             break
       
        else :
           print("""voce deseja sacar: R$""",saque,"?\n")
           resposta = input("""{1}sim {2}nao""")
           if resposta == "1" :
             saldo_ATUAL-=int(saque)
             numero_saques -=1
             print("""
################ SAQUE ################
                               
 PARABENS!!! PELO SAQUE DE R${saque} 
    seu saldo atual e : {saldo} 
 voce ainda possui {saques_diarios} saques diarios
                   
################# FIM ##################""".format(saque = saque, saldo=saldo_ATUAL, saques_diarios = numero_saques))
             extrato += "-"+"R$"+str(saque)+"\n"
             
             resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
             if resposta == "1" : break
             elif resposta != "1" : 
              print("VOCE VAI VOLTAR SIMM!!!!")
              break

       
        break

   elif opcao.lower()=="e":
    while True:
      print(       
   """
################ EXTRATO ################
                           
*{extrato1}      
                           
################# FIM ##################""".format(extrato1=extrato ))
      resposta = input ("deseja voltar ao menu? (1)sim (2)nao")

      if resposta == "1" : break
      elif resposta != "2" : 
         print("VOCE VAI VOLTAR SIMM!!!!")
         break
      


   elif opcao.lower() == "q" :
      break

   else :
      print("DIGITE A OPCAO NOVAMENTE")
    


   