#  Blood Request Web App (Flask)

This is a simple web application built with **Python Flask** that allows users to submit blood donation requests via a form. All data is stored in a local CSV file and can be viewed in a table or downloaded.

---

##  Features

- 📄 Submit blood request through a form  
- 📊 View all submitted requests in a table format  
- 📥 Download all request data as a CSV file  
- 💾 Data stored locally (no database needed)  

---

##  Project Structure

```
Blood_req/
├── app.py
├── README.md
├── blood_requests.csv        ← (auto-generated after submission)
├── screenshot.png            ← (optional, add your screenshot)
└── templates/
    ├── form.html
    └── requests.html
```

---

##  How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/saifahmad6462/BS_Blood_request_form.git
cd BS_Blood_request_form
```

2. **Install Flask**

```bash
pip install flask
```

3. **Run the application**

```bash
python app.py
```

4. **Open in your browser**

```
http://127.0.0.1:5000
```

---

##  Screenshot



<!-- ![Screenshot of Blood Request Form](Blood_req.png) -->
<!-- ![Screenshot of Blood Request Form](Blood_req2.png) -->
<!-- ![Screenshot of Blood Request Form](Blood_req3.png) -->

---

##  Tech Stack

- Python 3  
- Flask  
- HTML (Jinja2 templating)  
- CSV for local data storage  

---

##  Contact

Feel free to connect via GitHub [@saifahmad6462](https://github.com/saifahmad6462)  

