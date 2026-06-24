preview = True

from logger import registrar_log
import os
import shutil

# Pasta que será organizada
pasta_alvo = r"C:\Users\jeffe\Downloads"

# Categorias
categorias = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv"]
}

# Lista arquivos
arquivos = os.listdir(pasta_alvo)

# Percorre arquivos
for arquivo in arquivos:

    caminho_arquivo = os.path.join(pasta_alvo, arquivo)

    # Verifica se é arquivo
    if os.path.isfile(caminho_arquivo):

        # Separar nome e extensão
        nome, extensao = os.path.splitext(arquivo)

        # Percorre categorias
        for categoria, extensoes in categorias.items():

            # Verifica extensão
            if extensao.lower() in extensoes:

                pasta_categoria = os.path.join(pasta_alvo, categoria)

                # Cria pasta se não existir
                os.makedirs(pasta_categoria, exist_ok=True)

                origem = caminho_arquivo
                destino = os.path.join(pasta_categoria, arquivo)

                # PREVIEW MODE
                if preview:

                    mensagem = f"[PREVIEW] {arquivo} seria movido para {categoria}"

                    print(mensagem)

                    registrar_log(mensagem)

                else:

                    shutil.move(origem, destino)

                    mensagem = f"{arquivo} movido para {categoria}"

                    print(mensagem)

                    registrar_log(mensagem)