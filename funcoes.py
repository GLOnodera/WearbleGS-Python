import datetime
import pickle

# Função para registrar leitura de glicose
def carregar_leituras():
    try:
        with open("leituras.pkl", "rb") as file:
            leituras = pickle.load(file)
        print("Leituras carregadas com sucesso!")
        print("Conteúdo do arquivo:")
        print(leituras)
        return leituras
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo.")
        return []
    except Exception as e:
        print(f"Erro ao carregar leituras: {e}")
        return []


def imprimir_conteudo_arquivo():
    try:
        with open("leituras.pkl", "rb") as file:
            conteudo = pickle.load(file)
        print("Conteúdo do arquivo:")
        print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

imprimir_conteudo_arquivo()

# Função para exibir o histórico de leituras
def ver_historico(leituras):
    if not leituras:
        print("Nenhum dado disponível no histórico.")
    else:
        print("\n===== Histórico de Leituras =====")
        for i, leitura in enumerate(leituras, start=1):
            print(f"{i}. Nível de Glicose: {leitura['Nível de Glicose']} - Data e Hora: {leitura['Data e Hora']}")

# Função para calibrar o dispositivo
def calibrar_dispositivo():
    print("Calibrando dispositivo...")

# Função para calcular a média das leituras
def calcular_media(leituras):
    if not leituras:
        print("Nenhum dado disponível para calcular a média.")
    else:
        media = sum(leitura['Nível de Glicose'] for leitura in leituras) / len(leituras)
        print(f"A média das leituras é: {media}")

# Função para salvar as leituras em um arquivo
def salvar_leituras(leituras):
    with open("leituras.pkl", "wb") as file:
        pickle.dump(leituras, file)
    print("Leituras salvas com sucesso!")

# Função para carregar leituras de um arquivo
def carregar_leituras():
    try:
        with open("leituras.pkl", "rb") as file:
            leituras = pickle.load(file)
        print("Leituras carregadas com sucesso!")
        return leituras
    except FileNotFoundError:
        return []

# Função principal
def main():
    from menu import exibir_menu

    leituras_glicose = carregar_leituras()

    while True:
        exibir_menu()

        opcao = input("\nSelecione uma opção (1-5): ")

        if opcao == '1':
            registrar_leitura(leituras_glicose)
        elif opcao == '2':
            ver_historico(leituras_glicose)
        elif opcao == '3':
            calibrar_dispositivo()
        elif opcao == '4':
            calcular_media(leituras_glicose)
        elif opcao == '5':
            salvar_leituras(leituras_glicose)
            print("Saindo do programa. Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
