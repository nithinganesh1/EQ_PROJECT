from flask import Flask, render_template, request, session, redirect, url_for
from ai.eq_engine import (
    generate_scenario, 
    generate_questions, 
    calculate_eq,
    get_eq_interpretation
)

app = Flask(__name__)
app.secret_key = "your-secret-key-change-in-production"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Store user info in session
        session['age'] = request.form.get("age")
        session['gender'] = request.form.get("gender")
        session['profession'] = request.form.get("profession")
        
        return redirect(url_for('questions'))
    
    return render_template("index.html")

@app.route("/questions")
def questions():
    profession = session.get('profession', 'professional')
    scenario = generate_scenario(profession)
    questions_list = generate_questions()
    
    return render_template(
        "questions.html", 
        scenario=scenario, 
        questions=questions_list
    )

@app.route("/result", methods=["POST"])
def result():
    try:
        responses = request.form.getlist("answer")
        
        # Validate we have all responses
        if len(responses) != 5:
            return "Error: Please answer all questions", 400
        
        overall, breakdown = calculate_eq(responses)
        interpretation = get_eq_interpretation(overall)
        
        # Get user info from session
        user_info = {
            'age': session.get('age'),
            'gender': session.get('gender'),
            'profession': session.get('profession')
        }
        
        return render_template(
            "result.html", 
            overall=overall,
            interpretation=interpretation,
            breakdown=breakdown,
            user_info=user_info
        )
    except Exception as e:
        return f"Error processing results: {str(e)}", 500

@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
