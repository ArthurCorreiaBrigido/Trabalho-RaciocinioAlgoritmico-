import json
import csv

# Função para adicionar um item ao inventário
def adicionar_item(inventario, nome, preco, quantidade):
    if nome in inventario:
        print(f"O item '{nome}' já existe no inventário.")
    else:
        inventario[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Item '{nome}' adicionado com sucesso!")

# Função para remover um item do inventário
def remover_item(inventario, nome):
    if nome in inventario:
        del inventario[nome]
        print(f"Item '{nome}' removido com sucesso!")
    else:
        print(f"O item '{nome}' não existe no inventário.")

# Função para atualizar a quantidade de um item no inventário
def atualizar_quantidade(inventario, nome, quantidade):
    if nome in inventario:
        inventario[nome]['quantidade'] = quantidade
        print(f"Quantidade do item '{nome}' atualizada para {quantidade}.")
    else:
        print(f"O item '{nome}' não existe no inventário.")

# Função para listar todos os itens do inventário
def listar_itens(inventario):
    for nome, detalhes in inventario.items():
        print(f"{nome}: Preco: {detalhes['preco']} Quantidade: {detalhes['quantidade']}")

# Função para procurar um item pelo nome
def procurar_item(inventario, nome):
    if nome in inventario:
        detalhes = inventario[nome]
        print(f"{nome}: Preco: {detalhes['preco']} Quantidade: {detalhes['quantidade']}")
    else:
        print(f"O item '{nome}' não foi encontrado no inventário.")

# Função para salvar o inventário em um arquivo
def salvar_inventario(inventario, arquivo):
    try:
        with open(arquivo, 'w') as f:
            json.dump(inventario, f)
        print(f"Inventário salvo em '{arquivo}' com sucesso.")
    except IOError as e:
        print(f"Erro ao salvar o inventário: {e}")

# Função para carregar o inventário de um arquivo
def carregar_inventario(arquivo):
    try:
        with open(arquivo, 'r') as f:
            inventario = json.load(f)
        print(f"Inventário carregado de '{arquivo}' com sucesso.")
        return inventario
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado. Um novo inventário será criado.")
        return {}
# Função para atualizar o preço de um item no inventário
def atualizar_preco(inventario, nome, preco):
    if nome in inventario:
        inventario[nome]['preco'] = preco
        print(f"Preco do item '{nome}' atualizado para {preco}.")
    else:
        print(f"O item '{nome}' não existe no inventário.")

# Função para exibir estatísticas do inventário
def estatisticas_inventario(inventario):
    total_itens = len(inventario)
    valor_total = sum(item['preco'] * item['quantidade'] for item in inventario.values())
    print(f"Total de itens: {total_itens}")
    print(f"Valor total do estoque: {valor_total:.2f}")

# Função para exportar o inventário para um arquivo CSV
def exportar_inventario_csv(inventario, arquivo):
    try:
        with open(arquivo, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # Escrevendo os cabeçalhos das colunas
            writer.writerow(['Item', 'Preco(R$)', 'Quantidade'])
            # Escrevendo as linhas de dados
            for nome, detalhes in inventario.items():
                writer.writerow([nome, detalhes['preco'], detalhes['quantidade']])
        print(f"Inventário exportado para '{arquivo}' com sucesso.")
    except IOError as e:
        print(f"Erro ao exportar o inventário: {e}")

# Programa principal
def main():
    arquivo_inventario = 'inventario.json'
    inventario = carregar_inventario(arquivo_inventario)

    # Interface simples de linha de comando
    while True:
        print("\nGerenciador de Inventário")
        print("1 - Adicionar Item")
        print("2 - Remover Item")
        print("3 - Atualizar Quantidade de um Item")
        print("4 - Listar Itens do Inventário")
        print("5 - Procurar um Item")
        print("6 - Salvar Inventário")
        print("7 - Atualizar Preço de um Item")
        print("8 - Estatísticas do Inventário")
        print("9 - Exportar Inventário para CSV")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            quantidade = int(input("Quantidade do item: "))
            adicionar_item(inventario, nome, preco, quantidade)
        elif opcao == '2':
            nome = input("Nome do item a remover: ")
            remover_item(inventario, nome)
        elif opcao == '3':
            nome = input("Nome do item: ")
            quantidade = int(input("Nova quantidade do item: "))
            atualizar_quantidade(inventario, nome, quantidade)
        elif opcao == '4':
            listar_itens(inventario)
        elif opcao == '5':
            nome = input("Nome do item a procurar: ")
            procurar_item(inventario, nome)
        elif opcao == '6':
            salvar_inventario(inventario, arquivo_inventario)
        elif opcao == '7':
            nome = input("Nome do item: ")
            preco = float(input("Novo preço do item: "))
            atualizar_preco(inventario, nome, preco)
        elif opcao == '8':
            estatisticas_inventario(inventario)
        elif opcao == '9':
            nome_arquivo_csv = input("Nome do arquivo CSV (ex: inventario.csv): ")
            exportar_inventario_csv(inventario, nome_arquivo_csv)
        elif opcao == '0':
            salvar_inventario(inventario, arquivo_inventario)
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
