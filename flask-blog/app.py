# Importujemy niezbędne moduły z Flask
from flask import Flask, render_template, request, redirect, url_for
# Importujemy SQLAlchemy do obsługi bazy danych
from flask_sqlalchemy import SQLAlchemy
# Importujemy datetime do automatycznego zapisu daty utworzenia posta
from datetime import datetime
# Importujemy os, aby pobrać zmienne środowiskowe (np. adres bazy danych)
import os

# Tworzymy aplikację Flask
app = Flask(__name__)

# Pobieramy adres bazy danych z zmiennej środowiskowej lub domyślnie używamy SQLite
db_url = os.getenv("DATABASE_URL", "sqlite:///blog.db")
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# Wyłączamy ostrzeżenie dotyczące śledzenia zmian obiektów (optymalizacja)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicjalizujemy SQLAlchemy z aplikacją Flask
db = SQLAlchemy(app)

# Definiujemy model danych "Post" jako tabelę w bazie danych
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)         # unikalny identyfikator
    title = db.Column(db.String(100), nullable=False)    # tytuł posta (wymagany, max 100 znaków)
    content = db.Column(db.Text, nullable=False)         # treść posta (wymagana)
    created = db.Column(db.DateTime, default=datetime.utcnow)  # data utworzenia (domyślnie teraz)

# Strona główna – wyświetla listę wszystkich postów, posortowanych malejąco wg daty utworzenia
@app.route('/')
def index():
    posts = Post.query.order_by(Post.created.desc()).all()  # pobieramy wszystkie posty z bazy
    return render_template('index.html', posts=posts)       # przekazujemy je do szablonu HTML

# Widok pojedynczego posta – po ID
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)                   # szukamy posta po ID lub zwracamy 404
    return render_template('post.html', post=post)          # wyświetlamy go w szablonie

# Formularz dodawania nowego posta (GET – pokazuje formularz, POST – zapisuje dane)
@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # Pobieramy dane z formularza
        title = request.form['title']
        content = request.form['content']

        # Tworzymy nowy obiekt Post i zapisujemy go do bazy danych
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        # Po zapisaniu przekierowujemy na stronę główną
        return redirect(url_for('index'))

    # Jeśli metoda to GET – wyświetlamy formularz
    return render_template('new.html')

# Uruchamiamy aplikację tylko jeśli plik jest uruchamiany bezpośrednio
if __name__ == '__main__':
    app.run()
