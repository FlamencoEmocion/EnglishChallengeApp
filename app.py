from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Mock leaderboard
leaderboard = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/study')
def study():
    return render_template('study.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/leaderboard', methods=['GET', 'POST'])
def show_leaderboard():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        score = int(request.form.get('score', 0))
        leaderboard.append({
            'name': nickname,
            'score': score,
            'date': datetime.datetime.now().strftime('%Y-%m-%d')
        })
        leaderboard.sort(key=lambda x: x['score'], reverse=True)
    return render_template('leaderboard.html', leaderboard=leaderboard)

@app.route('/nickname')
def nickname():
    return render_template('nickname.html')

if __name__ == '__main__':
    app.run(debug=True)
