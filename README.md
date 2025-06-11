#  Flask Blog

Prosty blog stworzony przy użyciu **Flask** i **SQLite**. Pozwala na dodawanie i przeglądanie postów.

## Co zawiera

- Backend w Python (Flask)
- Baza danych SQLite (lokalnie)
- HTML + CSS (pastelowy styl, responsywny wygląd)
- System dodawania i wyświetlania postów
- Gotowe do wdrożenia na platformie Render

## Demo online

[Zobacz działającą aplikację](https://isi-blog-1.onrender.com/)

##  Zrzuty ekranu

###  Strona główna  
![screen-1](flask-blog/screen-1.png)

###  Dodawanie nowego posta  
![screen-2](flask-blog/screen-2.png)

##  Jak uruchomić lokalnie

1. Klonuj repozytorium:
   ```bash
   git clone https://github.com/twoj-uzytkownik/flask-blog.git
   cd flask-blog
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   
   
   
## Struktura
```
flask-blog/
├── app.py              # GŁÓWNY plik aplikacji Flask (uruchamia serwer)
├── templates/
│   ├── index.html      # Szablon strony głównej z listą postów
│   └── add.html        # Formularz dodawania nowego posta
├── static/
│   └── style.css       # Plik CSS ze stylami 
├── blog.db             # Plik bazy danych SQLite (tworzony automatycznie)
├── requirements.txt    # Lista zależności Pythona do zainstalowania
└── README.md           # Instrukcja projektu 
