import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk

class SchermataQuiz:
    def __init__(self, root, categoria, difficolta):
        self.root = root
        self.root.title(f"Quiz - {categoria}")
        self.punteggio = 0
        self.tempo_rimasto = 15  # Secondi
        
        self.main_frame = tk.Frame(self.root, bg="#121212")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9)

        # --- HEADER (Punteggio) ---
        self.score_label = tk.Label(
            self.main_frame, text=f"PUNTEGGIO: {self.punteggio}",
            fg="#4285F4", bg="#121212", font=("Helvetica", 12, "bold")
        )
        self.score_label.pack(pady=(0, 10))

        # --- TIMER BAR ---
        self.canvas_timer = tk.Canvas(self.main_frame, width=300, height=8, bg="#1E1E1E", highlightthickness=0)
        self.canvas_timer.pack(pady=10)
        self.timer_bar = self.canvas_timer.create_rectangle(0, 0, 300, 8, fill="#4285F4", width=0)

        # --- DOMANDA ---
        self.domanda_label = tk.Label(
            self.main_frame, 
            text="Qual è la capitale della Francia?", 
            fg="white", bg="#121212", font=("Helvetica", 14, "bold"),
            wraplength=350, justify="center"
        )
        self.domanda_label.pack(pady=30)

        # --- CONTENITORE RISPOSTE (Griglia 2x2) ---
        self.grid_frame = tk.Frame(self.main_frame, bg="#121212")
        self.grid_frame.pack(fill="x", pady=20)

        self.bottoni_risposte = []
        opzioni_demo = ["Berlino", "Madrid", "Parigi", "Roma"]
        
        for i in range(4):
            btn = tk.Button(
                self.grid_frame,
                text=opzioni_demo[i],
                bg="#1E1E1E", fg="white", font=("Helvetica", 11),
                bd=0, cursor="hand2", height=3, width=15,
                activebackground="#333333", activeforeground="white",
                command=lambda x=opzioni_demo[i]: self.controlla_risposta(x)
            )
            row = i // 2
            col = i % 2
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.bottoni_risposte.append(btn)

        self.grid_frame.columnconfigure(0, weight=1)
        self.grid_frame.columnconfigure(1, weight=1)

        # Avvia il countdown
        self.aggiorna_timer()

    def aggiorna_timer(self):
        if self.tempo_rimasto > 0:
            self.tempo_rimasto -= 0.1
            nuova_larghezza = (self.tempo_rimasto / 15) * 300
            self.canvas_timer.coords(self.timer_bar, 0, 0, nueva_larghezza, 8)
            
            if self.tempo_rimasto < 5:
                self.canvas_timer.itemconfig(self.timer_bar, fill="#ff6b6b")
                
            self.root.after(100, self.aggiorna_timer)
        else:
            self.fine_tempo()

    def controlla_risposta(self, scelta):
        print(f"Hai scelto: {scelta}")

    def fine_tempo(self):
        self.domanda_label.config(text="TEMPO SCADUTO!", fg="#ff6b6b")
        for b in self.bottoni_risposte:
            b.config(state="disabled")

class LoginSchermo:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.main_frame = tk.Frame(self.root, bg="#121212")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.label_font = tkfont.Font(family="Helvetica", size=10)
        self.entry_font = tkfont.Font(family="Helvetica", size=12)

        try:
            img = Image.open("./Immagini/logoTrasparente.png")
            img = img.resize((260, 170), Image.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(self.main_frame, image=self.logo_img, bg="#121212").pack(pady=(0, 40))
        except:
            tk.Label(self.main_frame, text="LOGO", fg="white", bg="#121212", font=("Helvetica", 24)).pack(pady=(0, 40))

        tk.Label(self.main_frame, text="NOME UTENTE", fg="#888888", bg="#121212", font=self.label_font).pack(anchor="w", padx=5)
        self.user_entry = self._crea_input_box()
        
        tk.Label(self.main_frame, text="PASSWORD", fg="#888888", bg="#121212", font=self.label_font).pack(anchor="w", padx=5)
        self.pass_entry = self._crea_input_box(password=True)

        tk.Button(self.main_frame, text="ACCEDI", bg="#4285F4", fg="white", font=("Helvetica", 12, "bold"),
                  bd=0, cursor="hand2", width=20, height=2, command=self.esegui_login).pack(pady=20)

    def _crea_input_box(self, password=False):
        f = tk.Frame(self.main_frame, bg="#1E1E1E")
        f.pack(pady=(5, 20), ipady=8, ipadx=10)
        e = tk.Entry(f, bg="#1E1E1E", fg="white", insertbackground="white", borderwidth=0, 
                     font=self.entry_font, width=25, show="●" if password else "")
        e.pack(padx=10)
        return e

    def esegui_login(self):
        self.main_frame.destroy() 
        self.on_login_success()

class SelezioneQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Configurazione Quiz")
        
        self.main_frame = tk.Frame(self.root, bg="#121212")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.dati_domande = ["Geografia", "Storia", "Scienze", "Informatica", "Letteratura", "Sport", "Cinema", "Musica", "Arte", "Cultura Generale"]
        self.categoria_scelta = tk.StringVar(value="Casuale")
        self.difficolta_scelta = tk.StringVar(value="facile")

        tk.Label(self.main_frame, text="IMPOSTA IL TUO QUIZ", fg="white", bg="#121212", font=("Helvetica", 16, "bold")).pack(pady=(0, 40))

        self._crea_label("SCEGLI ARGOMENTO")
        cat_menu = tk.OptionMenu(self.main_frame, self.categoria_scelta, "Casuale", *sorted(self.dati_domande))
        self._stile_menu(cat_menu)

        self._crea_label("LIVELLO DIFFICOLTÀ")
        diff_menu = tk.OptionMenu(self.main_frame, self.difficolta_scelta, "facile", "medio", "difficile")
        self._stile_menu(diff_menu)

        tk.Button(self.main_frame, text="INIZIA QUIZ", bg="#4285F4", fg="white", font=("Helvetica", 12, "bold"),
                  bd=0, cursor="hand2", width=20, height=2, command=self.avvia_quiz).pack(pady=40)

    def _crea_label(self, testo):
        tk.Label(self.main_frame, text=testo, fg="#888888", bg="#121212", font=("Helvetica", 10)).pack(anchor="w", padx=5)

    def _stile_menu(self, menu):
        menu.configure(bg="#1E1E1E", fg="white", highlightthickness=0, bd=0, activebackground="#333333", indicatoron=0)
        menu["menu"].configure(bg="#1E1E1E", fg="white", bd=0)
        menu.pack(pady=(5, 25), fill="x", ipady=5)

    def avvia_quiz(self):
        # --- MODIFICA QUI PER FARLO FUNZIONARE ---
        cat = self.categoria_scelta.get()
        diff = self.difficolta_scelta.get()
        self.main_frame.destroy()  # Distrugge la selezione
        SchermataQuiz(self.root, cat, diff)  # Crea la schermata del quiz vera e propria

# --- LOGICA DI AVVIO ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("400x600")
    root.configure(bg="#121212")
    root.resizable(False, False)

    # Inizia con il Login. Al successo carica la Selezione.
    app_login = LoginSchermo(root, on_login_success=lambda: SelezioneQuiz(root))
    
    root.mainloop()