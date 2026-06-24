import os #Manipulação de arquivos e diretórios
import shutil #Mover arquivos de um diretório para outro

#Pasta que será organizada. O 'r' evita erro com barras do Windows.
pasta_alvo = r"C:\Users\jeffe\Downloads"

#Quais extensões pertencem a quais pastas.
categorias = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Planilhas": [".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv"]
}
#Lista todos os arquivos na pasta alvo
arquivos = os.listdir(pasta_alvo)

#Loop para percorrer cada arquivo na pasta alvo
for arquivo in arquivos:
#Cria o caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_alvo, arquivo)
#Verifica se o caminho é um arquivo (não uma pasta)
    if os.path.isfile(caminho_arquivo):
#Separa o nome do arquivo da sua extensão
        nome, extensao = os.path.splitext(arquivo)
#Loop para percorrer cada categoria e suas extensões
        for categoria, extensoes in categorias.items():

#Se a extensão do arquivo estiver na lista de extensões da categoria, move o arquivo para a pasta correspondente
            
            if extensao.lower() in extensoes:
#Junta o caminho da pasta alvo com o nome da categoria para criar a pasta de destino
                pasta_categoria = os.path.join(pasta_alvo, categoria)
#Cria a pasta da categoria se ela não existir
                os.makedirs(pasta_categoria, exist_ok=True)
#Move o arquivo para a pasta da categoria
                origem = caminho_arquivo
                destino = os.path.join(pasta_categoria, arquivo)
#Move o arquivo para a pasta de destino
                shutil.move(origem, destino)
#Printa uma mensagem informando que o arquivo foi movido para a pasta da categoria
                print(f"{arquivo} movido para {categoria}")