# PitchPal AI

**PitchPal AI** is an intelligent pitch generation system powered by a large language model (LLM). It helps users quickly generate persuasive business pitch content based on a simple product description. Designed for startup teams, business professionals, and students, PitchPal AI combines structured pitch templates with the power of natural language generation to assist in creating professional pitch drafts in seconds.

## 🔍 Project Overview

PitchPal AI transforms a short product idea into a structured pitch paragraph covering:
- Product value
- The problem it solves
- Target market or users
- Business model

It also includes a **persuasiveness scoring module** and a **competitor analysis tool**, offering users both content and insight to improve their business proposals.

## ✨ Features

- **Startup Pitch Generator**: Generates one-paragraph pitch content using Hugging Face’s `t5-base` model.
- **Persuasiveness Scoring**: Analyzes keywords related to effective business communication and returns a score (0–100).
- **Competitor Analysis**: Parses a CSV of competing brands and highlights their unique selling propositions (USPs).
- **Interactive Demo in Google Colab**: Fully executable and user-friendly in a cloud environment without any setup.

## 🛠️ Technologies Used

- **Language Model**: [`t5-base`](https://huggingface.co/t5-base) from Hugging Face Transformers
- **Platform**: Google Colab (Jupyter Notebook)
- **Programming Language**: Python 3
- **Libraries**: `transformers`, `pandas`

## 🚀 How to Use

1. Open the `PitchPal_AI.ipynb` file in [`Google Colab`]([https://colab.research.google.com/](https://colab.research.google.com/drive/1VnJb7vALjBj2LnGtD6GApCQ413DEspt2?usp=sharing)).
2. Choose a product description or type your own.
3. Run the pitch generator to receive an auto-generated business pitch.
4. View the persuasiveness score based on business-relevant keywords.
5. Upload a competitor CSV file (`example_data.csv`) to see key differentiators.

### Example CSV format for competitor analysis:

```csv
Brand,USP
Notion,All-in-one workspace for notes and tasks
Evernote,Clip and organize web content with ease

📂 Folder Structure

PitchPalAI/
├── main.ipynb              # Google Colab-compatible demo
├── pitch_generator.py      # Python function to generate pitch content
├── competitor_analyzer.py  # Reads CSV and prints competitor summary
├── example_data.csv        # Sample competitor data
├── README.md               # Project description

🌐 Open Source Platforms Applied
	• GitHub – version control and source code hosting
	• Hugging Face – open-source model access (t5-base)
	• Google Colab – cloud-based runtime for interaction and sharing

📌 Target Users & Applications
	• Startup teams and founders
	• Business proposal writers
	• Entrepreneurship educators and students
	• Innovation accelerators and business incubators

PitchPal AI can be used in startup competitions, proposal workshops, investor presentations, or AI-assisted business education.

📝 License

This project is released under the MIT License.

⸻

Made with AI & creativity — by PitchSense AI
