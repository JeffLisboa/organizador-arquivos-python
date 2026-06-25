# Define se o sistema irá apenas visualizar
# ou mover os arquivos de verdade. (True = apenas visualizar, False = mover)
preview = False

# Importa função de logs
from logger import registrar_log

# Biblioteca para trabalhar com arquivos e pastas
import os

# Biblioteca usada para mover arquivos
import shutil

# Importa datetime para trabalhar com datas
from datetime import datetime


# Pasta que será organizada
pasta_alvo = r"C:\Users\jeffe\Downloads"


# Categorias de arquivos
categorias = {

    "Imagens": [
        ".jpg", ".png", ".jpeg", ".gif", ".bmp",
        ".tiff", ".svg", ".webp", ".ico",
        ".heic", ".raw", ".psd", ".ai",
        ".eps", ".indd"
    ],

    "Documentos": [
        ".pdf", ".docx", ".txt", ".pptx",
        ".ppt", ".doc", ".odt", ".rtf",
        ".tex", ".md"
    ],

    "Planilhas": [
        ".xlsx", ".csv", ".xls", ".ods",
        ".tsv", ".numbers", ".xml",
        ".json", ".yaml", ".yml",
        ".ini", ".log"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm", ".mpeg",
        ".mpg", ".3gp", ".m4v", ".vob",
        ".ts", ".rmvb", ".asf", ".divx",
        ".xvid"
    ],

    "Audios": [
        ".mp3", ".wav", ".flac", ".aac",
        ".ogg", ".wma", ".m4a", ".aiff",
        ".alac", ".opus", ".amr", ".mid",
        ".midi", ".ra", ".pcm", ".dts",
        ".ac3", ".eac3", ".dts-hd",
        ".truehd", ".mp2", ".mp1", ".m4b"
    ]
}


# Lista com nomes dos meses
meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]


# Lista todos os arquivos da pasta
arquivos = os.listdir(pasta_alvo)


# Percorre cada arquivo encontrado
for arquivo in arquivos:

    # Monta caminho completo do arquivo
    caminho_arquivo = os.path.join(
        pasta_alvo,
        arquivo
    )

    # Ignora pastas
    if not os.path.isfile(caminho_arquivo):
        continue

    # Separa nome e extensão
    nome, extensao = os.path.splitext(arquivo)

    # Obtém data da última modificação
    timestamp = os.path.getmtime(caminho_arquivo)

    # Converte timestamp para data real
    data_modificacao = datetime.fromtimestamp(timestamp)

    # Obtém ano do arquivo
    ano = str(data_modificacao.year)

    # Obtém número do mês
    numero_mes = data_modificacao.month

    # Converte número em nome do mês
    nome_mes = meses[numero_mes - 1]

    # Percorre categorias
    for categoria, extensoes in categorias.items():

        # Verifica extensão
        if extensao.lower() in extensoes:

            # Cria estrutura:
            # Categoria/Ano/Mês
            pasta_categoria = os.path.join(
                pasta_alvo,
                categoria,
                ano,
                nome_mes
            )

            # Cria pastas automaticamente
            os.makedirs(
                pasta_categoria,
                exist_ok=True
            )

            # Caminho final do arquivo
            destino = os.path.join(
                pasta_categoria,
                arquivo
            )

            # Evita sobrescrever arquivos
            contador = 1

            while os.path.exists(destino):

                novo_nome = (
                    f"{nome}_{contador}{extensao}"
                )

                destino = os.path.join(
                    pasta_categoria,
                    novo_nome
                )

                contador += 1

            # Preview mode
            if preview:

                mensagem = (
                    f"[PREVIEW] "
                    f"{arquivo} -> "
                    f"{categoria}/{ano}/{nome_mes}"
                )

            else:

                # Move arquivo
                shutil.move(
                    caminho_arquivo,
                    destino
                )

                mensagem = (
                    f"{arquivo} movido para "
                    f"{categoria}/{ano}/{nome_mes}"
                )

            # Exibe mensagem
            print(mensagem)

            # Salva log
            registrar_log(mensagem)

            # Interrompe loop
            break