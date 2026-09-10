## Comandos principais:
- `py -m venv .venv` -> Criar um ambiente virtual (apenas uma vez na criação)
- `.venv\scripts\activate`(windows powershell) ou `source .venv/Scripts/activate`(git bash) -> Ativar o ambiente virtual (toda vez que for inicializar o projeto)
- `py manage.py migrate` -> Implementa/migra/atualiza os scripts do app 
- `py manage.py createsuperuser` -> Cria um novo super user/admin
- `py manage.py runserver` -> Inicia o servidor web 

### Outros comandos
- `pip install -r requirements.txt` -> Instalar frameworks listados no arquivo requirements.txt
- `pip freeze` -> Lista todos os componentes que foram instalados com as suas respectivas versões
- `pip freeze > requirements.txt` -> Retorna a saida desse comando (pip freeze) para escrever no arquivo requirements.txt (redirecionamento)
- `py -m django --version` -> Retorna a versão do django
- `django-admin startproject project .` -> Cria uma pasta chamada project que contem arquivos de configurações do projeto
- `py manage.py startapp "nome_do_app"` -> Cria uma pasta com os arquivos do arquivo do projeto/app
- `py manage.py makemigrations forum` -> Cria scripts/models para a base do banco de dados
- `py manage.py sqlmigrate forum 0001` -> Mostra os comandos sql da tabela que sera criada para esse banco de dados
- `py manage.py shell` -> Abre um shell/terminal do django
- `py manage.py collectstatic` -> Busca e acessa os arquivos css (estaticos) quando estão em ambiente de produção

#### Exemplo forum perguntas comandos no shell:
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

