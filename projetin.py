while True:
 num1 = float(input("Insira um número: "))
 num2 = float(input("Insira outro número: "))
 metodo = int(input("Qual método deseja (1 - Adição; 2 - Subtração; 3 - Multiplicação; 4 - Divisão)?: "))   

 if metodo == 1:
      print("Resultado: ", num1 + num2)
 elif metodo == 2:
      print("Resultado: ", num1 - num2)
 elif metodo == 3:
      print("Resultado: ", num1 * num2)
 elif metodo == 4:
      if num1 != 0:
        print("Resultado: ", num1 / num2)
      else:
        print("ERRO! Impossível dividir por zero!")
 else:
      print("ERRO! Essa opção não existe, insira qualquer número de 1 à 4!")

 sair = int(input("Deseja encerrar o código? (1 - Sim; 0 - Não): "))
 if sair == 1:
     break
 elif sair == 0:
     continue