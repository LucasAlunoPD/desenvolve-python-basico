import csv
from collections import namedtuple
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
#Olá criei esse script como ideia para uma loja de aluguel de equipamentos 
# Constantes
ARQUIVO_EQUIPAMENTOS = 'equipamentos.csv'
USUARIO_LOGADO = None

##################### Funções de Equipamentos #####################

def ler_equipamentos(arquivo_csv):
    equipamentos = []
    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:  # Garantir que a linha tenha 4 campos
                id_equipamento, nome, quantidade, preco = row
                equipamentos.append((id_equipamento, nome, quantidade, preco))
            else:
                print(f"[Aviso] Linha ignorada: {row}")
    return equipamentos


# Função para adicionar um novo equipamento.
def adicionar_equipamento(equipamentos, arquivo_csv):
    console.print(Panel('[bold green]Cadastro de Novo Equipamento[/bold green]\nPor favor, insira os dados do novo equipamento.', 
                        title="Novo Equipamento", expand=False))

    nome = Prompt.ask("[bold cyan]Nome do Equipamento[/bold cyan]")
    quantidade = Prompt.ask("[bold cyan]Quantidade[/bold cyan]", default="1", type=int)
    preco = Prompt.ask("[bold cyan]Preço por unidade[/bold cyan]", type=float)

    id_equipamento = str(len(equipamentos) + 1)  # Atribuindo um ID sequencial para o novo equipamento

    # Adicionando o equipamento no arquivo
    with open(arquivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_equipamento, nome, quantidade, preco]) 
    
    console.print(f"[bold green]Equipamento '{nome}' cadastrado com sucesso![/bold green]")
    return id_equipamento

# Função para atualizar os dados de um equipamento (quantidade ou preço).
def atualizar_equipamento(equipamentos, arquivo_csv):
    console.print(Panel('[bold yellow]Atualização de Equipamento[/bold yellow]\nPor favor, informe o ID do equipamento a ser atualizado.', 
                        title="Atualizar Equipamento", expand=False))

    id_equipamento = Prompt.ask("[bold cyan]ID do Equipamento[/bold cyan]")

    if id_equipamento not in equipamentos:
        console.print(f"[bold red]Equipamento com ID '{id_equipamento}' não encontrado![/bold red]")
        return False
    
    novo_nome = Prompt.ask("[bold cyan]Novo Nome do Equipamento[/bold cyan]", default=equipamentos[id_equipamento].nome)
    nova_quantidade = Prompt.ask("[bold cyan]Nova Quantidade[/bold cyan]", default=str(equipamentos[id_equipamento].quantidade), type=int)
    novo_preco = Prompt.ask("[bold cyan]Novo Preço por unidade[/bold cyan]", default=str(equipamentos[id_equipamento].preco), type=float)

    # Atualizando os dados do equipamento
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for eq in equipamentos.values():
            if eq.id == id_equipamento:
                writer.writerow([id_equipamento, novo_nome, nova_quantidade, novo_preco])
            else:
                writer.writerow([eq.id, eq.nome, eq.quantidade, eq.preco])
    
    console.print(f"[bold green]Equipamento '{id_equipamento}' atualizado com sucesso![/bold green]")
    return True

# Função para excluir um equipamento.
def excluir_equipamento(equipamentos, arquivo_csv):
    console.print(Panel('[bold red]Exclusão de Equipamento[/bold red]\nPor favor, informe o ID do equipamento a ser excluído.', 
                        title="Excluir Equipamento", expand=False))

    id_equipamento = Prompt.ask("[bold cyan]ID do Equipamento[/bold cyan]")

    if id_equipamento not in equipamentos:
        console.print(f"[bold red]Equipamento com ID '{id_equipamento}' não encontrado![/bold red]")
        return False

    # Removendo o equipamento do arquivo
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for eq in equipamentos.values():
            if eq.id != id_equipamento:
                writer.writerow([eq.id, eq.nome, eq.quantidade, eq.preco])
    
    console.print(f"[bold green]Equipamento '{id_equipamento}' excluído com sucesso![/bold green]")
    return True

##################### Funções de Menu ########################

# Função para exibir o menu inicial.
def menu_inicial():
    console.print(Panel("[bold green]Sistema de Aluguel de Equipamentos[/bold green]\nEscolha uma das opções abaixo:", title="Menu Inicial", expand=False))
    console.print("[bold cyan]1.[/bold cyan] [bold white]Login[/bold white]")
    console.print("[bold cyan]2.[/bold cyan] [bold white]Cadastrar Novo Equipamento[/bold white]")
    console.print("[bold cyan]3.[/bold cyan] [bold white]Sair[/bold white]")
    opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["1", "2", "3"])
    return opcao

# Função para exibir o menu de operações internas.
def menu_interno():
    console.print(Panel(f"[bold green]Olá {USUARIO_LOGADO}!\nEscolha uma das opções abaixo:", title="Menu Interno", expand=False))
    console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar Equipamento[/bold white]")
    console.print("[bold cyan]2.[/bold cyan] [bold white]Excluir Equipamento[/bold white]")
    console.print("[bold cyan]3.[/bold cyan] [bold white]Listar Equipamentos[/bold white]")
    console.print("[bold cyan]0.[/bold cyan] [bold white]Logout[/bold white]")
    
    opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0", "1", "2", "3"])
    return opcao

##################### Fluxo Principal ##########################

console = Console()
equipamentos = ler_equipamentos(ARQUIVO_EQUIPAMENTOS)
while True:
    opcao = menu_inicial()
    
    if opcao == "1":
        # A lógica de login do administrador pode ser mantida aqui, se necessário
        USUARIO_LOGADO = 'admin'  # Definindo um usuário logado como exemplo
    elif opcao == "2":
        adicionar_equipamento(equipamentos, ARQUIVO_EQUIPAMENTOS)
        equipamentos = ler_equipamentos(ARQUIVO_EQUIPAMENTOS)
    elif opcao == "3":
        break

    if USUARIO_LOGADO:
        while True:
            opcao = menu_interno()
            if opcao == '0': break
            elif opcao == "1":
                atualizar_equipamento(equipamentos, ARQUIVO_EQUIPAMENTOS)
                equipamentos = ler_equipamentos(ARQUIVO_EQUIPAMENTOS)
            elif opcao == "2":
                excluir_equipamento(equipamentos, ARQUIVO_EQUIPAMENTOS)
                equipamentos = ler_equipamentos(ARQUIVO_EQUIPAMENTOS)
            elif opcao == "3":
                console.print("[bold cyan]Lista de Equipamentos:[/bold cyan]")
                for eq in equipamentos.values():
                    console.print(f"[bold white]{eq.id} - {eq.nome} - {eq.quantidade} unidades - R${eq.preco:.2f} por unidade[/bold white]")


