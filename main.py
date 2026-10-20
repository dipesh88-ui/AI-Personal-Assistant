from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

app = Flask(__name__)

load_dotenv()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    load_dotenv(override=True)
    question = request.form.get("question")
    if not question:
        return jsonify({"response": "Please enter a question."}), 400

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return jsonify({"response": "Error: GROQ_API_KEY is not set. Please configure it in your .env file."}), 500

    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Act like a helpful personal assistant. Provide clear, direct, and readable responses. "
                        "Do NOT use markdown formatting marks: do not use asterisks for bolding (no **), "
                        "do not use hash symbols for headings (no ###), and do not use markdown tables or pipes (|). "
                        "Write in clean plain text with standard paragraphs and clean hyphens (-) for lists if needed."
                    )
                },
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        choice = response.choices[0]
        content = choice.message.content or getattr(choice.message, "reasoning", "") or ""
        answer = content.strip() if content else "No response generated."
        return jsonify({"response": answer}), 200
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

@app.route("/summarize", methods=["POST"])
def summarize():
    load_dotenv(override=True)
    email_text = request.form.get("email")
    if not email_text:
        return jsonify({"response": "Please provide an email to summarize."}), 400

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return jsonify({"response": "Error: GROQ_API_KEY is not set. Please configure it in your .env file."}), 500

    prompt = f"summarize the following email in 2-3 sentences: {email_text}"
    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Act like an expert email assistant. Summarize clearly in 2-3 sentences. "
                        "Do NOT use markdown marks like asterisks (**) or hashes (###). Use clean plain text."
                    )
                },                
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1024
        )
        choice = response.choices[0]
        content = choice.message.content or getattr(choice.message, "reasoning", "") or ""
        summary = content.strip() if content else "Unable to generate summary."
        return jsonify({"response": summary}), 200
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)

