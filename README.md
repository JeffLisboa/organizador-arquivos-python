# Organizador Automático de Arquivos

Projeto desenvolvido em Python para automatizar a organização de arquivos em diretórios.

O sistema identifica automaticamente extensões de arquivos e os move para pastas categorizadas, facilitando a organização de ambientes como Downloads, Documentos e Área de Trabalho.

---

# Funcionalidades

* Organização automática de arquivos por extensão
* Organização automática por ano e mês
* Estrutura hierárquica automática
* Criação automática de pastas
* Sistema de logs
* Modo preview
* Prevenção de sobrescrita de arquivos
* Identificação automática de categorias:

  * Imagens
  * Documentos
  * Planilhas
  * Vídeos
  * Áudios

---

# Estrutura Automática Criada

Exemplo da organização gerada pelo sistema:

```bash
Downloads/
│
├── Imagens/
│   ├── 2025/
│   │   ├── Julho/
│   │   ├── Agosto/
│
├── Documentos/
│   ├── 2024/
│   │   ├── Dezembro/
│
├── Videos/
│   ├── 2025/
│   │   ├── Junho/
```

---

# Tecnologias Utilizadas

* Python
* os
* shutil
* logging
* datetime

---

# Estrutura do Projeto

```bash
organizador-arquivos-python/
│
├── logs/
│   └── organizacao.log
│
├── logger.py
├── main.py
├── README.md
```

---

# Como Executar

Clone o repositório:

```bash
git clone https://github.com/JeffLisboa/organizador-arquivos-python.git
```

Acesse a pasta do projeto:

```bash
cd organizador-arquivos-python
```

Execute o projeto:

```bash
python main.py
```

---

# Como Funciona

O sistema:

1. Lê todos os arquivos da pasta definida
2. Identifica a extensão do arquivo
3. Descobre a categoria correspondente
4. Obtém a data de modificação do arquivo
5. Cria automaticamente:

```bash
Categoria/Ano/Mês
```

6. Move o arquivo para a pasta correta
7. Registra tudo no arquivo de log

---

# Sistema de Logs

Todas as movimentações são registradas automaticamente em:

```bash
logs/organizacao.log
```

Exemplo:

```bash
2025-07-10 14:32:15 - foto.jpg movido para Imagens/2025/Julho
```

---

# Preview Mode

O sistema possui modo de visualização.

Quando ativado:

```python
preview = True
```

Os arquivos NÃO serão movidos.

O sistema apenas exibirá:

```bash
[PREVIEW] foto.jpg -> Imagens/2025/Julho
```

---

# Objetivo do Projeto

Este projeto foi criado com foco em:

* automação de tarefas
* manipulação de arquivos
* aprendizado de Python
* desenvolvimento de lógica de programação
* organização de diretórios
* modularização
* criação de softwares utilitários

---

# Próximas Melhorias (V4)

* Organização por tamanho
* Filtros personalizados
* Interface gráfica
* Identificação de arquivos duplicados
* Monitoramento automático de pastas
* Configuração externa via config.py
* Geração de executável (.exe)

---

# Autor

Projeto desenvolvido por Jeff Lisboa.
