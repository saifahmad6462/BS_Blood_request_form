from flask import Flask, render_template, request, send_file
import csv
import os
<<<<<<< HEAD
import uuid

app = Flask(__name__)
=======

app = Flask(__name__)

>>>>>>> f5aeaee12be7dddc6525fd82eca26b7362bb2cff
CSV_FILE = 'blood_requests.csv'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
<<<<<<< HEAD
    request_code = str(uuid.uuid4())[:8].upper()
    data = {
        'request_code': request_code,
=======
    data = {
>>>>>>> f5aeaee12be7dddc6525fd82eca26b7362bb2cff
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

<<<<<<< HEAD
    return f"""
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>Thank You</title>
  <script src='https://cdn.tailwindcss.com'></script>
=======
    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Thank You</title>
  <script src="https://cdn.tailwindcss.com"></script>
>>>>>>> f5aeaee12be7dddc6525fd82eca26b7362bb2cff
  <style>
    @keyframes pulseText {{
      0% {{ opacity: 0.3; transform: scale(1); }}
      50% {{ opacity: 1; transform: scale(1.05); }}
      100% {{ opacity: 0.3; transform: scale(1); }}
    }}
  </style>
</head>
<<<<<<< HEAD
<body class='bg-gradient-to-br from-red-100 via-white to-red-200 min-h-screen flex items-center justify-center'>
  <div class='backdrop-blur-md bg-white/30 border border-white/40 shadow-xl rounded-3xl px-10 py-14 text-center max-w-lg w-full'>
    <h1 class='text-3xl font-bold text-red-600 mb-4'>&#9989; Thank You, {data['name']}!</h1>
    <p class='text-lg text-gray-800 mb-2'>Your request code is:</p>
    <p class='text-lg font-bold text-blue-800 mb-6'>{data['request_code']}</p>
    <p class='text-red-600 text-xl font-semibold animate-pulse' style='animation: pulseText 2s infinite;'>&#128657; Help is on the way...</p>
    <div class='mt-8 flex justify-center gap-4'>
      <a href='/' class='bg-red-500 hover:bg-red-600 text-white px-6 py-2 rounded-xl transition transform hover:scale-105'>New Request</a>
      <a href='/requests' class='bg-white/60 text-red-600 border border-red-300 px-6 py-2 rounded-xl hover:bg-white/80 transition transform hover:scale-105'>View All</a>
=======
<body class="bg-gradient-to-br from-red-100 via-white to-red-200 min-h-screen flex items-center justify-center">
  <div class="backdrop-blur-md bg-white/30 border border-white/40 shadow-xl rounded-3xl px-10 py-14 text-center max-w-lg w-full">
    <h1 class="text-3xl font-bold text-red-600 mb-4">✅ Thank You, {data['name']}!</h1>
    <p class="text-lg text-gray-800 mb-6">Your blood request has been recorded.</p>
    <p class="text-red-600 text-xl font-semibold animate-pulse" style="animation: pulseText 2s infinite;">🚑 Help is on the way...</p>
    <div class="mt-8 flex justify-center gap-4">
      <a href="/" class="bg-red-500 hover:bg-red-600 text-white px-6 py-2 rounded-xl transition transform hover:scale-105">New Request</a>
      <a href="/requests" class="bg-white/60 text-red-600 border border-red-300 px-6 py-2 rounded-xl hover:bg-white/80 transition transform hover:scale-105">View All</a>
>>>>>>> f5aeaee12be7dddc6525fd82eca26b7362bb2cff
    </div>
  </div>
</body>
</html>
<<<<<<< HEAD
"""
=======
'''
>>>>>>> f5aeaee12be7dddc6525fd82eca26b7362bb2cff

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

<<<<<<< HEAD
=======
@app.route('/delete_entry', methods=['POST'])
def delete_entry():
    name = request.form['del_name'].strip().lower()
    contact = request.form['del_contact'].strip()

    if not os.path.exists(CSV_FILE):
        return "<h3>No data found.</h3>"

    with open(CSV_FILE, 'r') as f:
        reader = list(csv.reader(f))
        headers = reader[0]
        data = reader[1:]

    updated_data = [row for row in data if not (row[0].strip().lower() == name and row[5].strip() == contact)]

    if len(updated_data) == len(data):
        return "<h3>❌ No matching entry found to delete.</h3><a href='/'>Back</a>"

    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(updated_data)

    return f"<h3>✅ Entry for {name.title()} deleted successfully.<br><a href='/'>Back</a></h3>"

>>>>>>> f5aeaee12be7dddc6525fd82eca26b7362bb2cff
if __name__ == '__main__':
    app.run(debug=True)
