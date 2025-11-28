Here is a **beautiful, professional, GitHub-ready README.md** — clean formatting, emojis, screenshots, sections, everything perfectly organized.
You can **copy–paste directly** into your GitHub repository.

---

# 🎬 **VidSynth AI — YouTube Content Synthesizer**

**Transform any YouTube video into notes, key topics, or chat with the video using RAG — all in one place.**

VidSynth AI is a powerful AI-driven tool that extracts transcripts, translates them, generates notes, identifies important topics, and even allows you to **chat with the video** using a Retrieval-Augmented Generation (RAG) system.

---

## 🚀 **Overview**

VidSynth AI takes any YouTube URL and turns it into:

✔️ **Important Topics**
✔️ **Structured, concise Notes**
✔️ **Interactive Chatbot (RAG-based)**
✔️ **Accurate Translation (Any language → English)**

Powered by **Google Gemini**, **LangChain**, **ChromaDB**, and **YouTube Transcript API**.

---

## ✨ **Features**

### 🔍 **1. Transcript Extraction**

* Fetches video transcripts using `youtube-transcript-api`.
* Supports multiple languages: `en`, `hi`, `es`, `fr`, and more.

### 🌐 **2. Smart Translation**

* Uses **Gemini 2.5 Flash Lite** for highly accurate English translation.
* Preserves meaning, tone, nuance, and intent.

### 🧠 **3. Important Topic Extraction**

* Extracts the **top 5 key topics** from the video.
* Ensures clarity, relevance, and conciseness.

### 📝 **4. AI-Generated Notes**

* Clean, structured notes with bullet points & subheadings.
* Ideal for studying, revision, or quick understanding.

### 💬 **5. Chat with Video (RAG)**

* Embeds transcript using **Google Embeddings**.
* Stores vectors in **ChromaDB**.
* Ask any question — it finds answers *only from the video content*.

---

## 🛠️ **Tech Stack**

* **Python**
* **Streamlit** for UI
* **Google Gemini 2.5 Flash Lite**
* **LangChain**
* **ChromaDB**
* **YouTube Transcript API**

---

## 🖼️ **Project Screenshots**

### 🟦 **Home Interface**
<img width="100%" alt="Screenshot 3" src="https://github.com/user-attachments/assets/fccf6b28-d325-45b2-828f-19301cd370f1" />

---

### 🟩 **Notes & Important Topics**

<img width="1920" height="1080" alt="yt_buudy" src="https://github.com/user-attachments/assets/5cdfab04-c7a5-4bc6-a032-583e04ca9b97" />





---

### 🟧 **Chat With Video (RAG Interface)**


<img width="100%" alt="Screenshot 2" src="https://github.com/user-attachments/assets/3abc2253-4c48-4c66-9e48-7d8629d5411a" />


---

## 📦 **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/Rohansinghjadoan/YT_Buddy.git
cd YT_Buddy
```

### **2. Create a Virtual Environment**

```bash
python3 -m venv yt_buddy
source yt_buddy/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Add Gemini API Key**

Create a file named **`.env`**:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ **Run the App**

```bash
streamlit run app.py
```

---

## ⚙️ **How It Works (Pipeline)**

### 🔹 Step 1 — Extract Transcript

Using YouTube Transcript API.

### 🔹 Step 2 — Translate (if needed)

Gemini ensures accurate English translation.

### 🔹 Step 3 — Create Chunks

Splits the text into overlapping chunks.

### 🔹 Step 4 — Embed + Store

Embeds using Google Embeddings → stored in ChromaDB.

### 🔹 Step 5 — RAG Query

User asks a question → vector search → Gemini generates answer.

---

## 🙋‍♂️ **Author**

**Rohan Singh Jadoan**
AI/ML Developer • Python • Deep Learning

---

## ⭐ **Like the project?**

Don’t forget to **star** ⭐ the repo — it helps !

