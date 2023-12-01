import csv
import datetime
from menu import exibir_menu

def carregar_leituras():
    try:
        with open("leituras.csv", newline='', encoding='utf-8') as file:
            leitor_csv = csv.DictReader(file)
            leituras = list(leitor_csv)
        print("Leituras carregadas com sucesso!")
        exibir_leituras(leituras)
        return leituras
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo.")
        return []
    except Exception as e:
        print(f"Erro ao carregar leituras: {e}")
        return []

def salvar_leituras(leituras):
    with open("leituras.csv", "w", newline='', encoding='utf-8') as file:
        campos = ['Nível de Glicose', 'Data e Hora']
        escritor_csv = csv.DictWriter(file, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(leituras)
    print("Leituras salvas com sucesso!")

def registrar_leitura(leituras):
    nivel_glicose = float(input("Digite o nível de glicose: "))
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    leitura = {'Nível de Glicose': nivel_glicose, 'Data e Hora': data_hora}
    leituras.append(leitura)
    print(f"Leitura registrada: {leitura}")

def exibir_leituras(leituras):
    print("\n===== Conteúdo do Arquivo =====")
    for i, leitura in enumerate(leituras, start=1):
        print(f"{i}. Nível de Glicose: {leitura['Nível de Glicose']} - Data e Hora: {leitura['Data e Hora']}")

def ver_historico(leituras):
    if not leituras:
        print("Nenhum dado disponível no histórico.")
    else:
        exibir_leituras(leituras)

def calibrar_dispositivo():
    print("Calibrando dispositivo...")

def calcular_media(leituras):
    if not leituras:
        print("Nenhum dado disponível para calcular a média.")
    else:
        media = sum(float(leitura['Nível de Glicose']) for leitura in leituras) / len(leituras)
        print(f"A média das leituras é: {media}")

def main():
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
