import streamlit as st
from smolagents import CodeAgent, DuckDuckGoSearchTool, GoogleSearchTool,VisitWebpageTool, HfApiModel

import os
from huggingface_hub import login

# Retrieve the token from the environment variable
hf_token = os.getenv('HF_TOKEN')

# Login using the token
login(token=hf_token)

# Define the blog-writing agent with DuckDuckGo tool
blog_agent = CodeAgent(
    #tools=[DuckDuckGoSearchTool()], 
    tools=[GoogleSearchTool(), VisitWebpageTool()], 
    model=HfApiModel()
)

# Function to log agent actions
def log_agent_action(prompt, result, agent_name):
    st.write(f"### Agent Activity ({agent_name}):")
    st.write("**Prompt Sent to Agent:**")
    st.code(prompt, language="text")
    st.write("**Agent Output:**")
    st.code(result, language="text")

# Streamlit app title
st.title("AI Blog Writing Agent with Real-Time Insights")

# App description
st.write("Generate creative blogs enriched with insights gathered with Web search using the AI Blog Writing Agent powered by SmolAgents and Google Search API.")

# Input blog topic or prompt
blog_prompt = st.text_area("Enter your blog topic or prompt:", placeholder="E.g., Best Ideas for investments in 2025")

# Button to generate blog content
if st.button("Generate Blog Content"):
    if blog_prompt:
        with st.spinner("Generating blog content with google search insights..."):
            try:
                # Run the blog agent with the given prompt
                blog_result = blog_agent.run(blog_prompt)
                # Display the generated blog content
                st.subheader("Generated Blog Content:")
                st.write(blog_result)

                # Log backend activity
                log_agent_action(blog_prompt, blog_result, "Blog Writing Agent with GoogleSearchTool")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a blog topic or prompt to proceed.")

# Footer
st.markdown("---")
st.caption("Powered by SmolAgents, GoogleSearchTool, and Streamlit")
