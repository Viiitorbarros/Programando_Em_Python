class Conta:
   def __init__(self, numero, titular, saldo, limite):
      
      self.__numero= numero #DEIXAR  O ATRIBUTO PRIVADO '__'
      self.__titular = titular
      self.__saldo = saldo
      self.__limite = limite
      

   def extrato(self): # VER SALDO EM CONTA
      print(f'O saldo do titular  {self.__titular} é de {self.__saldo}')

   def depositar (self, valor): # DEPOSITAR VALOR
      self.__saldo += valor
      
   def __pode_sacar (self ,valor_a_sacar):

      if (self.__saldo > valor_a_sacar and valor_a_sacar < self.limite ):
         return valor_a_sacar
      
      #Valor_disponivel_a_Sacar = self.__saldo + self.__limite
      #return valor_a_sacar <= Valor_disponivel_a_Sacar
      
   def sacar (self, valor): # SACAR VALOR 
      if (self.__pode_sacar(valor)):
         self.__saldo -= valor
         print(f'Saque Realizado com Succeso no valor de {valor} Reais')
      else :
         print(f'Voce Nao tem saldo suficiente ou limite nao permitido.')   

      
   def transferir(self, destino, valor): # SELF PARA CHAMAR MINHA CONTA DE ORIGEM
      self.sacar(valor)
      destino.depositar(valor) 

   def get_saldo(self):   
      return self.__saldo

   def get_titular(self):  
      return self.__titular

   @property # trata como uma propriedade, preciso deixar o atributo 'Privado __' 
   def limite(self):
      return self.__limite   

   @staticmethod # CRIAR METODOS ESTATICOS 
   def Codigo_Banco () :
      return '001'

   @limite.setter # Alterar valores 
   def limite(self,  limite):
      self.__limite= limite   
  
 #Programa Principal     

conta = Conta(123,'Vitor', 50.0, 1000.0)
conta2 = Conta(321,'Anne', 2000.0, 1000.0)

#  TIPOS DE COMANDOS :

#conta2.depositar(100.0)
#conta2.sacar(550.0)
#conta.transferir (conta2, 20)
#print(conta2.extrato())
#print(conta2.get_saldo())
#print(conta.limite)
#conta.limite = 9000
#print(conta.limite)
#print(conta.Codigo_Banco())