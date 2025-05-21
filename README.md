MAP – Sistema de Validação de Atividades Acadêmicas

  

MAP é um sistema web desenvolvido em Django para facilitar o envio, o acompanhamento e a validação de relatórios de atividades acadêmicas (como estágios, monitorias e extensões). Alunos, professores e coordenadores podem interagir em um ambiente organizado e seguro, garantindo maior transparência e eficiência.

📚 Conteúdo

Funcionalidades

Arquitetura

Pré-requisitos

Instalação

Configuração

Estrutura de Pastas

Rotas e Endpoints

Como usar

Contribuição

Licença

✨ Funcionalidades

Home: Visão geral e acesso rápido às principais ações.

Listagem de Atividades: Painel com atividades em andamento do usuário.

Formulário de Nova Atividade: Solicitação de atividades de estágio, monitoria ou extensão.

Listagem de Relatórios: Visão geral de relatórios por tipo (estágio, monitoria, extensão).

Validação de Relatórios: Professores e coordenadores podem validar relatórios enviados.

🏛️ Arquitetura

Django (v5.2): Framework principal.

SQLite: Banco de dados padrão para desenvolvimento.

Templates: HTML + Bootstrap 5 para estilo responsivo e clean.

Formulários: ModelForm para criar e editar atividades.

Views: Genéricas e baseadas em função, simples e diretas.

🛠️ Pré-requisitos

Python 3.10+

Git

Virtualenv (opcional, mas recomendado)

⚙️ Instalação

Clone o repositório

git clone https://github.com/seu-usuario/MAP.git
cd MAP

Crie e ative um virtualenv

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows

Instale as dependências

pip install -r requirements.txt

Aplique as migrações

python manage.py migrate

Crie um superusuário

python manage.py createsuperuser

Execute o servidor

python manage.py runserver

Acesse http://127.0.0.1:8000/ no navegador.

🛠️ Configuração (opcional)

Se desejar configurar variáveis de ambiente:

Crie um arquivo .env na raiz:

DEBUG=True
SECRET_KEY=sua_chave_secreta

Instale python-dotenv e atualize settings.py para carregar o .env.

📂 Estrutura de Pastas
````
MAP/                    # raiz do repositório
├── academic_reports/   # settings do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── relatorios/         # app principal
│   ├── migrations/
│   ├── templates/
│   │   └── relatorios/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── atividades.html
│   │       ├── atividade_form.html
│   │       ├── relatorios.html
│   │       └── validacao.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── media/              # uploads de relatórios
├── venv/               # virtualenv local
├── .gitignore
├── manage.py
└── requirements.txt
````

🔗 Rotas e Endpoints

URL

View / Template

Nome da URL

/

home.html

relatorios:home

/atividades/

atividades.html

relatorios:atividades

/atividades/nova/

atividade_form.html

relatorios:atividade_nova

/relatorios/

relatorios.html

relatorios:relatorios

/relatorios/<id>/validar/

validacao.html

relatorios:validar_relatorio

🚀 Como usar

Home – Tela inicial com botão para criar novas atividades.

Atividades – Lista suas atividades; clique em “Detalhes” para ver mais (a implementar).

Nova Atividade – Preencha título, tipo, data de início e envie.

Relatórios – Visualize relatórios por categoria.

Validar Relatório – Clique em “Validar” para confirmar.

🤝 Contribuição

Fork este repositório.

Crie uma branch: git checkout -b feature/nome-da-feature.

Faça commits: git commit -m "feat: Descrição do que você fez".

Envie para sua branch: git push origin feature/nome-da-feature.

Abra um Pull Request.

Siga o Guia de Contribuição para mais detalhes.

📝 Licença

Este projeto está licenciado sob a MIT License.
