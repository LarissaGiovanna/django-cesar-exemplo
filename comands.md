### Aplicação Django comands
- `py -m venv .venv` -> criar um ambiente virtual (apenas uma vez na criação)
- `.venv\scripts\activate` -> ativar o ambiente virtual (toda vez que for inicializar o projeto)
- `pip install -r requirements.txt` -> instalar frameworks listados no arquivo requirements.txt
- `pip freeze` -> lista todos os componentes com as respectivas versoes que foram instalados
- `pip freeze > requirements.txt` -> retorna a saida desse comando (pip freeze) para escrever no arquivo requirements.txt
- `py -m django --version` -> retorna a versao do django
- `django-admin startproject project .` -> cria uma pasta chamada project que contem arquivos de configurações do projeto
- `py manage.py runserver` -> inicia o servidor web 
- `py manage.py startapp "nome_do_app"` -> cria uma pasta com os arquivos do arquivo do projeto/app