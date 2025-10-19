# 🧾 Sistema de Gerenciamento de Estoque - Guia de Implementação

## Visão Geral

Este documento descreve a implementação completa de um sistema de gerenciamento de estoque em Python com banco de dados SQL (SQLite).

## Arquitetura do Sistema

### 1. Camada de Dados (database.py)
- Gerencia a conexão com o banco de dados SQLite
- Cria e inicializa as tabelas necessárias
- Fornece métodos para conectar e fechar o banco de dados

**Tabelas:**
- `produtos`: Armazena informações dos produtos
- `movimentacoes`: Registra todas as entradas e saídas de estoque

### 2. Camada de Negócio (produto.py)
Implementa todas as regras de negócio e operações:

**CRUD de Produtos:**
- `cadastrar()`: Registra novos produtos com validação de código único
- `editar()`: Atualiza informações de produtos existentes
- `excluir()`: Remove produtos do sistema (com exclusão em cascata)
- `consultar_por_id()`: Busca produto por ID
- `consultar_por_codigo()`: Busca produto por código único
- `consultar_por_nome()`: Busca produtos por nome (parcial)
- `consultar_por_categoria()`: Busca produtos por categoria
- `listar_todos()`: Lista todos os produtos

**Controle de Estoque:**
- `entrada_estoque()`: Registra entrada de produtos
- `saida_estoque()`: Registra saída de produtos (com validação de estoque)
- `historico_movimentacoes()`: Exibe histórico completo de movimentações

### 3. Camada de Apresentação (main.py)
Interface interativa com o usuário:
- Menu principal com 8 opções + sair
- Formulários de entrada de dados
- Exibição formatada de resultados
- Mensagens de confirmação e erro
- Validação de entrada de dados

## Funcionalidades Implementadas

### ✅ 1. Cadastrar Produtos
- Código único obrigatório
- Nome, categoria, descrição
- Quantidade inicial e preço
- Registro automático de estoque inicial

### ✅ 2. Editar Produtos
- Atualização seletiva de campos
- Preserva campos não modificados
- Atualiza timestamp automaticamente

### ✅ 3. Excluir Produtos
- Confirmação antes da exclusão
- Exclusão em cascata de movimentações
- Mensagens informativas

### ✅ 4. Consultar Produtos
- Por código único
- Por nome (busca parcial)
- Por categoria
- Exibição detalhada

### ✅ 5. Entrada de Estoque
- Validação de quantidade
- Atualização automática do estoque
- Registro na tabela de movimentações
- Observações opcionais

### ✅ 6. Saída de Estoque
- Validação de estoque disponível
- Prevenção de estoque negativo
- Registro na tabela de movimentações
- Observações opcionais

### ✅ 7. Histórico de Movimentações
- Visualização completa por produto
- Tipo (ENTRADA/SAIDA)
- Quantidade e observações
- Data e hora de cada movimentação

### ✅ 8. Listar Todos os Produtos
- Visualização em formato tabular
- Informações resumidas
- Ordenação por nome

## Validações e Segurança

1. **Integridade de Dados:**
   - Códigos únicos de produtos
   - Chaves estrangeiras para movimentações
   - Timestamps automáticos

2. **Validações de Negócio:**
   - Quantidade deve ser maior que zero
   - Estoque não pode ficar negativo
   - Produto deve existir para operações

3. **Tratamento de Erros:**
   - Try-catch em todas as operações
   - Mensagens amigáveis ao usuário
   - Rollback automático em caso de erro

4. **Consistência:**
   - Transações atômicas
   - Histórico completo de movimentações
   - Atualização automática de timestamps

## Testes

O sistema inclui uma suíte completa de testes (`test_sistema.py`) que verifica:

1. ✅ Inicialização do banco de dados
2. ✅ Operações CRUD de produtos
3. ✅ Movimentações de estoque
4. ✅ Funcionalidades de busca

Todos os testes passam com sucesso (4/4).

## Demonstração

O arquivo `demo.py` contém um script de demonstração completo que:
- Cadastra produtos de exemplo
- Demonstra todas as funcionalidades
- Exibe resultados formatados
- Remove o banco de teste ao final

## Como Usar

### Instalação
```bash
git clone https://github.com/ThiagoDalamaria/Gestor-.git
cd Gestor-
python main.py
```

### Requisitos
- Python 3.6+
- SQLite3 (incluído no Python)

### Primeiro Uso
1. Execute `python main.py`
2. O banco de dados será criado automaticamente
3. Use o menu interativo para gerenciar o estoque

## Estrutura de Arquivos

```
Gestor-/
├── database.py          # Gerenciamento do banco de dados
├── produto.py           # Lógica de negócios
├── main.py              # Interface do usuário
├── test_sistema.py      # Testes automatizados
├── demo.py              # Script de demonstração
├── requirements.txt     # Dependências
├── README.md            # Documentação principal
├── .gitignore          # Arquivos ignorados pelo Git
└── estoque.db          # Banco de dados (criado em runtime)
```

## Tecnologias

- **Python 3**: Linguagem principal
- **SQLite3**: Banco de dados embutido
- **SQL**: Consultas e operações no banco

## Próximas Melhorias Possíveis

1. Interface gráfica (GUI) com Tkinter ou PyQt
2. Relatórios em PDF
3. Gráficos de estoque
4. Backup automático do banco
5. Autenticação de usuários
6. API REST para integração
7. Alertas de estoque baixo
8. Suporte a múltiplos depósitos

## Conclusão

O sistema está completamente funcional e atende todos os requisitos especificados:
- ✅ Cadastro de produtos
- ✅ Edição de produtos
- ✅ Exclusão de produtos
- ✅ Consulta por nome, categoria e código
- ✅ Controle de entradas e saídas
- ✅ Histórico de movimentações

O código é modular, bem documentado e testado, facilitando manutenção e expansão futura.
