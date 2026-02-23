import datetime

def salva_punteggio(nome_giocatore, punteggio):
    adesso = datetime.datetime.now()
    data_e_ora = adesso.strftime("%d/%m/%Y %H:%M:%S")
    
    # Apre il file in modalità "a"
    # "append" aggiunge il testo alla fine senza cancellare i salvataggi vecchi.
    with open("punteggi_giocatori.csv", "a") as file:
        # Crea la riga separando i dati con una virgola e va a capo (\n)
        riga = nome_giocatore + "," + str(punteggio) + "," + data_e_ora + "\n"
        
        file.write(riga)



def mostra_classifica():

    tutti_i_punteggi = []

    try:
 
        with open("punteggi_giocatori.csv", "r") as file:
            righe = file.readlines()

            for riga in righe:
                dati = riga.strip().split(",")
                
                nome = dati[0]
                punteggio = int(dati[1]) 
                data_ora = dati[2]

                tutti_i_punteggi.append([nome, punteggio, data_ora])


        def prendi_punteggio(elemento):
            return elemento[1]

        tutti_i_punteggi.sort(key=prendi_punteggio, reverse=True)

        print("--- CLASSIFICA TOP 5 ---")
        
        # Prendiamo solo i primi 5 elementi della lista ordinata
        primi_5 = tutti_i_punteggi[:5]
        
       
        for i in range(len(primi_5)):
            giocatore = primi_5[i]
            nome_giocatore = giocatore[0]
            punti = giocatore[1]
            print(str(i + 1) + "° posto: " + nome_giocatore + " - " + str(punti) + " punti")

    except FileNotFoundError:

        print("Nessuna partita giocata finora. La classifica è vuota!")
