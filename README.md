
# MoneyManagerApp - Controle de Gastos

Este é um aplicativo de gerenciamento de gastos desenvolvido em Python, usando `customtkinter` para a interface gráfica. O objetivo é facilitar o acompanhamento de depósitos e saques, além de exibir um histórico das transações.

## Funcionalidades

- **Registro de Transações**: Adicione transações de depósito e saque.
- **Cálculo de Saldo**: Exibe o saldo atualizado conforme os registros.
- **Histórico de Transações**: Visualize todas as transações realizadas.
- **Interface Gráfica Interativa**: Desenvolvido com `customtkinter` para uma experiência de uso intuitiva.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **customtkinter**: Biblioteca para uma interface gráfica customizada.
- **datetime**: Para registrar a data e hora das transações.

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado. Em seguida, instale a biblioteca `customtkinter`:

```bash
pip install customtkinter
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/controle-de-gastos.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd controle-de-gastos
   ```

## Como Usar

1. Execute o aplicativo:
   ```bash
   python Controle_DInheiro2.py
   ```
2. Na interface, insira valores para depósitos e saques conforme necessário.
3. Visualize o saldo e o histórico de transações, atualizados automaticamente.

## Estrutura de Arquivos

- **`transactions.txt`**: Registro de todas as transações realizadas.
- **`balance.txt`**: Armazena o saldo atual.
- **`totals.txt`**: Guarda o total de depósitos e saques.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-nova-funcionalidade
   ```
3. Realize o commit das alterações:
   ```bash
   git commit -m 'Adicionar nova funcionalidade'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-nova-funcionalidade
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
