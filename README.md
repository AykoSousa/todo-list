# Aplicação Todo-List em Django

Este é um exemplo de aplicação de lista de tarefas (Todo-List) desenvolvida em Django. A aplicação permite que os usuários criem, visualizem, atualizem e excluam tarefas em uma interface amigável e responsiva. Além disso, a biblioteca Crispy Forms é utilizada para aprimorar o estilo dos formulários.

## Pré-requisitos

- [Python]()
- Pip
- Django

Para instalar o django execute o seguinte comando:
```bash
pip install django
```


## Instalação

Siga as etapas abaixo para instalar e executar a aplicação em sua máquina:

1. Clone o repositório:

```bash
git clone https://github.com/AykoSousa/todo-list.git
```


2. Navegue até o diretório do projeto:

```bash
cd todo-list
```


3. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```


4. Ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\activate
```

- No macOS e no Linux:

```bash
source venv/bin/activate
```


5. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```


6. Aplique as migrações:

```bash
python manage.py migrate
```


7. Execute a aplicação:

```bash
python manage.py runserver
```


A aplicação estará disponível em `http://localhost:8000/`.

## Uso

- Acesse a interface da aplicação no seu navegador.
- Crie, visualize, atualize e exclua tarefas de acordo com suas necessidades.
- A biblioteca Crispy Forms é utilizada para melhorar a aparência dos formulários e tornar a experiência do usuário mais agradável.

## Contribuindo

Sinta-se à vontade para contribuir para este projeto.