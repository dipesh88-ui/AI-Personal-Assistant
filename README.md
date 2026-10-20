# 🤖 AI Personal Assistant

An AI-powered web application built using **Python, Flask, and Groq API** that helps users get instant answers to their questions and summarize lengthy emails into concise, meaningful summaries.

🔗 **Live Demo:** [AI Personal Assistant](https://ai-personal-assistant-37iv.onrender.com)

## ✨ Features

- **AI Chat Assistant:** Ask questions and receive intelligent, AI-generated responses.
- **Email Summarization:** Convert lengthy emails into concise 2–3 sentence summaries.
- **Simple User Interface:** Clean and user-friendly design for a smooth experience.
- **Real-Time Responses:** Get results dynamically without reloading the webpage.
- **Error Handling:** Handles empty inputs, API configuration issues, and request errors.
- **Cloud Deployment:** Accessible online through Render.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI Integration:** Groq API, LLM
- **Frontend:** HTML5, CSS3, JavaScript
- **Environment Management:** python-dotenv
- **Deployment:** Render, Gunicorn

## ⚙️ How It Works

1. **Ask Anything:** Enter a question, and the application sends it to the Groq API to generate an AI-powered response.
2. **Summarize Email:** Paste an email, and the AI generates a concise summary in 2–3 sentences.
3. **Display Results:** The generated answers and summaries appear directly on the webpage.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd AI-Personal-Assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Get your API key from the [Groq Console](https://console.groq.com/).

### 4. Run the Application

```bash
python main.py
```

Open your browser and visit:

`http://127.0.0.1:5000`

## 🌐 Live Deployment

The application is deployed on Render.

**Try it here:** https://ai-personal-assistant-37iv.onrender.com

## 🔮 Future Enhancements

- Add chat history and conversational memory.
- Integrate voice input and text-to-speech.
- Support document uploads and summarization.
- Improve mobile responsiveness.
- Add user authentication and personalization.

## 👨‍💻 Author

**Dipesh Kumar**  
B.Tech in Computer Science and Engineering

---

⭐ If you like this project, consider giving the repository a star!

*Built with Python, Flask, and Generative AI.*
