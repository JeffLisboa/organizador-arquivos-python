import logging

logging.basicConfig(
    filename='logs/organizacao.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def registrar_log(mensagem):
    logging.info(mensagem)