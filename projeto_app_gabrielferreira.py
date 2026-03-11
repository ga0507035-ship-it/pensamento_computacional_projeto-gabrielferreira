'''
CRUD

AÇÃI



#SISTEMA DE AGENDAMENTO DE AULAS - MEET

print('Sistema de Agendamento de Aulas - Meet')

id_usuario = input('Seja bem-vindo! Digite seu nome para continuar: ')

print("\n" + "😁" * 14)

aluno_turma = input('Digite sua turma: ("a", "b", "c", "d"): ')
email_usuario = input('Digite seu e-mail ("nome.sobrenome@gmail.com"): ')

print("Confirmando agendamento...")
print("Aula agendada com sucesso!")

while True:
    print('\n1 - Agendar aula')
    print('2 - Exibir agenda')
    print('0 - Sair')

    acesso_menu = input('Escolha uma opção: ')

    if acesso_menu == '1':
        nome_aluno = input('Digite o nome do aluno: ')
        print('Aula agendada com sucesso!')

    elif acesso_menu == '2':
        print('Exibindo agenda...\n')

        print('::Programação Python::')
        print('')
        print('Turma A - Segunda e Quarta')
        print('')
        print('Turma A 10:00 - 12:00')

    elif acesso_menu == '0':
        print('Saindo do Sistema. Até logo...')
        break

    else:
        print('Opção inválida!')



#AÇÃITERIA
(exemplo)
print('\n === Sistema de Açãiteria === \n')
print("1. Cadastro no Aplicativo")
print("2. Número de telefone")
print("3.Agendar Pedido")
print("4. Promoções e ofertas")
print("5. Cancelamento")
print("6. Constatar o Suporte")
print("7. Feedback e Avaliações")



while True:

  escolha_menu = input('\n Cadastro no Aplicativo')
if escolha_menu == '1':
 print('Agendamento do Cliente...')
 nome_do_cliente = ipunt("Digite o Nome do Cliente")
 telefone_cliente = input('Digite o Telefone do Cliente')
 #Código para agendar cliente
  
elif escolha_menu == '0':
   


   print('Saindo do Sistema. Até Logo!')


else:

   print('Opção Inválida. Por Favor, Tente Novamente')


   #TRABALHO REAL
   [

{"id": 1, "nome": "Copo Clássico", "preco": 15.00},
{"id": 2, "nome": "Barca Especial", "preco": 35.00},
{"id": 3, "nome": "Copo Kids", "preco": 10.00},
{"id": 4, "nome": "Açaí Fit (Zero)", "preco": 18.00},
{"id": 5, "nome": "Copo Trufado", "preco": 22.00},
{"id": 6, "nome": "Super Shake Açaí", "preco": 20.00},

]

print("=== BEM-VINDO À AÇAITERIA EXPRESS (ESTILO IFOOD) ===")

# --- COMANDO DE CADASTRO ---
nome_usuario = input("Para começar, digite seu nome de usuário: ")
senha_usuario = input("Crie uma senha: ")
print(f"\nCadastro realizado com sucesso, {nome_usuario}!")

# --- SISTEMA PRINCIPAL (WHILE TRUE) ---
while True:
    print("\n" + "="*30)
    print(f"USUÁRIO: {nome_usuario}")
    print("1. Ver Cardápio")
    print("2. Fazer Pedido")
    print("3. Sair do Sistema")
    print("="*30)
    
    opcao = input("Escolha uma opção: ")

    # --- COMANDO IF / ELIF / ELSE ---
    if opcao == "1":
        print("\n--- NOSSO CARDÁPIO ---")
        for item in cardapio:
            print(f"ID: {item['id']} | {item['nome']} - R$ {item['preco']:.2f}")
    
    elif opcao == "2":
        print("\n--- ÁREA DE PEDIDOS ---")
        id_pedido = int(input("Digite o ID do açaí que deseja: "))
        
        # Busca o item no cardápio
        achou = False
        for item in cardapio:
            if item["id"] == id_pedido:
                print(f"✅ {item['nome']} adicionado ao carrinho!")
                print(f"Total a pagar: R$ {item['preco']:.2f}")
                achou = True
                break
        
        if not achou:
            print("❌ ID Inválido! Tente novamente.")

    elif opcao == "3":
        print(f"\nEncerrando o aplicativo... Até logo, {nome_usuario}!")
        # --- COMANDO BREAK (SAIR DO LOOP) ---
        break
    
    else:
        print("⚠️ Opção inválida! Escolha 1, 2 ou 3.")

print("\n[Sistema Finalizado]")



#CALCULADORA SIMPLES 

print('\nCalculadora simples - Python Vocação\n')

numb_hum = input('Digite o primeiro número: ')
numb_dois = input('Digite o segundo número: ')

operar_numb = input('Escolha a operação: +, -, *, / : ')

if operar_numb == '/':
    result = int(numb_hum) / int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '*':
    result = int(numb_hum) * int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '+':
    result = int(numb_hum) + int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '-':
    result = int(numb_hum) - int(numb_dois)
    print(f'O resultado é: {result}')

else:
    print('Operação inválida.')
  
