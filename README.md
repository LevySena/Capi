# Capi
Repositorio do Projeto Capi

# Como rodar localmente 
Baixe a ferramenta UV ela vai fazer a gestão de pacotes do projeto, você pode baixar usando esse comando no powershell em modo administrador: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Para outros maneiras de instalção acesse o [site oficial](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

Após a instalação da ferramenta e com o repositório já em seu computador, abra a pasta com o VS Code, abra um terminal no VS Code e faça os seguintes comandos (Os pacotes serão instalados ao fazer o primeiro comando):

- uv run manage.py makemigrations
- uv run manage.py migrate

Esses comandos garantem que o banco de dados contenha as tabelas necessárias, após isso você pode criar um super usuário ou usar o já existente (Recomendo criar um novo para teste)

- uv run manage.py createsuperuser (Informe o nome e a senha, os outros campos podem ficar em brancos)

Com o super usuário criado podemos iniciar o servidor com o seguinte comando:

- uv run manage.py runserver

Esse comando vai fornecer um link no terminal para o acesso local.

# Atenção

O super usuário serve principalmente para acessar a tela de admin que pode ser acessada colocando /admin depois do link fornecido pelo comando anterior, certas telas podem não funcionar pois dependem que o usuário tenha um cadastro associado, então para isso faça logout acessando o link /login/logout e realize um cadastro novo pela tela de cadastro, com isso as telas irão funcionar normalmente.