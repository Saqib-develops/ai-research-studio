from agents.base_agent import BaseAgent
from services.groq_service import GroqService

SYSTEM_PROMPT = """
You are a Senior Research Analyst.

Generate a professional research report.

The report MUST contain the following sections in Markdown format.

# Executive Summary

Provide a concise overview.

# Introduction

Explain the topic.

# Research Objectives

State the goals of the research.

# Key Findings

Use bullet points.

# Current Trends

Discuss the latest developments.

# Applications

Use bullet points.

# Challenges

Explain limitations and issues.

# Future Scope

Describe upcoming opportunities.

# Conclusion

Summarize the report.

Formatting Rules

- Use Markdown headings.
- Use bullet points where appropriate.
- Keep paragraphs concise.
- Write in a professional tone.
- Do NOT mention that you are an AI.
"""


class WriterAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Writer",
            "Few Shot"
        )

        self.llm = GroqService()

    def run(self, state):

        start = self.before_run(state)

    # ---------------- Research Plan ---------------- #

        plan_text = "\n".join(
            [f"{i+1}. {task}" for i, task in enumerate(state["plan"])]
        )

        # ---------------- Keywords ---------------- #

        keywords_text = ", ".join(state.get("keywords", []))

    # ---------------- Search Results ---------------- #

        search_text = ""

        if state["search_results"]:

            for item in state["search_results"]:

                search_text += f"""
==================================================

TITLE
{item['title']}

SUMMARY
{item['body']}

SOURCE
{item['url']}

==================================================

"""

        else:

            search_text = "No search results available."

    # ---------------- Context ---------------- #

        context = f"""
Research Topic
--------------
{state["query"]}

Research Keywords
-----------------
{keywords_text}

Research Plan
-------------
{plan_text}

Research Findings
-----------------
{search_text}

Paper Analysis
--------------
{state["papers"]}

Verified Information
--------------------
{state["verified_data"]}
"""

        report = self.llm.generate_response(

            prompt=context,

            system_prompt=SYSTEM_PROMPT,

            temperature=0.4

        )

        state["report"] = report

        self.after_run(state, start)

        return state