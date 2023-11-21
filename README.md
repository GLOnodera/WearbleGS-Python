# Registro de Glicose

Este é um programa simples em Python para registrar leituras de níveis de glicose, permitindo que o usuário realize operações como registrar leituras, visualizar o histórico, calibrar o dispositivo, calcular a média das leituras e sair do programa.

## Funcionalidades

1. **Menu Principal:**
   - Um menu principal é exibido com opções numeradas de 1 a 5.
   - As opções incluem registrar leitura de glicose, ver histórico de leituras, calibrar dispositivo, calcular média das leituras e sair.

2. **Registrar Leitura de Glicose:**
   - Solicita ao usuário que insira o nível de glicose.
   - Registra a leitura com a data e hora atuais.

3. **Ver Histórico de Leituras:**
   - Exibe o histórico de leituras, incluindo o nível de glicose e a data e hora de cada leitura.

4. **Calibrar Dispositivo:**
   - Simula a calibração do dispositivo, exibindo uma mensagem indicando o processo.

5. **Calcular Média das Leituras:**
   - Calcula e exibe a média dos níveis de glicose registrados.

6. **Salvar e Carregar Dados:**
   - As leituras são salvas em um arquivo (`leituras.pkl`) para persistência de dados entre execuções.
   - Ao iniciar o programa, as leituras anteriores são carregadas, se disponíveis.

7. **Tratamento de Erros:**
   - O programa trata erros, como inserção de valores não numéricos durante o registro de leituras.

## Utilização

1. Execute o script em um ambiente Python.
2. Escolha as opções no menu digitando o número correspondente.
3. Siga as instruções para realizar as operações desejadas.

## Observações

- Certifique-se de ter as permissões necessárias para gravar e ler arquivos no diretório onde o script está sendo executado.
- Os dados são salvos no arquivo `leituras.pkl` e carregados automaticamente ao iniciar o programa.

## Participantes

- Gabriel Onodera - RM533779
- Soraya Haddad - RM554032
