# 🍳 Smart Recipe Explorer (Backend)

> A modern, AI-powered Recipe Management System built with **FastAPI**, **PostgreSQL**, and **Google Gemini Generative AI**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql)
![Google Gemini](https://img.shields.io/badge/GenAI-Gemini%201.5-8E75B2?style=for-the-badge)

## 📖 Evaluation Overview
This project is developed as part of a Python Backend/Full-Stack assessment. It demonstrates:
- **Clean Architecture Implementation** (Separation of Concerns)
- **REST API Design Best Practices**
- **Strict Typing** with Pydantic & SQLAlchemy
- **Integration of LLMs** (Large Language Models) for practical features.

---

## 🏗️ Architecture
The project follows a modular 3-layer architecture to ensure scalability and maintainability.

```mermaid
graph TD
    Client["Frontend / API Client"] -->|"HTTP Request"| API["API Layer (app/api)"]
    API -->|"Validation"| Schema["Pydantic Schemas"]
    API -->|"Business Logic"| GenAI["GenAI Service (app/genai)"]
    API -->|"Data Access"| DB["Database Layer (app/database)"]
    GenAI -->|"External API"| Gemini["Google Gemini API"]
    DB -->|"SQL"| Postgres[("PostgreSQL")]
```

### 📂 Folder Structure
The codebase is organized for clarity:

```text
Python-Backend-API/
├── app/
│   ├── api/          # 🌐 Routes & Controllers (REST Interface)
│   ├── database/     # 💾 Database Models & Connection Logic
│   ├── genai/        # 🧠 Service Layer for AI Logic (Gemini)
│   ├── config.py     # ⚙️ Configuration & Environment handling
│   └── schemas.py    # 🛡️ Pydantic Data Validation Models
├── main.py           # 🚀 Application Entry Point
└── requirements.txt  # 📦 Dependencies
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL Database
- Google AI Studio API Key

### 🛠️ Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/smart-recipe-explorer.git
    cd smart-recipe-explorer
    ```

2.  **Create Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Create a `.env` file in the `Python-Backend-API` directory:
    ```ini
    # Database Connection (PostgreSQL)
    Database_url="postgresql://user:password@localhost:5432/smart_recipe_db"

    # Google Gemini API Key (Free Tier)
    Gemini_Api_Key="your_gemini_api_key_here"
    ```

5.  **Run the Application**
    ```bash
    cd Python-Backend-API
    uvicorn main:app --reload
    ```
    The server will start at `http://127.0.0.1:8000`.

---

## ⚡ API Documentation

You can view the interactive **Swagger UI** at `http://127.0.0.1:8000/docs`.

### 🥘 Recipes

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/recipes` | List all recipes |
| `GET` | `/recipes/{id}` | Get detailed view of a recipe |
| `POST` | `/recipes` | Create a new recipe |
| `POST` | `/recipes/search` | **Smart Search** by Name AND/OR Ingredients list |

### 🧠 GenAI Features

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/ai/suggest` | Suggests a recipe based on a list of ingredients |
| `POST` | `/ai/simplify` | Rewrites complex instructions into simple steps |

---

## 🧪 Sample Payloads

**Create Recipe:**
```json
{
  "name": "Paneer Butter Masala",
  "cuisine": "Indian",
  "isVegetarian": true,
  "prepTimeMinutes": 45,
  "ingredients": ["Paneer", "Tomato Puree", "Cream", "Butter"],
  "difficulty": "Medium",
  "instructions": "Fry spices, add tomato puree...",
  "tags": ["Dinner", "Rich"],
  "description": "A classic North Indian delight."
}
```

**Smart Search:**
```json
{
  "name": "Paneer",
  "ingredients": ["Tomato Puree"]
}
```
*(Finds recipes named "Paneer..." that ALSO contain "Tomato Puree")*

---

## 🛠️ Technology Stack
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic V2
- **AI Model**: Google Gemini 1.5 Flash
- **Server**: Uvicorn

---

