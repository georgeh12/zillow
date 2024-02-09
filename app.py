from flask import Flask, send_file, jsonify
from model import generate_plot_and_metrics

app = Flask(__name__)

@app.route('/')
def plot():
    buf, metrics = generate_plot_and_metrics()
    return send_file(buf, mimetype='image/png')

@app.route('/metrics')
def show_metrics():
    _, metrics = generate_plot_and_metrics()
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
