from flask import Flask, render_template, request, send_file
import csv
import os

app = Flask(__name__)

CSV_FILE = 'blood_requests.csv'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form['name'],
        'age': request.form['age'],
        'blood_type': request.form['blood_type'],
        'units': request.form['units'],
        'hospital': request.form['hospital'],
        'contact': request.form['contact'],
        'urgency': request.form['urgency'],
        'notes': request.form.get('notes', '')
    }

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(data.keys())
        writer.writerow(data.values())

    return f"<h2>✅ Thank you {data['name']}. Request saved successfully!<br><a href='/requests'>View All Requests</a></h2>"

@app.route('/requests')
def show_requests():
    if not os.path.exists(CSV_FILE):
        return "<h3>No requests found.</h3>"

    with open(CSV_FILE, mode='r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        headers = rows[0] if rows else []
        data = rows[1:] if len(rows) > 1 else []

    return render_template('requests.html', headers=headers, data=data)

@app.route('/download')
def download_csv():
    if os.path.exists(CSV_FILE):
        return send_file(CSV_FILE, as_attachment=True)
    else:
        return "<h3>No CSV file found to download.</h3>"

if __name__ == '__main__':
    app.run(debug=True)
