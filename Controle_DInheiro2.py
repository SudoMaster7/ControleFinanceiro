# Importar bibliotecas
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime


# Classe Do app
class MoneyManagerApp(ctk.CTk):
    # Função Principal
    def __init__(self):
        super().__init__()

        self.title("Gerenciamento de Gastos")
        self.geometry("630x450")

        # Arquivos para salvar dados
        self.transactions_file = "transactions.txt"
        self.balance_file = "balance.txt"
        self.totals_file = "totals.txt"
        self.calc_deposit_file = "total_deposito.txt"
        self.calc_withdraw_file = "total_saque.txt"

        # Dados armazenados
        self.balance = 0.0  #Saldo
        self.transactions = []  #Transições
        self.total_deposit = 0.0  #Total Deposito
        self.total_withdraw = 0.0  #Total Saque

        # Rastrear estado do checkbox
        self.show_remove_widgets = ctk.BooleanVar(value=False)

        # Carregar Dados
        self.load_balance()
        self.load_transactions()
        self.load_total_deposit()
        self.load_total_withdraw()
        self.setup_ui()

        self.toggle_remove_widgets()

    # Função de carregar e salvar os dados
    def load_balance(self):
        try:
            with open(self.balance_file, "r") as file:
                self.balance = float(file.read())
        except FileNotFoundError:
            pass

    def save_balance(self):
        with open(self.balance_file, "w") as file:
            file.write(str(self.balance))

    def load_transactions(self):
        try:
            with open(self.transactions_file, "r") as file:
                for line in file:
                    self.transactions.append(line.strip())
        except FileNotFoundError:
            pass

    def save_transactions(self):
        with open(self.transactions_file, "w") as file:
            for transaction in self.transactions:
                file.write(transaction + "\n")

    def load_total_deposit(self):
        try:
            with open(self.calc_deposit_file, "r") as file:
                self.total_deposit = float(file.read())
        except FileNotFoundError:
            pass

    def save_total_deposit(self):
        with open(self.calc_deposit_file, "w") as file:
            file.write(str(self.total_deposit))

    def load_total_withdraw(self):
        try:
            with open(self.calc_withdraw_file, "r") as file:
                self.total_withdraw = float(file.read())
        except FileNotFoundError:
            pass

    def save_total_withdraw(self):
        with open(self.calc_withdraw_file, "w") as file:
            file.write(str(self.total_withdraw))

    # Gerencia a Interface Grafica do app
    def setup_ui(self):

        ctk.set_default_color_theme("blue")

        # Labels
        ctk.CTkLabel(self, text="Saldo: R$").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.balance_label = ctk.CTkLabel(self, text=str(self.balance))
        self.balance_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(self, text="Valor: R$").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.amount_entry = ctk.CTkEntry(self)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self, text="Descrição:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.reason_entry = ctk.CTkEntry(self)
        self.reason_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        ctk.CTkLabel(self, text="Histórico:").grid(row=3, column=0, padx=5, pady=5, sticky="ne")
        self.transaction_text = ctk.CTkTextbox(self, height=100, width=300)
        self.transaction_text.grid(row=3, column=1, padx=5, pady=5, rowspan=3)

        ctk.CTkLabel(self, text="Total Saques: R$").grid(row=10, column=0, padx=5, pady=5, sticky="e")
        self.total_withdraw_label = ctk.CTkLabel(self, text=str(self.total_withdraw))
        self.total_withdraw_label.grid(row=10, column=1, padx=5, pady=5, sticky="w")

        ctk.CTkLabel(self, text="Total Depósitos: R$").grid(row=11, column=0, padx=5, pady=5, sticky="e")
        self.total_deposit_label = ctk.CTkLabel(self, text=str(self.total_deposit))
        self.total_deposit_label.grid(row=11, column=1, padx=5, pady=5, sticky="w")

        # Checkbox para mostra/ocultar remoção
        self.remove_checkbox = ctk.CTkCheckBox(self, text="Deseja apagar algum item?",
                                               variable=self.show_remove_widgets, command=self.toggle_remove_widgets)
        self.remove_checkbox.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        self.remove_index_label = ctk.CTkLabel(self, text="Remover Índice:")
        self.remove_index_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.remove_index_entry = ctk.CTkEntry(self)
        self.remove_index_entry.grid(row=7, column=1, padx=5, pady=5, sticky="we")

        self.remove_transaction_button = ctk.CTkButton(self, fg_color="purple", text="Remover Transação", command=self.remove_transaction)
        self.remove_transaction_button.grid(row=8, column=1, padx=5, pady=5)

        # Buttons
        self.deposit_button = ctk.CTkButton(self, fg_color="green", text="Depositar", command=self.deposit)
        self.deposit_button.grid(row=9, column=0, padx=5, pady=5)

        self.withdraw_button = ctk.CTkButton(self, fg_color="red", text="Sacar", command=self.withdraw)
        self.withdraw_button.grid(row=9, column=1, padx=5, pady=5)

        self.reset_balance_button = ctk.CTkButton(self, fg_color="purple", text="Resetar Saldo", command=self.reset_balance)
        self.reset_balance_button.grid(row=8, column=2, padx=5, pady=5)

        # Carrega as transações na caixa de texto
        self.update_transaction_text()

    # Função para alternar a visibilidade dos widgets de remoção de transação com base no estado do checkbox
    def toggle_remove_widgets(self):

        if self.show_remove_widgets.get():
            self.remove_index_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
            self.remove_index_entry.grid(row=7, column=1, padx=5, pady=5, sticky="we")
            self.remove_transaction_button.grid(row=8, column=1, padx=5, pady=5)
            self.reset_balance_button.grid(row=8, column=2, padx=5, pady=5)
        else:
            self.remove_index_label.grid_remove()
            self.remove_index_entry.grid_remove()
            self.remove_transaction_button.grid_remove()
            self.reset_balance_button.grid_remove()

    # Função para o DEPOSITO e armazena a transição no historico
    def deposit(self):
        amount = self.get_amount()
        reason = self.get_reason()
        if amount > 0:
            self.balance += amount
            self.total_deposit += amount
            self.update_balance()
            now = datetime.now()
            timestamp = now.strftime("%d/%m %H:%M")
            self.transactions.append(f"{timestamp} - Depositado R${amount} - {reason}")
            self.save_balance()
            self.save_transactions()
            self.save_total_deposit()
            self.update_transaction_text()
            self.clear_entry_fields()
            self.update_total_labels()

    # Função para o SAQUE e armazena a transição ao historico
    def withdraw(self):
        amount = self.get_amount()
        reason = self.get_reason()
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.total_withdraw += amount
            self.update_balance()
            now = datetime.now()
            timestamp = now.strftime("%d/%m %H:%M")
            self.transactions.append(f"{timestamp} - Sacado R${amount} - {reason}")
            self.save_balance()
            self.save_transactions()
            self.save_total_withdraw()
            self.update_transaction_text()
            self.clear_entry_fields()
            self.update_total_labels()

        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido")

    # Função para remover o item do Historico
    def remove_transaction(self):
        try:
            index = int(self.remove_index_entry.get())
            if 0 <= index < len(self.transactions):
                del self.transactions[index]
                self.save_transactions()
                self.save_total_deposit()
                self.save_total_withdraw()
                self.update_transaction_text()
                self.remove_index_entry.delete(0, ctk.END)
            else:
                messagebox.showerror("Erro", "Índice inválido")
        except ValueError:
            messagebox.showerror("Erro", "Índice inválido")

    # Função para resetar o Saldo da conta
    def reset_balance(self):
        self.balance = 0.0
        self.total_deposit = 0.0
        self.total_withdraw = 0.0
        self.update_balance()
        self.save_balance()
        self.save_total_deposit()
        self.save_total_withdraw()
        messagebox.showinfo("Saldo Resetado", "O saldo foi resetado para zero.")

    # Função de pegar o valor digitado
    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            return amount
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido")
            return 0.0

    # Recebe a discrição
    def get_reason(self):
        return self.reason_entry.get()

    # Atualiza o saldo
    def update_balance(self):
        self.balance_label.configure(text=str(self.balance))

    # Atualiza a Caixa de Descrição
    def update_transaction_text(self):
        self.transaction_text.delete(1.0, ctk.END)
        for i, transaction in enumerate(self.transactions):
            self.transaction_text.insert(ctk.END, f"{i}: {transaction}\n")

    # Limpar o campo de entrada
    def clear_entry_fields(self):
        self.amount_entry.delete(0, ctk.END)
        self.reason_entry.delete(0, ctk.END)

    # Total de gasto de ganhos
    def update_total_labels(self):
        self.total_withdraw_label.configure(text=str(self.total_withdraw))
        self.total_deposit_label.configure(text=str(self.total_deposit))


if __name__ == "__main__":
    app = MoneyManagerApp()
    app.mainloop()
