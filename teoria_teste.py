
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


class perfil:
    
    def __init__ (self,saldo_ATUAL,extrato_list,numero_saques):
    
     self.saldo_ATUAL = saldo_ATUAL
     self.extrato_list= extrato_list
     self.numero_saques = numero_saques
     self.limite= 500

    
     



    def deposito(self):
  
       
         while True:
           print(menu_deposito) 
           deposito = input("valor: ") 

           print("""voce deseja depositar: R$""",deposito,"?\n")
           resposta = input("""{1}sim {2}nao""")
           if resposta == "1" :
             self.saldo_ATUAL += int(deposito)
             print("""
################ DEPOSITO ################
                               
 PARABENS!!! PELO DEPOSITO DE R${deposito1}        
       seu saldo atual e : R$ {saldo} 
                
################# FIM ####################""".format(deposito1 = deposito,saldo=self.saldo_ATUAL))
             self.extrato_list += "+"+"R$"+str(deposito)+"\n"
            
             resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
             if resposta == "1" : break
             elif resposta != "1" : 
               print("VOCE VAI VOLTAR SIMM!!!!")
               break
           elif resposta != "1" : break
         ""
  
    
             
    def saque(self):
       
       while True:
        if self.numero_saques == 0 :
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
        

        if int(saque) > int(self.limite)  :
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
          
          
        if  int(saque) > int(self.saldo_ATUAL):
           print("""
################ SAQUE ################
                               
    VALOR MAXIMO DE SAQUE EXCEDIDO
 Voce nao possui essse valor na conta
    seu saldo atual e : {saldo}                 
                            
################# FIM ##################""".format(saldo=self.saldo_ATUAL))
          
           resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
           if resposta == "1" : break
           elif resposta != "1" : 
             print("VOCE VAI VOLTAR SIMM!!!!")
             break
       
        else :
           print("""voce deseja sacar: R$""",saque,"?\n")
           resposta = input("""{1}sim {2}nao""")
           if resposta == "1" :
             self.saldo_ATUAL-=int(saque)
             self.numero_saques -=1
             print("""
################ SAQUE ################
                               
 PARABENS!!! PELO SAQUE DE R${saque} 
    seu saldo atual e : {saldo} 
 voce ainda possui {saques_diarios} saques diarios
                   
################# FIM ##################""".format(saque = saque, saldo=self.saldo_ATUAL, saques_diarios = self.numero_saques))
             self.extrato_list += "-"+"R$"+str(saque)+"\n"
             
             resposta = input ("deseja voltar ao menu? (1)sim (2)nao")
             if resposta == "1" : break
             elif resposta != "1" : 
              print("VOCE VAI VOLTAR SIMM!!!!")
              break
             


    def extrato(self):

      
         while True:
          print(       
   """
################ EXTRATO ################
                           
*{extrato1}      
                           
################# FIM ##################""".format(extrato1=self.extrato_list))
          resposta = input ("deseja voltar ao menu? (1)sim (2)nao")

          if resposta == "1" : break
          elif resposta != "2" : 
            print("VOCE VAI VOLTAR SIMM!!!!")
            break
      
    


    def start (self):
     
     while True:
      print(menu)
      opcao = input("aqui: ")
      if opcao.lower()=="d": 
           perfil(saldo,extrato,numero_s).deposito()
           saldo = self.saldo_ATUAL
           extrato= self.extrato_list
           numero_s = self.numero_saques

      elif opcao.lower()=="s": 
           perfil(saldo,extrato,numero_s).saque()
           saldo = self.saldo_ATUAL
           extrato= self.extrato_list
           numero_s = self.numero_saques

      elif opcao.lower()=="e":
           perfil(saldo,extrato,numero_s).extrato()
           saldo = self.saldo_ATUAL
           extrato= self.extrato_list
           numero_s = self.numero_saques

      elif opcao.lower()=="q":
           break
      else :print("DIGITE A OPCAO NOVAMENTE")
  
    
      
      
perfil.start()

      
      
      