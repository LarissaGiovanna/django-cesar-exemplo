#### Quando clonar este repositorio:
- `py -m venv .venv` -> criar um ambiente virtual (apenas uma vez na criação)
- `.venv\scripts\activate` -> ativar o ambiente virtual (toda vez que for inicializar o projeto)
- `py manage.py migrate` -> implementa/migra/atualiza os scripts do app 
- `py manage.py createsuperuser` -> cria um novo super user/admin

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
- `py manage.py migrate` -> implementa/migra/atualiza os scripts do app 
- `py manage.py makemigrations forum` -> cria scirpts/models para a base do banco de dados
- `py manage.py sqlmigrate forum 0001` -> mostra os comandos sql da tabela que sera criada para esse banco de dados
- `py manage.py shell` -> abre um shell/terminal do django
#### no shell:
- `forum forum.models import Pergunta, Resposta` ->importa as Perguntas e as respostas para a manipulação
- `forum django.utils import timezone` ->importa a biblioteca da data e hora
- `Pergunta.objects.all()` ->lista todas as perguntas
- `Pergunta.objects.all().values()` ->lista todas as perguntas com todos os detalhes
- `Pergunta.objects.filter(id=1)` ->lista todas as perguntas cujo o id seja 1
- `p = Pergunta(titulo = "titulo", detalhe="...", ...)` -> cria/define a pergunta
- `p.save()`-> salva a pergunta no banco de dados que foi criada
- `p.resposta_set.all()`-> mostra as respostas associadas a essa pergunta
- `a1 = Resposta(pergunta = p, texto="...", ...)` -> cria/define a resposta para a perguna 'p'
- `a1.save()` -> salva a resposta da pergunta
- `a1.pergunta` -> mostra a pergunta dessa resposta
- `a2 = p.resposta_set.create(texto="..", data_criacao = timezone.now())`-> cria uma resposta diretamente da pergunta selecionada
#### criacao admin
- `py manage.py createsuperuser` -> cria um novo super user/admin

