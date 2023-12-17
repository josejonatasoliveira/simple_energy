**README.md**

# Simple Energy

## Sumário

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Rodar](#como-rodar)

## Requisitos

Certifique-se de ter o Python instalado com uma versão maior que 3.8. Você também precisará da biblioteca Scrapy. Você pode instalar os requisitos executando:

```bash
pip install -r requirements.txt
```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/josejonatasoliveira/simple_energy.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd simple_energy
   ```
3. Crie um ambiente virtual:
    ```bash
   python -m venv .env
   ```

    Ative o ambiente virtual

   ```bash
   .env\\Scripts\\activate.bat
   ```

4. Instale os requisitos:

   ```bash
   pip install -r requirements.txt
   ```

## Como Rodar

Execute o seguinte comando para rodar o projeto:

```bash
scrapy crawl file_data
```

Isso iniciará a execução do spider chamado `file_data` e salvará os dados coletados dentro do arquivo
database.db.