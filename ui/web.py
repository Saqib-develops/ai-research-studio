
def render_web():
    import streamlit as st
    import sys
    from pathlib import Path
    from prompts.prompt_builder import PromptBuilder
    from services.groq_service import GroqService
    from config import TEMPERATURE

    BASE_DIR = Path(__file__).parent.parent
    #TEMPLATE_DIR = BASE_DIR / "prompts" / "template"
    #templates = list(TEMPLATE_DIR.glob("*.py"))
    #print(templates)
    sys.path.append(str(BASE_DIR))
    from prompts.template.zero_shot import ZeroShotPrompt

    OPTIONS = {
       "Zero Shot" : ZeroShotPrompt
    }

    st.set_page_config(
       page_title="Prompt Lab",
       layout='wide'
    )

    st.title("Prompt Engineering lab")
    st.write("Learn Prompt Engineering by doing")

#select type of prompt
    prompt_type = st.selectbox(
      "select Prompt Technique",
       OPTIONS
    )

    user_prompt = st.text_area("Enter the prompt", height=150)
    temperate = st.slider("Temperature Range:", min_value=float(TEMPERATURE),max_value=1.0)
    
    if st.button("Generate Response"):
        if user_prompt.strip() =="":
            st.warning("Please Enter the Prompt")
        else:
            final_prompt = PromptBuilder.build(prompt_type,user_prompt)
            groq = GroqService()
            response = groq.generate_response(final_prompt,temperate)

            st.subheader("Generated Prompt")
            st.code(final_prompt)
            st.subheader("Groq Response")
            st.write(response)

