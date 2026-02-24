# # Verifica su File e JSON 

# ## Consegna
# Consegna un singolo file Python rinominato come `cognome.py` (es. `rossi.py`).
# Testa il codice eseguendolo in terminale con `python cognome.py`.

# ---

# ## Esercizio: Gestione Biblioteca

# Stai costruendo un sistema per gestire una piccola biblioteca.
# I dati di partenza sono da definire hardcoded nel `main()`:

# ```python
# libri = [
#     {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
#     {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
#     {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
#     {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
# ]
# ```

# ---

# ### Punto A – Salvataggio e caricamento JSON 

# 1. Definisci `salva_biblioteca(libri: list[dict], nome_file: str) -> None`:
#    Salva la lista in formato JSON con indentazione. Stampa un messaggio di conferma.

# 2. Definisci `carica_biblioteca(nome_file: str) -> list[dict]`:
#    Carica e restituisce la lista da JSON.
#    Se il file non esiste, stampa un messaggio di errore e restituisce `[]`.

# Nel `main()`:
# - Chiama `salva_biblioteca` per salvare su `"biblioteca.json"`.
# - Chiama `carica_biblioteca` e stampa quanti libri sono stati caricati.

# **Esempio di output:**
# ```
# File 'biblioteca.json' salvato con successo.
# Libri in archivio: 4
# ```


# ---

# ### Punto B – Filtro per genere

# 1. Definisci `filtra_per_genere(libri: list[dict], genere: str) -> list[dict]`:
#    Restituisce una nuova lista con solo i libri il cui campo `"genere"` corrisponde a quello passato.

# Nel `main()`:
# - Usa i libri caricati nel Punto A.
# - Filtra per `"Fantascienza"` e stampa quanti ne hai trovati e i loro titoli.

# **Esempio di output:**
# ```
# Libri di Fantascienza: 2
# - 1984
# - Dune
# ```

# ---

# ### Punto C – Statistiche 

# 1. Definisci `calcola_media_anno(libri: list[dict]) -> float`:
#    Restituisce la media degli anni di pubblicazione come `float`.
#    Se la lista è vuota, restituisce `0.0`.

# 2. Definisci `trova_libro_piu_recente(libri: list[dict]) -> dict | None`:
#    Restituisce il dizionario del libro con l'anno più alto.
#    Se la lista è vuota, restituisce `None`.

# Nel `main()`:
# - Chiama entrambe le funzioni sui libri caricati e stampa i risultati.

# **Esempio di output:**
# ```
# Media anno di pubblicazione: 1963.5
# Libro più recente: Harry Potter (1997)
# ```

# ---

# ### Punto D – Conta libri per genere

# 1. Definisci `conta_per_genere(libri: list[dict]) -> dict[str, int]`:
#    Restituisce un dizionario dove le chiavi sono i generi e i valori sono il numero di libri per genere.

# Nel `main()`:
# - Chiama la funzione sui libri caricati.
# - Stampa il risultato ordinato per genere (alfabetico).

# **Esempio di output:**
# ```
# Libri per genere:
# Fantasy: 1
# Fantascienza: 2
# Romanzo: 1
# ```

# ---

# ### Punto E – Bonus: Modifica anno di un libro 

# Definisci `modifica_anno_libro(libri: list[dict], titolo: str, nuovo_anno: int) -> tuple[bool, str, list[dict]]`:
# - Trova il libro con quel titolo (ricerca esatta) e aggiorna l'anno.
# - Restituisce una tupla `(success, messaggio, libri_modificati)` dove `success` è `True` se il libro è stato trovato e modificato, altrimenti `False`. La lista modificata è sempre restituita.

# Nel `main()`, dopo il Punto D:
# - Chiedi all'utente un titolo e un nuovo anno.
# - Chiama `modifica_anno_libro` e stampa il messaggio.
# - Se la modifica è riuscita, richiama `salva_biblioteca` per salvare le modifiche su `"biblioteca.json"`.

# **Esempio di interazione:**
# ```
# Inserisci titolo da modificare: 1984
# Inserisci nuovo anno: 1950
# Libro '1984' aggiornato con anno 1950. Totale libri: 4
# ```

# **Se il libro non esiste:**
# ```
# Inserisci titolo da modificare: Titanic
# Libro 'Titanic' non trovato.

import json

def salva_biblioteca(libri: list[dict], nome_file: str) -> None: 
   try:
        with open(nome_file, "w", encoding = "utf-8") as f:
            json.dump(libri, f, indent=4)
        print(f"File '{nome_file}' salvato con successo.")
    except IOError as e:
        print(f"errore durante la scrittura del file: {e}")

def carica_biblioteca(nome_file: str) -> list[dict]:  
    try:
        with open(nome_file, "r") as f:
            libri = json.load(f)
            return libri
    except FileNotFoundError:
        print(f"Errore: Il file '{nome_file}' non esiste.")
        return []



def salva_biblioteca(nome_file: str) -> list[dict]:   
    Libro: []
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(libri, file, indent=4)
        print(f"File '{nome_file}' salvato con successo.")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def main()-> None: 
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
        {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]
    libri_salvati = salva_biblioteca(libri, "biblioteca.json")
    libri_caricati = carica_biblioteca("biblioteca.json")
    print(f"Libri in archivio: {len(libri_caricati)}")


# b

def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]: 
    filtrati = []
    for libri in genere:
        if libro["genere"] == genere:
            filtrati.append(libri)
    return filtrati

def main(): 
     libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
        {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]

    salva_inventario(libri, nome_file)
    prodotti_caricati = carica_inventario(nome_file)
    if prodotti_caricati:
        fantascienza = filtra_per_categoria(prodotti_caricati, "Fantascienza")
        print(f"Prodotti fantascienza: {fantascienza}")
   

#c

def calcola_media_anno(libri: list[dict]) -> float:
    libri = [
        {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
        {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
        {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
        {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]
    somma_anni = 0.0
    for libro in libri:
        somma_anni += ["media"]
        media_anni = somma_anni / len(libri)
        print(f"Media libri : {media_anni:.2f}")
        print()
        if libri == "":
            return 0.0
    
def trova_libro_piu_recente(libri: list[dict]) -> dict | None:
    recente = []
    for libro in libri:
        if libro["anno"] not in recente:
            recente.append(libro["anno"])
            return recente
          
def main():
    media_anni = calcola_media_anno(libri: list[dict])
    recentita_libro = trova_libro_piu_recente(libri: list[dict])
    print(f"la media è {media_anni}")
    print(f"la recentita del libro è {recentita_libro}")



# ### Punto D – Conta libri per genere

# 1. Definisci `conta_per_genere(libri: list[dict]) -> dict[str, int]`:
#    Restituisce un dizionario dove le chiavi sono i generi e i valori sono il numero di libri per genere.
def conta_per_genere(libri: list[dict]) -> dict[str, int]:
    conteggio = {}
    try:
        with open(libri, "r", encoding="utf-8") as file:
            contenuto = file.read().lower()
            contenuto = contenuto.replace(".", "").replace(",", "")
            parole = contenuto.split()
            for genere in libri:
                if genere in libri:
                    libri[genere] += 1
                else:
                    libri[genere] = 1
    except FileNotFoundError:
        print(f"Errore: il file '{libri}' non è stato trovato.")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")
    return conteggio

def main():
    

# Nel `main()`:
# - Chiama la funzione sui libri caricati.
# - Stampa il risultato ordinato per genere (alfabetico).

# **Esempio di output:**
# ```
# Libri per genere:
# Fantasy: 1
# Fantascienza: 2
# Romanzo: 1
# ```



def modifica_anno_libromodifica_anno_libro(libri: list[dict], titolo: str, nuovo_anno: int) -> tuple[bool, str, list[dict]]:

# ### Punto E – Bonus: Modifica anno di un libro 

# Definisci `modifica_anno_libro(libri: list[dict], titolo: str, nuovo_anno: int) -> tuple[bool, str, list[dict]]`:
# - Trova il libro con quel titolo (ricerca esatta) e aggiorna l'anno.
# - Restituisce una tupla `(success, messaggio, libri_modificati)` dove `success` è `True` se il libro è stato trovato e modificato, altrimenti `False`. La lista modificata è sempre restituita.

# Nel `main()`, dopo il Punto D:
# - Chiedi all'utente un titolo e un nuovo anno.
# - Chiama `modifica_anno_libro` e stampa il messaggio.
# - Se la modifica è riuscita, richiama `salva_biblioteca` per salvare le modifiche su `"biblioteca.json"`.

# **Esempio di interazione:**
# ```
# Inserisci titolo da modificare: 1984
# Inserisci nuovo anno: 1950
# Libro '1984' aggiornato con anno 1950. Totale libri: 4
# ```

# **Se il libro non esiste:**
# ```
# Inserisci titolo da modificare: Titanic
# Libro 'Titanic' non trovato.

