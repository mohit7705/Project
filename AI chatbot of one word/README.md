# Flan-T5 Short Answer Chatbot  
A simple AI chatbot built using the **Flan-T5 model (google/flan-t5-base)**.  
This chatbot answers questions in **one short sentence**, making it perfect for  
AI projects, demos, and CodSoft internship submissions.

---

## 📌 Features
- Uses **Flan-T5 Base** (or Small) for question answering.
- Gives **short, clean, and meaningful replies**.
- Works offline after model download.
- Easy to run on any laptop.
- Simple Python code (only 1 main file).

---

## 📂 Folder Structure
Extra_FlanT5_Chatbot/
│
├── smart_flan_t5.py # Main chatbot program
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🛠 Requirements
Install the required packages:

pip install -r requirements.txt

yaml
Copy code

This installs:
- `transformers`
- `torch`
- `sentencepiece`

These are needed to run the Flan-T5 model.

---

## ▶️ How to Run the Chatbot

1. Open terminal (VS Code or CMD).
2. Go to the project folder:
cd Extra_FlanT5_Chatbot

markdown
Copy code
3. Run the chatbot:
python smart_flan_t5.py

yaml
Copy code

4. Start chatting!  
Type **bye** to exit the chatbot.

---

## 💡 Example Chat

You: hi
Bot: Hello! How can I help you?

You: what is python
Bot: Python is a popular programming language.

You: tell me something interesting
Bot: Honey never spoils.

You: bye
Bot: Goodbye!

yaml
Copy code

---

## 🤖 Model Used
- **Model:** google/flan-t5-base  
- **Size:** ~230 MB  
- **Capabilities:**  
  ✔ Short answers  
  ✔ Factual replies  
  ✔ General question answering  
  ✔ Lightweight and fast  

You can switch to the smaller model by editing this line in `smart_flan_t5.py`:

MODEL_NAME = "google/flan-t5-small"

yaml
Copy code

---

## 📘 Notes
- The model is downloaded only once and stored in:
C:\Users\YOURNAME.cache\huggingface\hub\

yaml
Copy code
- If your laptop has low space or RAM, use the smaller Flan-T5 model.
- This project is fully suitable for the **CodSoft AI Internship Task (Chatbot)**.

---

## 🏁 Completion Status
✔ Task: Create a short-response AI chatbot  
✔ Framework used: Python + HuggingFace Transformers  
✔ Works locally and can be deployed anywhere  

---

## 🔗 Author  
Created by **Mohit Rao**  
