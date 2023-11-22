import datetime
import pickle

# Função para exibir o menu principal
def exibir_menu():
    print("\n===== Menu Principal =====")
    print("1. Registrar Leitura de Glicose")
    print("2. Ver Histórico de Leituras")
    print("3. Calibrar Dispositivo")
    print("4. Calcular Média das Leituras")
    print("5. Sair")

# Função para registrar leitura de glicose
def registrar_leitura(leituras):
    try:
        nivel_glicose = float(input("Informe o nível de glicose: "))
        data_hora = datetime.datetime.now()
        leitura = {"Nível de Glicose": nivel_glicose, "Data e Hora": data_hora}
        leituras.append(leitura)
        print("Leitura registrada com sucesso!")
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido.")

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
    