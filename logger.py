# Importa o módulo logging da biblioteca padrão do Python
# Esse módulo é usado para criar registros (logs) de eventos do sistema
import logging


# Configura o sistema de logs
logging.basicConfig(

    # Define o arquivo onde os logs serão salvos
    # O arquivo será criado dentro da pasta "logs"
    filename='logs/organizacao.log',

    # Define o nível mínimo de mensagens que serão registradas
    # INFO significa que mensagens informativas e acima disso serão salvas
    level=logging.INFO,

    # Define o formato da mensagem salva no log
    # %(asctime)s = data e hora do evento
    # %(message)s = texto da mensagem enviada
    format='%(asctime)s - %(message)s'
)


# Cria uma função chamada registrar_log
# Essa função recebe uma mensagem como parâmetro
def registrar_log(mensagem):

    # Salva a mensagem no arquivo de log usando o nível INFO
    logging.info(mensagem)