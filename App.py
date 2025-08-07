from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "gizli_anahtar_123"  # Güvenlik için

# Basit kullanıcı verisi (demo amaçlı)
users = {
    "user1": "password123",
    "muammer": "sifre456"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            return redirect(url_for('profile', username=username))
        else:
            flash('Kullanıcı adı veya şifre yanlış!', 'error')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/profile/<username>')
def profile(username):
    if username not in users:
        flash('Kullanıcı bulunamadı!', 'error')
        return redirect(url_for('login'))
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
