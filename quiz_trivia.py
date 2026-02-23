import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from pathlib import Path


class LoginSchermo:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        # File account
        self.file_account = Path("accounts.txt")
        self._assicurati_file_account()

        # Font
        self.label_font = tkfont.Font(family="Helvetica", size=10)
        self.entry_font = tkfont.Font(family="Helvetica", size=12)

        # Container principale
        self.main_frame = tk.Frame(self.root, bg="#121212")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # --- IMMAGINE LOGO ---
        img = Image.open("./Immagini/logoTrasparente.png")
        img = img.resize((260, 170), Image.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(img)

        tk.Label(self.main_frame, image=self.logo_img, bg="#121212").pack(pady=(0, 40))

        # --- USERNAME ---
        tk.Label(
            self.main_frame,
            text="NOME UTENTE",
            fg="#888888",
            bg="#121212",
            font=self.label_font
        ).pack(anchor="w", padx=5)

        self.user_frame = tk.Frame(self.main_frame, bg="#1E1E1E")
        self.user_frame.pack(pady=(5, 20), ipady=8, ipadx=10)

        self.user_entry = tk.Entry(
            self.user_frame,
            bg="#1E1E1E",
            fg="white",
            insertbackground="white",
            borderwidth=0,
            font=self.entry_font,
            width=25
        )
        self.user_entry.pack(padx=10)
        self.user_entry.focus_set()

        # --- PASSWORD ---
        tk.Label(
            self.main_frame,
            text="PASSWORD",
            fg="#888888",
            bg="#121212",
            font=self.label_font
        ).pack(anchor="w", padx=5)

        self.pass_frame = tk.Frame(self.main_frame, bg="#1E1E1E")
        self.pass_frame.pack(pady=(5, 30), ipady=8, ipadx=10)

        self.pass_entry = tk.Entry(
            self.pass_frame,
            bg="#1E1E1E",
            fg="white",
            insertbackground="white",
            borderwidth=0,
            font=self.entry_font,
            width=25,
            show="●"
        )
        self.pass_entry.pack(padx=10)

        # --- BOTTONE ---
        self.login_btn = tk.Button(
            self.main_frame,
            text="ACCEDI",
            bg="#4285F4",
            fg="white",
            font=("Helvetica", 12, "bold"),
            bd=0,
            cursor="hand2",
            width=20,
            height=2,
            command=self.verificaAccount
        )
        self.login_btn.pack(pady=20)

        # ENTER per login
        self.root.bind("<Return>", lambda e: self.verificaAccount())

        # Label errori (invece di messagebox)
        self.msg = tk.Label(self.main_frame, text="", fg="#ff6b6b", bg="#121212", font=self.label_font)
        self.msg.pack(pady=(5, 0))

    def _assicurati_file_account(self):
        """Crea accounts.txt se non esiste, con un account demo."""
        if not self.file_account.exists():
            self.file_account.write_text("admin:admin\n")  # account demo

    def _carica_account(self) -> dict:
        """
        Legge accounts.txt e ritorna un dict {username: password}
        Ignora righe vuote o malformate.
        """
        accounts = {}
        for line in self.file_account.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" not in line:
                continue
            user, pwd = line.split(":", 1)
            user = user.strip()
            pwd = pwd.strip()
            if user:
                accounts[user] = pwd
        return accounts

    def verificaAccount(self):
        username = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()

        if not username or not password:
            self.msg.config(text="Inserisci username e password")
            return

        accounts = self._carica_account()

        if username in accounts and accounts[username] == password:
            self.msg.config(text="")
            self.apriAccount(username)
        else:
            self.msg.config(text="Username o password errati")

    def apriAccount(self, username):
        """Simula accesso: apre una nuova finestra."""
        win = tk.Toplevel(self.root)
        win.title("Account")
        win.geometry("400x250")
        win.resizable(False, False)
        win.configure(bg="#121212")

        tk.Label(
            win,
            text=f"Benvenuto, {username}!",
            fg="white",
            bg="#121212",
            font=tkfont.Font(family="Helvetica", size=18, weight="bold")
        ).pack(pady=40)

        tk.Button(
            win,
            text="ESCI",
            bg="#333333",
            fg="white",
            bd=0,
            cursor="hand2",
            width=15,
            height=2,
            command=win.destroy
        ).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginSchermo(root)
    root.mainloop()