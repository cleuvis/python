import os
restaurantes=[{'nome':'praça','categoria':"Japonesa",'ativo':False},
              {'nome':'pizza','categoria':"pizza",'ativo':True},
              {'nome':'cantina','categoria':"Italiano",'ativo':False}]

def exibir_nome_do_Programa():
 print("⟆Ꭿᑲᗝᖇ ᕮⲭᕈᖇ∈⟆⟆ \n")

def exibir_Opcoes():
 print("1. Cadastrar restaurante")
 print("2. Listar restaurante")
 print("3. Ativar restaurante")
 print("4. Sair  \n")

def cadastrar_novo_restaurante():
    """Essa funçao é responsavel por cadastrar novos restaurantes! """
    exibir_subtitulo("Cadastro de novos restaurantes \n")
    nomeDoRestaurante= input("Digite o nome do restaurante que deseja cadastrar: ")
    nome_do_restaurante=nomeDoRestaurante.lower()
    categoria=input(f"Digite o nome da categoria do restaurante {nome_do_restaurante} : ")
    dados_do_restaurante=({"nome":nome_do_restaurante , "categoria":categoria , "ativo":False})
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ")
    voltar_ao_menu_principal()
    
def listar_restaurantes():
 exibir_subtitulo("Listando os restaurantes \n")
 for restaurante in restaurantes:
  nome_restaurante=restaurante['nome']
  categoria=restaurante['categoria']
  ativo=restaurante["ativo"]
  print(f"-{nome_restaurante} | {categoria} | {ativo}")
 voltar_ao_menu_principal()

def alternar_estado_restaurante():
  exibir_subtitulo('Alterando estado do restaurante. ')
  restaurante_encontrado=False
  nomeRestaurante=input("Digite o nome do restaurante que deseja alterar o estado: ")
  nome_restaurante=nomeRestaurante.lower()
  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado=True
      restaurante["ativo"]=not restaurante["ativo"]
      mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso. ' if restaurante['ativo'] else f'O restuarante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)
      #listar_restaurantes()  
  if not restaurante_encontrado:
     print("restaurante nao foi encontrado !")
  voltar_ao_menu_principal() 

def exibir_subtitulo(texto):
  os.system('cls')
  print(texto)

def voltar_ao_menu_principal():
  input("\nDigite uma tecla para voltar ao menu ")
  main()

def opcao_invalida():
  print("opção inválida!")
  voltar_ao_menu_principal("Digite uma tecla para voltar ao menu principal. ")

def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    
def escolher_Opção():
 try:
  opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida)

  if opcao_escolhida == 1:
   cadastrar_novo_restaurante()

  elif opcao_escolhida ==2:
   listar_restaurantes()
  elif opcao_escolhida == 3:
   alternar_estado_restaurante()
  elif opcao_escolhida ==4:
   finalizar_app()
  else:
   opcao_invalida()
 except:
  opcao_invalida()

def main():
 #limpar_terminal()
 os.system('cls')
 exibir_nome_do_Programa()
 exibir_Opcoes()
 escolher_Opção()
       
if __name__=="__main__":
 main()
 


