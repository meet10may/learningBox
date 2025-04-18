import json
import subprocess

def load_questions(subject_path):
    with open(subject_path, "r") as f:
        return json.load(f)

def speak(text):
    volume = 200         # Max is 200, default is 100
    speed = 130    
    subprocess.run(["espeak", f"-a{volume}", f"-s{speed}", text])

def ask_question(question_data):
    question = question_data["question"]
    speak(question)
    print(f"\n🧠 {question}")
