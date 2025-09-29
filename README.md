# projectscribe-ai

An AI-powered application that generates **Business Requirement Documents (BRDs)** and **UI design descriptions for Figma**, with optional **Jira ticket automation**.  
Built using **Streamlit, Ollama- llama (LLM), Jira API, and Figma plugins**, this project demonstrates how generative AI can accelerate product documentation and design workflows.

---

## 🚀 Features

- 📝 **BRD Generator** – Expands a short project description into a structured BRD (overview, objectives, requirements, user stories, etc.)
- 🎨 **UI Description Generator** – Converts natural language prompts into plain-English UI descriptions for Figma plugins
- 📊 **Figma Preview** – Paste AI-generated descriptions into a Figma plugin (like Magician) and preview mockups
- 🏷 **Jira Ticket Automation** – Create Jira tasks directly from the generated BRD and UI preview
- ⚡ **Configurable LLM Parameters** – Supports `temperature`, `top-p`, and other settings for better control
- 🔒 **Environment Variables** – Secure integration with Jira using `.env` file

---

## 📂 Project Structure

```

ai-brd-ui-generator/
│
├── main_app.py               # Streamlit app entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .env.example              # Example environment variables
├── .gitignore                # Ignore cache, env, logs, etc.
├── LICENSE                   # MIT License
├── utils/
│   ├── ollama_helper.py      # LLM text generation helper
│   └── jira_helper.py        # Jira ticket creation helper
└── assets/
    └── brd_example.png       # Screenshot examples

````

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/pranavibunny/projectscribe-ai.git
cd projectscribe-ai
````

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables

Create a `.env` file in the root directory for Jira API:

```env
JIRA_DOMAIN=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API=your-api-token
PROJECT_KEY= your-project-key
```

### 5️⃣ Run the app

```bash
streamlit run main_app.py
```

---

## 💡 How It Works

1. **Generate BRD**

   * Enter a project description
   * AI expands it into a structured Business Requirement Document

2. **Review & Edit BRD**

   * Edit the generated BRD if needed
   * Provide a Jira summary line

3. **Generate UI Description**

   * Enter a UI prompt (e.g., *"Shopping cart with product images, quantity, and checkout button"*)
   * AI outputs a plain-English UI description

4. **Preview in Figma**

   * Copy the description into a Figma plugin like *Magician*
   * Paste the preview image URL into Streamlit

5. **Create Jira Ticket**

   * Combine BRD + Figma preview into a Jira task
   * Auto-generate ticket directly in your Jira project

---

## 🧪 Example Prompts

### BRD Generator

```
Build a shopping cart system for an e-commerce website that allows customers to add, edit, and remove items before checkout.
```

### UI Generator

```
Create a shopping cart UI with product images, item names, quantity selector, price, subtotal, and a checkout button at the bottom.
```

---

## ⚡ Performance Tweaks

* **Temperature** → Lower for more factual, higher for creative BRDs
* **Top-p / Top-k** → Adjust response diversity
* **Prompt Padding** → Add extra context/examples for consistency
* **Caching** → Reuse LLM outputs for repeated prompts to reduce latency

---

## 🎥 Demo

assets

---

## 🔮 Future Improvements

Support multiple LLMs (OpenAI, Anthropic, etc.)
Automate Figma API integration (no manual plugin needed)
Generate BRDs in multiple languages
Publish BRDs directly to Confluence
Automatically create and assign multiple Jira issues to respective teams

---

## 🛡 License

This project is licensed under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Pranavi Katarapu**
💼 Aspiring AI Engineer | Generative AI Enthusiast
📌 [LinkedIn](https://www.linkedin.com/in/pranavi-katarapu-317425384/) • [GitHub](https://github.com/pranavibunny)
