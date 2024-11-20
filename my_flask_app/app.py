from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# 初期クリックカウント
click_count = 0

@app.route('/')
def index():
    global click_count
    return render_template('index.html', click_count=click_count)

@app.route('/increment', methods=['POST'])
def increment():
    global click_count
    data = request.get_json()
    click_count = data['count']
    return jsonify(success=True), 200

if __name__ == '__main__':
    app.run(debug=True)
