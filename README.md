# AI Blog Writing Agent with Real-Time Insights

Generate creative blogs enriched with insights from real-time web searches using **SmolAgents**, **Google Search API**, and **Streamlit**.

## Features
- **Web Search Integration**: Uses Google Search API and VisitWebpageTool for live insights.
- **AI-Generated Content**: Powered by SmolAgents and Hugging Face models.
- **Interactive UI**: Built with Streamlit for ease of use.
- **Action Logs**: Displays prompts and outputs for transparency.

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/annads/simple_search_agent.git
   cd simple_search_agent

2. Install dependencies:
pip install -r requirements.txt

3. Set Hugging Face API token:
export HF_TOKEN='your_hugging_face_token'

## Usage
Run the app:

streamlit run app.py

Open the app in your browser (default: http://localhost:8501).
Enter a blog topic or prompt (e.g., "Best Ideas for Investments in 2025").
Click Generate Blog Content and view the results.

## Tools Used
SmolAgents: AI agent framework.
GoogleSearchTool: Real-time search integration.
Streamlit: Interactive UI.
Hugging Face API: Underlying AI models.
