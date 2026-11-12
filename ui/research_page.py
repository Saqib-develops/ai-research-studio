import streamlit as st
from agents.supervisor import SupervisorAgent


def render_research():

    # ---------------- PAGE ---------------- #

    st.title("🤖 AI Research Studio")

    st.markdown("""
### Multi-Agent Research & Report Generation Platform

Powered by **Groq Llama 3.3 70B Versatile**, Prompt Engineering and Multi-Agent AI.
""")

    # ---------------- SIDEBAR ---------------- #

    with st.sidebar:

        st.title("🤖 AI Research Studio")

        st.divider()

        st.subheader("🤖 Agents")

        st.success("🧠 Planner")
        st.success("🌐 Research Agent")
        st.success("📚 Paper Analysis")
        st.success("✔ Fact Checker")
        st.success("✍ Writer")

        st.divider()

        st.subheader("🧩 Prompt Engineering")

        st.info("Zero Shot")
        st.info("One Shot")
        st.info("Few Shot")

        st.divider()

        st.subheader("🖥 Model")

        st.code("Llama 3.3 70B Versatile")

        st.caption("Version 1.0")

    # ---------------- INPUT ---------------- #

    topic = st.text_input(
        "🔍 Enter Research Topic",
        placeholder="Example: Quantum Computing"
    )

    depth = st.selectbox(
        "📚 Research Depth",
        [
            "Basic",
            "Standard",
            "Advanced"
        ]
    )

    supervisor = SupervisorAgent()

    # ---------------- BUTTON ---------------- #

    if st.button("🚀 Generate Research Report", use_container_width=True):

        if topic.strip() == "":
            st.warning("Please enter a research topic.")
            st.stop()

        state = {
            "query": topic,
            "depth": depth,
            "plan": [],
            "keywords": [],
            "search_results": [],
            "papers": "",
            "verified_data": "",
            "report": "",
            "metrics": [],
            "logs": []
        }

        # ---------------- RUN ---------------- #

        with st.spinner("🤖 AI Agents are working..."):

            state = supervisor.run(state)

        st.success("✅ Research Completed!")

        # ---------------- DETAILS ---------------- #

        st.info(f"""
### 📌 Research Details

**Topic:** {state['query']}

**Research Depth:** {state['depth']}

**Workflow**

Planner → Research Agent → Paper Analysis → Fact Checker → Writer
""")
       # st.write(state["keywords"])
       #st.write(state["search_results"])

        # ---------------- PLAN ---------------- #

        with st.expander("🧠 Research Plan"):

            for i, task in enumerate(state["plan"], start=1):
                st.write(f"**{i}.** {task}")

        # ---------------- TABS ---------------- #

        tab1, tab2, tab3 = st.tabs(
            [
                "📄 Research Report",
                "⚙ Agent Metrics",
                "📝 Execution Logs"
            ]
        )

        # ==========================================================
        # REPORT
        # ==========================================================

        with tab1:

            st.subheader("Generated Research Report")

            st.markdown("---")

            st.markdown(state["report"])

            st.markdown("---")

            st.download_button(
                "📥 Download Report",
                data=state["report"],
                file_name="Research_Report.md",
                mime="text/markdown",
                use_container_width=True
            )

        # ==========================================================
        # METRICS
        # ==========================================================

        with tab2:

            st.subheader("Agent Overview")

            if len(state["metrics"]) > 0:

                cols = st.columns(len(state["metrics"]))

                for col, metric in zip(cols, state["metrics"]):

                    with col:

                        st.metric(
                            metric["Agent"],
                            metric["Strategy"],
                            f"{metric['Latency (s)']} sec"
                        )

                st.divider()

                st.table(state["metrics"])

            else:

                st.warning("No metrics available.")

        # ==========================================================
        # LOGS
        # ==========================================================

        with tab3:

            st.subheader("Execution Logs")

            if len(state["logs"]) > 0:

                for log in state["logs"]:
                    st.write(log)

            else:

                st.warning("No logs available.")
            
    