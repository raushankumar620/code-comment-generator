# 📝 Code Comment Generator

## 📌 Overview
The **Code Comment Generator** is an AI-powered tool that automatically adds meaningful comments to Python code.  
It uses **NLP (Natural Language Processing) techniques** with **T5 Transformer models** to analyze and generate comments.  

🔹 **Problem Statement**: Writing comments manually can be time-consuming and inconsistent.  
🔹 **Solution**: This tool **automatically** generates comments, making code **more readable** and **easy to understand**.

---

## 🚀 Features
✔️ **AI-based Comment Generation** using `T5 Transformer`  
✔️ **Manual Commenting for Simple Code Blocks** (like `print()` and variable assignments)  
✔️ **Interactive Web Interface** built with Flask & JavaScript  
✔️ **Supports Multi-line Code Input**  
✔️ **Fast & Accurate Commenting**  

---

## 📷 Project Screenshot  
![Project UI](https://github.com/raushankumar620/code-comment-generator/blob/main/Screenshot%202025-03-12%20154557.png)

---

## 🛠️ Technologies Used & How They Work  
| Technology | Purpose |
|------------|---------|
| **Python** | Backend Development |
| **Flask** | Web Framework for API & UI Handling |
| **NLP (Natural Language Processing)** | Understanding & Generating Comments |
| **Transformers (T5 Model)** | AI Model for Comment Generation |
| **Torch (PyTorch)** | Running Deep Learning Models |
| **HTML, CSS, JavaScript** | Frontend UI for User Interaction |
| **AJAX** | Sending Code Input to Server & Getting Output |

### **🧠 How This Works Internally?**
1️⃣ **User Inputs Python Code** in the web interface  
2️⃣ **Flask Backend Receives Code** via API  
3️⃣ **Manual Rule-Based Comments** are added for simple operations (like `print()`, `=` assignments)  
4️⃣ **T5 Transformer NLP Model Processes Complex Code** & Generates Comments  
5️⃣ **Final Commented Code is Sent Back** & Displayed in UI  

---

## ⚙️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/raushankumar620/code-comment-generator.git
cd code-comment-generator
