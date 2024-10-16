# Documentação do código "Newtask v1.0"

Este é um sistema simples de gerenciamento de tarefas escrito em Python, que permite ao usuário criar, listar, ordenar, concluir e apagar tarefas. O sistema organiza as tarefas com base em suas prioridades e categorias, além de fornecer um menu interativo para facilitar a navegação.

---

## Estrutura de Dados
As tarefas são armazenadas em uma lista chamada `banco_de_dados`, onde cada tarefa é representada por um dicionário que contém os seguintes campos:
- **Nome**: Nome da tarefa
- **Descrição**: Detalhes sobre a tarefa
- **Categoria**: Categoria da tarefa (e.g., Pessoal, Trabalho)
- **Prioridade**: Nível de prioridade (1 para alta, 3 para baixa)
- **Status**: Indica se a tarefa foi concluída (True ou False)

---

## Funções

### `criar_tarefa()`
- **Descrição**: Permite ao usuário criar uma nova tarefa inserindo o nome, descrição, categoria e prioridade (1 a 3). Se a prioridade estiver fora desse intervalo, o sistema exibe uma mensagem de erro.
- **Saída**: Adiciona a nova tarefa ao `banco_de_dados` e exibe uma confirmação de sucesso.

### `listar_tarefa()`
- **Descrição**: Exibe todas as tarefas criadas em ordem de entrada. Mostra o nome, categoria, prioridade e status de conclusão (pendente ou concluída).
- **Saída**: Lista as tarefas formatadas.

### `prioridade_tarefa()`
- **Descrição**: Ordena as tarefas por prioridade e as exibe em ordem crescente (1 é a prioridade mais alta).
- **Saída**: Exibe as tarefas ordenadas por prioridade, juntamente com suas informações.

### `categoria_tarefa()`
- **Descrição**: Ordena as tarefas por categoria em ordem alfabética e as exibe.
- **Saída**: Exibe as tarefas ordenadas por categoria.

### `concluir_tarefa()`
- **Descrição**: Marca uma tarefa como concluída. O usuário seleciona a tarefa por seu número na lista.
- **Saída**: Atualiza o status da tarefa selecionada para "Concluída".

### `apagar_tarefa()`
- **Descrição**: Remove uma tarefa do banco de dados. O usuário seleciona a tarefa por seu número na lista.
- **Saída**: A tarefa é removida e o sistema confirma a remoção.

---

## Fluxo de Execução

O sistema apresenta um **menu de opções** para o usuário, que pode selecionar uma das seguintes funcionalidades:

1. **Criar tarefa**: O usuário pode inserir uma nova tarefa.
2. **Listar tarefa**: Mostra todas as tarefas criadas.
3. **Ordenar tarefas por Prioridade**: Exibe as tarefas organizadas pela prioridade (1 a 3).
4. **Ordenar tarefas por Categoria**: Mostra as tarefas ordenadas alfabeticamente por categoria.
5. **Marcar tarefa como Concluída**: O usuário seleciona uma tarefa para marcar como concluída.
6. **Apagar tarefa**: O usuário pode remover uma tarefa da lista.
0. **Sair**: Encerra o programa.

Caso o usuário insira uma opção inválida, o sistema exibe uma mensagem de erro.

---

## Exemplo de Uso

1. O programa começa com uma mensagem de boas-vindas.
2. O usuário seleciona a opção desejada através do menu.
3. Após realizar uma ação (como criar ou listar tarefas), o menu é exibido novamente.
4. O programa continua em loop até que o usuário escolha a opção "0" para sair.

---

Este código é uma base sólida para um sistema simples de gerenciamento de tarefas, que pode ser expandido conforme as necessidades do usuário.
