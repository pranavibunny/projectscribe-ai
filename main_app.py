import streamlit as st
from utils.ollama_helper import generate_text_with_ollama
from utils.jira_helper import create_jira_issue

st.set_page_config(page_title="AI-Powered BRD & UI Generator", layout="wide")

# ---------------- Prompts ----------------
BRD_SYSTEM_PROMPT = """
You are a highly professional Business Requirements Document (BRD) writer.
Take the user project description and expand it into a well-structured BRD.
Include: Overview, Objectives, Stakeholders, Functional Requirements,
Non-Functional Requirements, Assumptions, Scope, User Stories, References.
"""

UI_SYSTEM_PROMPT = """
You are a professional UI design assistant.
Take the user prompt and output a clear plain-English description of a UI page.
Describe frames, elements, labels, and content in simple terms, suitable for Figma plugin.
"""

# ---------------- Session State ----------------
for key in ["generated_brd", "editable_brd", "summary_line", "ui_description", "figma_preview_url"]:
    if key not in st.session_state:
        st.session_state[key] = None

st.title("🤖 AI-Powered BRD & Figma UI Generator with Jira Integration")

# ---------------- Step 1: Generate BRD ----------------
project_prompt = st.text_area("Enter your project description:")

if st.button("Generate BRD"):
    if project_prompt.strip():
        with st.spinner("Generating BRD..."):
            brd_doc = generate_text_with_ollama(f"{BRD_SYSTEM_PROMPT}\n\nProject Description:\n{project_prompt}")
            st.session_state.generated_brd = brd_doc
            st.session_state.editable_brd = brd_doc
            st.session_state.summary_line = brd_doc.splitlines()[0] if brd_doc else "Auto-generated task"
        st.success("✅ BRD generated!")

# ---------------- Step 2: Review BRD ----------------
if st.session_state.generated_brd:
    st.subheader("Review & Edit BRD")
    st.session_state.editable_brd = st.text_area(
        "Editable BRD:",
        value=st.session_state.editable_brd,
        height=300
    )
    st.session_state.summary_line = st.text_input(
        "Jira Ticket Summary:",
        value=st.session_state.summary_line
    )

# ---------------- Step 3: Generate UI Description ----------------
st.subheader("Generate UI Description for Figma Plugin")
ui_prompt = st.text_area("Enter prompt for UI Design:")

if st.button("Generate UI Description"):
    if ui_prompt.strip():
        with st.spinner("Generating UI description..."):
            ui_description = generate_text_with_ollama(f"{UI_SYSTEM_PROMPT}\n\nUser Prompt:\n{ui_prompt}")
            st.session_state.ui_description = ui_description
        st.code(ui_description, language="text")
        st.success("✅ UI description generated!")

# ---------------- Step 4: Figma Preview ----------------
st.subheader("Figma UI Preview")
st.write("Use a Figma plugin (like Magician) to paste the above UI description and generate a frame.")
st.write("After generating the frame in Figma, paste the **preview image URL** below to continue:")

figma_url = st.text_input("Figma Preview Image URL")
if figma_url:
    st.session_state.figma_preview_url = figma_url
    st.image(figma_url, caption="Figma UI Preview")

# ---------------- Step 5: Create Jira Ticket ----------------
if st.session_state.editable_brd and st.session_state.figma_preview_url:
    if st.button("Create Jira Ticket"):
        with st.spinner("Creating Jira ticket..."):
            jira_description = f"{st.session_state.editable_brd}\n\nFigma Preview: {st.session_state.figma_preview_url}"
            ticket_id = create_jira_issue(st.session_state.summary_line, jira_description)
        st.success(f"✅ Jira ticket created: {ticket_id}")
