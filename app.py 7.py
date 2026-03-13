from flask import Flask, render_template, request

app = Flask(__name__)

qa = {
    "hi": "Hello! Welcome to Sri Raaja Raajan College of Engineering and Technology.",
"hello": "Hi! How can I help you about our college?",
"thanks": "You are welcome!",
    "courses": "Our college offers CSE, ECE, EEE, MECH, CIVIL, B.Tech(agriculture).",
    "college": "Our college name is Sri Raaja Raajan College of Engineering and Technology.",
    "fees": "Average course fee is 80000 per year.",
    "hostel": "Hostel facility available.",
    "placement": "Our college provides good placement support.",
    "library": "Library is open from 10 AM to 4 PM.",
    "transport": "College buses available from major areas.",
    "admission": "Admission can be done through online or office.",
    "contact": "You can contact college office at 9487441043.",
    "principal": "Principal of our college is Dr. Mahalingam suresh.",
    "location": "Our college is located in karaikudi."
}


@app.route("/", methods=["GET","POST"])
def home():
    response = ""
    if request.method == "POST":
        user = request.form["question"].lower()
        if user in qa:
            response = qa[user]
        else:
            response = "Sorry, I don't understand."
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)