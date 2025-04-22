import time

from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_title = request.form["job_title"]
        if job_title:
            try:
                # Use the correct model name
                time.sleep(1)
                model = genai.GenerativeModel("gemini-1.5-flash-latest")
                response = model.generate_content(
                    f"identify the movie or series name, \n\n"
                    f"Identify the main cast and director of the movie or series{job_title}"
                    f"give a small glimpse of the movie or series{job_title}"
                    f"Identify the budget and worldwide collection of the movie or series{job_title}"
                    f"Identify the Censor Board Certificate for the movie or series{job_title}"
                    f"identify in which streaming platform it can watch{job_title}"
                    f"what is the rating of the movie or the series{job_title}"
                    f"the information which is being provided should be latest keep it concise and professional (maximum 5-7 sentences)\n"
                )
                result = response.text.replace(". ", ".<br><br>")
                return render_template("index.html", job_title=job_title, result=result)
            except Exception as e:
                import traceback
                traceback.print_exc()
                return f"Error: {str(e)}"
    return render_template("index.html", job_title=None, result=None)


