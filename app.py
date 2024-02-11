from flask import Flask, send_file, jsonify, redirect, url_for, render_template
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

@app.route('/mlflow')
def mlflow_ui():
    # This assumes MLflow is running on the default port 5000 on the host machine
    return redirect("http://127.0.0.1:5000")

@app.route('/site-map')
# https://stackoverflow.com/questions/13151161/display-links-to-new-webpages-created/13161594#13161594
def all_links():
    links = []
    for rule in app.url_map.iter_rules():
        if len(rule.defaults) >= len(rule.arguments):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return render_template("all_links.html", links=links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

