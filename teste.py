# # # # # # # # livros = []  # Lista para armazenar os livros cadastrados
# # # # # # # # generos = []  # Lista para armazenar os gêneros dos livros
# # # # # # # # bibliotecaUsuario = []  # Lista para armazenar os livros que o usuário pegou

# # # # # # # # def mostrar_livros():
# # # # # # # #     if not livros:
# # # # # # # #         print("Não há nenhum livro cadastrado.")
# # # # # # # #     else:
# # # # # # # #         print("Lista de livros cadastrados:")
# # # # # # # #         for i in range(len(livros)):
# # # # # # # #             print(f"{i + 1} - {livros[i]} - {generos[i]}")

# # # # # # # # def biblioteca_Usuario():
# # # # # # # #     if not bibliotecaUsuario:
# # # # # # # #         print("Não há nenhum livro na sua biblioteca.")
# # # # # # # #     else:
# # # # # # # #         print("Seus livros salvos:")
# # # # # # # #         for i in range(len(bibliotecaUsuario)):
# # # # # # # #             print(f"{i + 1} - {bibliotecaUsuario[i]}")

# # # # # # # # # Exemplo de cadastramento de alguns livros para testes
# # # # # # # # livros.extend(["Harry Potter", "Senhor dos Anéis", "O Hobbit"])
# # # # # # # # generos.extend(["Fantasia", "Fantasia", "Aventura"])

# # # # # # # # while True:
# # # # # # # #     print("\n1. Mostrar todos os livros")
# # # # # # # #     print("2. Pegar um livro")
# # # # # # # #     print("3. Mostrar minha biblioteca")
# # # # # # # #     print("4. Sair")
# # # # # # # #     escolha = input("Escolha uma opção: ")

# # # # # # # #     if escolha == "1":
# # # # # # # #         mostrar_livros()

# # # # # # # #     elif escolha == "2":
# # # # # # # #         mostrar_livros()
# # # # # # # #         try:
# # # # # # # #             posicao = int(input("Escolha a posição do livro que você deseja pegar: ")) - 1
# # # # # # # #             if 0 <= posicao < len(livros):
# # # # # # # #                 bibliotecaUsuario.append(livros[posicao])
# # # # # # # #                 print(f"O livro '{livros[posicao]}' foi adicionado à sua biblioteca.")
# # # # # # # #             else:
# # # # # # # #                 print("Posição inválida.")
# # # # # # # #         except ValueError:
# # # # # # # #             print("Por favor, digite um número válido.")

# # # # # # # #     elif escolha == "3":
# # # # # # # #         biblioteca_Usuario()

# # # # # # # #     elif escolha == "4":
# # # # # # # #         print("Saindo...")
# # # # # # # #         break

# # # # # # # #     else:
# # # # # # # #         print("Opção inválida. Tente novamente.")















# # # # # # # # # Mapeamento dos gêneros em um dicionário com as várias versões de entrada
# # # # # # # # generos = {
# # # # # # # #     "aventura": "Aventura",
# # # # # # # #     "biografia": "Biografia",
# # # # # # # #     "classico": "Clássico",
# # # # # # # #     "clássico": "Clássico",
# # # # # # # #     "distopia": "Distopia",
# # # # # # # #     "drama": "Drama",
# # # # # # # #     "fantasia": "Fantasia",
# # # # # # # #     "ficção": "Ficção",
# # # # # # # #     "filosofico": "Filosófico",
# # # # # # # #     "filosófico": "Filosófico",
# # # # # # # #     "portugues": "Português",
# # # # # # # #     "português": "Português",
# # # # # # # #     "infantil": "Infantil",
# # # # # # # #     "misterio": "Mistério",
# # # # # # # #     "mistério": "Mistério",
# # # # # # # #     "poesia": "Poesia",
# # # # # # # #     "romance": "Romance",
# # # # # # # #     "suspense": "Suspense",
# # # # # # # #     "terror": "Terror",
# # # # # # # #     "tragédia": "Tragédia",
# # # # # # # #     "tragedia": "Tragédia"
# # # # # # # # }

# # # # # # # # # Entrada do usuário
# # # # # # # # qualGenero = input("Escolha qual gênero deseja: ").strip().lower()

# # # # # # # # # Verificação do gênero usando o dicionário
# # # # # # # # if qualGenero in generos:
# # # # # # # #     genero_escolhido = generos[qualGenero]
# # # # # # # #     print(f"Gênero selecionado: {genero_escolhido}")
# # # # # # # # else:
# # # # # # # #     print("Gênero não encontrado.")
















# # # # # # # # Listas de livros e gêneros
# # # # # # # livros = [
# # # # # # #     "Harry Potter", "Senhor dos Anéis", "O Hobbit", "Dom Quixote", "O Grande Gatsby",
# # # # # # #     "Moby Dick", "Crime e Castigo", "A Divina Comédia", "Orgulho e Preconceito", "Guerra e Paz"
# # # # # # # ]
# # # # # # # generos = [
# # # # # # #     "Fantasia", "Fantasia", "Aventura", "Aventura", "Clássico",
# # # # # # #     "Aventura", "Drama", "Poesia", "Romance", "Histórico"
# # # # # # # ]

# # # # # # # # Dicionário para facilitar a verificação dos gêneros
# # # # # # # generos_map = {
# # # # # # #     "aventura": "Aventura",
# # # # # # #     "biografia": "Biografia",
# # # # # # #     "classico": "Clássico",
# # # # # # #     "clássico": "Clássico",
# # # # # # #     "distopia": "Distopia",
# # # # # # #     "drama": "Drama",
# # # # # # #     "fantasia": "Fantasia",
# # # # # # #     "ficção": "Ficção",
# # # # # # #     "filosofico": "Filosófico",
# # # # # # #     "filosófico": "Filosófico",
# # # # # # #     "portugues": "Português",
# # # # # # #     "português": "Português",
# # # # # # #     "infantil": "Infantil",
# # # # # # #     "misterio": "Mistério",
# # # # # # #     "mistério": "Mistério",
# # # # # # #     "poesia": "Poesia",
# # # # # # #     "romance": "Romance",
# # # # # # #     "suspense": "Suspense",
# # # # # # #     "terror": "Terror",
# # # # # # #     "tragédia": "Tragédia",
# # # # # # #     "tragedia": "Tragédia"
# # # # # # # }

# # # # # # # # Função para exibir livros de um gênero específico
# # # # # # # def mostrar_livros_por_genero(genero):
# # # # # # #     print(f"Livros no gênero '{genero}':")
# # # # # # #     encontrou = False
# # # # # # #     for i in range(len(livros)):
# # # # # # #         if generos[i].lower() == genero.lower():  # Verifica o gênero
# # # # # # #             print(f"- {livros[i]}")
# # # # # # #             encontrou = True
# # # # # # #     if not encontrou:
# # # # # # #         print("Nenhum livro encontrado nesse gênero.")


# # # # # # # # Solicitar o gênero ao usuário
# # # # # # # qualGenero = input("Escolha o gênero de livro que deseja ver: ").strip().lower()

# # # # # # # # Verificação do gênero e exibição dos livros correspondentes
# # # # # # # if qualGenero in generos_map:
# # # # # # #     genero_escolhido = generos_map[qualGenero]
# # # # # # #     mostrar_livros_por_genero(genero_escolhido)
# # # # # # # else:
# # # # # # #     print("Gênero não encontrado.")















# # # # # # # import os

# # # # # # # # Listas de livros e gêneros
# # # # # # # livros = [
# # # # # # #     "Harry Potter", "Senhor dos Anéis", "O Hobbit", "Dom Quixote", "O Grande Gatsby",
# # # # # # #     "Moby Dick", "Crime e Castigo", "A Divina Comédia", "Orgulho e Preconceito", "Guerra e Paz"
# # # # # # # ]
# # # # # # # generos = [
# # # # # # #     "Fantasia", "Fantasia", "Aventura", "Aventura", "Clássico",
# # # # # # #     "Aventura", "Drama", "Poesia", "Romance", "Histórico"
# # # # # # # ]

# # # # # # # # Dicionário para facilitar a verificação dos gêneros
# # # # # # # generos_map = {
# # # # # # #     "aventura": "Aventura",
# # # # # # #     "biografia": "Biografia",
# # # # # # #     "classico": "Clássico",
# # # # # # #     "clássico": "Clássico",
# # # # # # #     "distopia": "Distopia",
# # # # # # #     "drama": "Drama",
# # # # # # #     "fantasia": "Fantasia",
# # # # # # #     "ficção": "Ficção",
# # # # # # #     "filosofico": "Filosófico",
# # # # # # #     "filosófico": "Filosófico",
# # # # # # #     "portugues": "Português",
# # # # # # #     "português": "Português",
# # # # # # #     "infantil": "Infantil",
# # # # # # #     "misterio": "Mistério",
# # # # # # #     "mistério": "Mistério",
# # # # # # #     "poesia": "Poesia",
# # # # # # #     "romance": "Romance",
# # # # # # #     "suspense": "Suspense",
# # # # # # #     "terror": "Terror",
# # # # # # #     "tragédia": "Tragédia",
# # # # # # #     "tragedia": "Tragédia"
# # # # # # # }






# # # # # # # # Função para exibir livros e retornar posições de um gênero específico
# # # # # # # def livros_por_genero(genero):
# # # # # # #     posicoes = []
# # # # # # #     print(f"Livros no gênero '{genero}':")
# # # # # # #     for i in range(len(livros)):
# # # # # # #         if generos[i].lower() == genero.lower():  # Verifica o gênero
# # # # # # #             print(f"{i + 1} - {livros[i]}")
# # # # # # #             posicoes.append(i)
# # # # # # #     return posicoes


# # # # # # # # Lista para armazenar os livros do usuário
# # # # # # # bibliotecaUsuario = []








# # # # # # # # Solicitar o gênero ao usuário
# # # # # # # qualGenero = input("Escolha o gênero de livro que deseja ver: ").strip().lower()

# # # # # # # # Verificação do gênero e exibição dos livros correspondentes
# # # # # # # if qualGenero in generos_map:
# # # # # # #     genero_escolhido = generos_map[qualGenero]
# # # # # # #     posicoes_validas = livros_por_genero(genero_escolhido)

# # # # # # #     try:
# # # # # # #         # Solicita a posição do livro
# # # # # # #         posicao = int(input("\nEscolha a posição do livro que você deseja pegar, ou aperte qualquer outra tecla para voltar.\n")) - 1
# # # # # # #         os.system('cls')
        
# # # # # # #         # Verifica se a posição é válida e pertence ao gênero escolhido
# # # # # # #         if posicao in posicoes_validas:
# # # # # # #             bibliotecaUsuario.append(livros[posicao])
# # # # # # #             print(f"O livro '{livros[posicao]}' foi adicionado à sua biblioteca.")
# # # # # # #         else:
# # # # # # #             print("Este livro não pertence a este gênero, por favor tente novamente.")
# # # # # # #     except ValueError:
# # # # # # #         print("Por favor, digite um número válido.")
# # # # # # # else:
# # # # # # #     os.system('cls')
# # # # # # #     print("Gênero não encontrado, tente novamente!")








# # # # # # import os

# # # # # # # Listas para armazenar usuários e senhas
# # # # # # usuarios = []
# # # # # # senhas = []

# # # # # # # Dicionário para armazenar as bibliotecas de cada usuário
# # # # # # bibliotecas = {}

# # # # # # # Função para exibir a biblioteca de um usuário
# # # # # # def biblioteca_usuario(usuario):
# # # # # #     if usuario not in bibliotecas:
# # # # # #         print("Usuário não encontrado.")
# # # # # #         return

# # # # # #     biblioteca = bibliotecas[usuario]  # Obtem a biblioteca do usuário

# # # # # #     if not biblioteca:
# # # # # #         print("Não há nenhum livro na sua biblioteca.\n")
# # # # # #     else:
# # # # # #         print("Seus livros salvos:")
# # # # # #         for i, livro in enumerate(biblioteca, 1):
# # # # # #             print(f"{i} - {livro}")
    
# # # # # #     input("\nAperte qualquer tecla para voltar para o menu.")
# # # # # #     os.system('cls')

# # # # # # # Cadastro e login do usuário
# # # # # # while True:
# # # # # #     print(f"temos {usuarios} cadastrados")
# # # # # #     print(f"com um total de {len(usuarios)} usuarios")
# # # # # #     temCadastro = input("Você já possui cadastro? 1) sim 2) não\n")
# # # # # #     os.system('cls')
    
# # # # # #     if temCadastro == '1':  # Login
# # # # # #         print("Entrar na conta")
# # # # # #         print(20 * "-=")
# # # # # #         usuario = input("Usuário: ")
# # # # # #         senha = input("Senha: ")
# # # # # #         os.system('cls')

# # # # # #         # Verificação de login
# # # # # #         if usuario in usuarios:
# # # # # #             indice = usuarios.index(usuario)
# # # # # #             if senhas[indice] == senha:
# # # # # #                 print("Login bem-sucedido!")
# # # # # #                 biblioteca_usuario(usuario)
# # # # # #             else:
# # # # # #                 print("Senha incorreta.")
# # # # # #         else:
# # # # # #             print("Usuário não encontrado.")
# # # # # #         break

# # # # # #     elif temCadastro == '2':  # Cadastro
# # # # # #         print("\nVamos fazer seu cadastro")
# # # # # #         print(20 * "-=")
        
# # # # # #         while True:
# # # # # #             usuario = input("Digite qual vai ser seu usuário: ")
# # # # # #             senha = input("Escolha sua senha: ")

# # # # # #             # Verifica se o usuário já existe
# # # # # #             if usuario in usuarios:
# # # # # #                 print("Usuário já utilizado, tente outro!")
# # # # # #             elif usuario == '':
# # # # # #                 print("Seu usuário deve conter ao menos 1 caractere")
# # # # # #             elif len(senha) < 6:
# # # # # #                 print("Sua senha deve possuir ao menos 6 caracteres")
# # # # # #             else:
# # # # # #                 # Adiciona o novo usuário e senha
# # # # # #                 usuarios.append(usuario)
# # # # # #                 senhas.append(senha)
# # # # # #                 bibliotecas[usuario] = []  # Cria uma biblioteca vazia para o novo usuário
# # # # # #                 print("Cadastro realizado com sucesso!")
# # # # # #                 os.system('cls')
# # # # # #                 break

# # # # # #     else:
# # # # # #         os.system('cls')
# # # # # #         print("Digite uma das duas opções, 1 ou 2.")


















# # # # # import os
# # # # # from py.defs import bibliotecas, voltando, livros_por_genero, livros, usuario
# # # # # from py.db import generos_map



# # # # # # Função para mostrar a biblioteca de um usuário específico
# # # # # def biblioteca_usuario(usuario):
# # # # #     if not bibliotecas[usuario]:  # Verifica se a biblioteca do usuário está vazia
# # # # #         print("Não há nenhum livro na sua biblioteca.\n")
# # # # #     else:
# # # # #         print("Seus livros salvos:")
# # # # #         for i, livro in enumerate(bibliotecas[usuario], 1):
# # # # #             print(f"{i} - {livro}\n")
# # # # #     input("Aperte qualquer tecla para voltar para o menu.")
# # # # #     os.system('cls')


# # # # # # Função para adicionar livros na biblioteca do usuário
# # # # # def escolher_livro(usuario):
# # # # #     separar = input("\nDeseja separar a biblioteca por gênero? \n1) Sim \n2) Não \n3) Voltar\n")
# # # # #     os.system('cls')

# # # # #     if separar == '1':
# # # # #         while True:
# # # # #             print("\naventura\nbiografia\nclássico\ndistopia\ndrama\nfantasia\nficção\nfilosófico\nportuguês\ninfantil\nmistério\npoesia\nromance\nsuspense\nterror\ntragédia\n")
# # # # #             print(20 * "-=")
# # # # #             qualGenero = input("Escolha o gênero de livro que deseja ver, ou digite \"voltar\", para voltar ao menu.\n").strip().lower()
            
# # # # #             if qualGenero == 'voltar':
# # # # #                 voltando()
# # # # #                 break
# # # # #             elif qualGenero in generos_map:   # Verificação do gênero
# # # # #                 genero_escolhido = generos_map[qualGenero]
# # # # #                 livros_do_genero = livros_por_genero(genero_escolhido)
                
# # # # #                 try:
# # # # #                     posicao = int(input("\nEscolha a posição do livro que você deseja pegar, ou aperte qualquer tecla para voltar.\n")) - 1
# # # # #                     os.system('cls')
                    
# # # # #                     if 0 <= posicao < len(livros):  # Verifica se a posição é válida
# # # # #                         livro_escolhido = livros[posicao]
                        
# # # # #                         if livro_escolhido not in bibliotecas[usuario]:  # Verifica se o livro já está na biblioteca do usuário
# # # # #                             bibliotecas[usuario].append(livro_escolhido)
# # # # #                             print(f"O livro '{livro_escolhido}' foi adicionado à sua biblioteca.")
# # # # #                         else:
# # # # #                             print("Este livro já está na sua biblioteca.")
# # # # #                     else:
# # # # #                         print("Posição inválida. Tente novamente.")
# # # # #                 except ValueError:
# # # # #                     voltando()
# # # # #             else:
# # # # #                 os.system('cls')
# # # # #                 print("Gênero não encontrado, tente novamente!")

# # # # # # Uso do dicionário 'bibliotecas' ao registrar o usuário
# # # # # if usuario not in bibliotecas:
# # # # #     bibliotecas[usuario] = []

# # # # # # Chamada das funções ajustada para incluir o parâmetro 'usuario'
# # # # # biblioteca_usuario(usuario)








# # # # # Inicializando o dicionário de bibliotecas
# # # # bibliotecas = {}

# # # # # Simulação de lista de livros
# # # # livros = ["Livro A", "Livro B", "Livro C"]

# # # # # Função para adicionar livros à biblioteca de um usuário
# # # # def adicionar_livro(usuario, posicao):
# # # #     if usuario not in bibliotecas:
# # # #         bibliotecas[usuario] = []  # Se o usuário não tem biblioteca, cria uma lista vazia
    
# # # #     # Adiciona o livro na posição indicada
# # # #     bibliotecas[usuario].append(livros[posicao])

# # # # # Exemplo de uso
# # # # adicionar_livro("fernando", 1)  # Fernando escolheu o Livro A
# # # # adicionar_livro("fernando", 2)  # Fernando escolheu o Livro C

# # # # adicionar_livro("bernardo", 1)  # Bernardo escolheu o Livro B

# # # # # Exibindo o dicionário de bibliotecas
# # # # print(bibliotecas)







# # # # Exemplo de dicionário
# # # bibliotecas = {
# # #     "fernando": ["Livro A", "Livro B", "Livro C"],
# # #     "bernardo": ["Livro X", "Livro Y"]
# # # }

# # # # Nome do usuário que deseja deletar
# # # usuario = "bernardo"

# # # # Verifica se o usuário existe no dicionário antes de deletar
# # # if usuario in bibliotecas:
# # #     del bibliotecas[usuario]
# # #     print(f"O usuário '{usuario}' foi deletado com sucesso.")
# # # else:
# # #     print(f"O usuário '{usuario}' não foi encontrado.")

# # # # Exibindo o dicionário após a exclusão
# # # print(bibliotecas)









# # # Exemplo de dicionário de bibliotecas
# # bibliotecas = {
# #     "fernando": ["Livro A", "Livro B", "Livro C"],
# #     "bernardo": ["Livro X", "Livro Y"]
# # }

# # # Nome do usuário antigo e o novo nome do usuário
# # usuario_antigo = "fernando"
# # novo_usuario = "fernando_novo"

# # # Verifica se o usuário antigo existe antes de realizar a operação
# # if usuario_antigo in bibliotecas:
# #     # Copia o valor da biblioteca para a nova chave e apaga a chave antiga
# #     bibliotecas[novo_usuario] = bibliotecas.pop(usuario_antigo)
# #     print(f"O nome de usuário foi alterado de '{usuario_antigo}' para '{novo_usuario}'.")
# # else:
# #     print(f"O usuário '{usuario_antigo}' não foi encontrado.")

# # # Exibindo o dicionário após a operação
# # print(bibliotecas)



# # usuarios = ["usuario1", "usuario2", "usuario3"]  # Array com os usuários cadastrados

# # print("Usuários cadastrados:")
# # for i, usuario in enumerate(usuarios, 1):
# #     print(f"{i} - {usuario}")



# # def mostra_biblioteca_usuario(bibliotecas):
# #     # Seleciona o usuário para exibir a biblioteca
# #     escolha = int(input("\nEscolha o número do usuário para ver os livros: "))
# #     if 1 <= escolha <= len(usuarios):
# #         usuario_selecionado = usuarios[escolha - 1]
# #         livros = bibliotecas.get(usuario_selecionado, [])
        
# #         # Exibe a biblioteca do usuário selecionado
# #         print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
# #         print(usuario_selecionado)
# #         for i, livro in enumerate(livros, 1):
# #             print(f"{i} - {livro}")
# #     else:   
# #         print("Escolha inválida.")

# # # Exemplo de dicionário de bibliotecas
# # bibliotecas = {
# #     "fernando": ["livro A", "livro B", "livro C"],
# #     "bernardo": ["livro D", "livro E"],
# #     "nikolas": ["livro F", "livro G", "livro H", "livro I"]
# # }

# # # Chamando a função
# # mostra_biblioteca_usuario(bibliotecas)







# def excluir_livro_usuario(bibliotecas):
#     # Exibe todos os usuários cadastrados
#     print("Usuários cadastrados:")
#     usuarios = list(bibliotecas.keys())
    
#     for i, usuario in enumerate(usuarios, 1):
#         print(f"{i} - {usuario}")

#     # Seleciona o usuário para excluir um livro
#     escolha = int(input("\nEscolha o número do usuário para excluir um livro: "))
#     if 1 <= escolha <= len(usuarios):
#         usuario_selecionado = usuarios[escolha - 1]
#         livros = bibliotecas.get(usuario_selecionado, [])
        
#         if not livros:
#             print("Este usuário não tem nenhum livro na sua biblioteca.")
#         else:
#             print(f"\nLivros na biblioteca de {usuario_selecionado}:")
#             for i, livro in enumerate(livros, 1):
#                 print(f"{i} - {livro}")
            
#             # Escolhe o livro para excluir
#             livro_escolha = int(input("\nEscolha o número do livro para excluir: "))
#             if 1 <= livro_escolha <= len(livros):
#                 livro_removido = livros.pop(livro_escolha - 1)
#                 print(f"O livro '{livro_removido}' foi removido da biblioteca de {usuario_selecionado}.")
#             else:
#                 print("Escolha de livro inválida.")
#     else:
#         print("Escolha de usuário inválida.")

# # Exemplo de dicionário de bibliotecas
# bibliotecas = {
#     "fernando": ["livro A", "livro B", "livro C"],
#     "bernardo": ["livro D", "livro E"],
#     "nikolas": ["livro F", "livro G", "livro H", "livro I"]
# }

# # Chamando a função
# excluir_livro_usuario(bibliotecas)








# import os

# def mostra_usuarios():
#     if len(usuarios) <= 1 or not usuarios[1]:  # Verifica se há usuários além do admin
#         print("Não há nenhum usuário cadastrado.\n")
#         input("Aperte qualquer tecla para voltar para o menu.")
#         os.system('cls')
#     else:
#         print("Usuários cadastrados:")
#         for i, usuario in enumerate(usuarios[1:], 1):  # Começa a partir do segundo item
#             print(f"{i} - {usuario}")

# def voltando():
#     input("Voltando ao menu... Aperte qualquer tecla.")

# # Exemplo de dicionários
# usuarios = ["admin", "fernando", "bernardo", "nikolas"]
# bibliotecas = {
#     "fernando": ["livro A", "livro B", "livro C"],
#     "bernardo": ["livro D", "livro E"],
#     "nikolas": ["livro F", "livro G", "livro H", "livro I"]
# }

# def verificar_biblioteca_usuario():
#     os.system('cls')
#     if len(usuarios) <= 1 or not usuarios[1]:
#         mostra_usuarios()
#         voltando()
#     else:
#         while True:
#             try:
#                 mostra_usuarios()
#                 print(20 * "-=")
#                 posicao = int(input("\nEscolha a posição do usuário que deseja verificar sua biblioteca. \nOu aperte qualquer tecla para voltar.\n")) - 1
#                 os.system('cls')
                
#                 if 0 <= posicao < (len(usuarios) - 1):  # Verifica se a posição é válida
#                     usuario_selecionado = usuarios[posicao + 1]  # Corrige o índice para evitar erro
#                     livros = bibliotecas.get(usuario_selecionado, [])
                    
#                     # Exibe a biblioteca do usuário selecionado
#                     print(20 * "-=")
#                     print("\n\nUsuário:", usuario_selecionado)
#                     if not livros:
#                         print("Este usuário não tem nenhum livro na sua biblioteca.")
#                     else:
#                         for i, livro in enumerate(livros, 1):
#                             print(f"{i} - {livro}")

#                     input("Pressione qualquer tecla para voltar.")
#                     voltando()
#                     break
#                 else:
#                     print("Não existe usuário nesta posição, tente novamente!")
#             except ValueError:
#                 voltando()
#                 break

# # Chamando a função para verificar
# verificar_biblioteca_usuario()











# mostra_usuarios()
# menu_usuarios = input("\n1) Excluir um usuário \n2) Visualizar biblioteca de usuário \n3) Voltar\n")
# if menu_usuarios == '1':
#     # Escolhe o usuário para excluir
#     os.system('cls')
#     mostra_usuarios()
#     usuario_escolha = int(input("\nEscolha o número do usuário para excluir: "))
    
#     # Verifica se a escolha é válida e se não está tentando excluir o admin
#     if 1 <= usuario_escolha < len(usuarios):  
#         os.system('cls')
#         usuario_removido = usuarios.pop(usuario_escolha)
#         bibliotecas.pop(usuario_removido, None)  # Remove a biblioteca do usuário, se existir
#         print(f"Foi removido o cadastro de '{usuario_removido}' da Livraria.")
#     else:
#         print("Escolha de usuário inválida.")
    
#     input("\nAperte qualquer tecla para voltar para o menu.")
#     voltando()
