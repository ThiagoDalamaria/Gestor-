# 🧾 Sistema de Gerenciamento de Estoque

Sistema completo de controle de estoque desenvolvido em Python com banco de dados SQL. Permite o cadastro, atualização, exclusão e consulta de produtos, além do controle de entradas e saídas do estoque.

## ✨ Funcionalidades Principais

- **Cadastrar Produtos**: Registre novos produtos com código único, nome, categoria, descrição, quantidade inicial e preço
- **Editar Produtos**: Atualize informações de produtos existentes (nome, categoria, descrição, preço)
- **Excluir Produtos**: Remova produtos do sistema com confirmação de segurança
- **Consultar Produtos**: Busque produtos por:
  - Código único
  - Nome (busca parcial)
  - Categoria
- **Entrada de Estoque**: Registre adições ao estoque com histórico
- **Saída de Estoque**: Registre retiradas com validação de estoque disponível
- **Histórico de Movimentações**: Visualize todas as entradas e saídas de cada produto
- **Listar Produtos**: Veja todos os produtos cadastrados

## 🚀 Como Usar

### Requisitos

- Python 3.6 ou superior
- SQLite3 (incluído na biblioteca padrão do Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ThiagoDalamaria/Gestor-.git
cd Gestor-
```

2. Execute o sistema:
```bash
python main.py
```

### Uso do Sistema

Ao executar o programa, você verá um menu interativo com as seguintes opções:

```
🧾 SISTEMA DE GERENCIAMENTO DE ESTOQUE

[1] Cadastrar Produto
[2] Editar Produto
[3] Excluir Produto
[4] Consultar Produtos
[5] Entrada de Estoque
[6] Saída de Estoque
[7] Histórico de Movimentações
[8] Listar Todos os Produtos
[0] Sair
```

#### Exemplos de Uso

**Cadastrar um Produto:**
1. Selecione opção `1`
2. Informe o código do produto (único)
3. Informe nome, categoria, descrição, quantidade inicial e preço
4. O sistema confirmará o cadastro

**Consultar Produtos:**
1. Selecione opção `4`
2. Escolha o tipo de busca (código, nome ou categoria)
3. Informe o critério de busca
4. Visualize os resultados

**Movimentar Estoque:**
1. Para entrada: selecione opção `5`
2. Para saída: selecione opção `6`
3. Informe o ID do produto
4. Informe a quantidade
5. Adicione uma observação (opcional)

## 📊 Estrutura do Banco de Dados

### Tabela: produtos
- `id`: Identificador único (chave primária)
- `codigo`: Código do produto (único)
- `nome`: Nome do produto
- `categoria`: Categoria do produto
- `descricao`: Descrição detalhada
- `quantidade`: Quantidade em estoque
- `preco_unitario`: Preço unitário
- `data_cadastro`: Data de cadastro
- `data_atualizacao`: Data da última atualização

### Tabela: movimentacoes
- `id`: Identificador único (chave primária)
- `produto_id`: Referência ao produto
- `tipo`: Tipo de movimentação (ENTRADA/SAIDA)
- `quantidade`: Quantidade movimentada
- `observacao`: Observações sobre a movimentação
- `data_movimentacao`: Data da movimentação

## 📁 Estrutura do Projeto

```
Gestor-/
├── main.py           # Interface principal e menu do sistema
├── database.py       # Gerenciamento de conexão e inicialização do banco
├── produto.py        # Operações CRUD e controle de estoque
├── requirements.txt  # Dependências do projeto
├── README.md         # Documentação
└── estoque.db       # Banco de dados SQLite (criado automaticamente)
```

## 🔒 Validações e Segurança

- Códigos de produtos únicos (não permite duplicação)
- Validação de estoque antes de saídas
- Confirmação antes de excluir produtos
- Tratamento de erros e mensagens informativas
- Histórico completo de todas as movimentações

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal
- **SQLite3**: Banco de dados relacional embutido
- **SQL**: Para gerenciamento e consultas ao banco de dados

## 📝 Licença

Este projeto é de código aberto e está disponível para uso livre.
