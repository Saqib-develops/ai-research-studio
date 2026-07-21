from typing import TypedDict, List, Dict, Any


class ResearchState(TypedDict):
    # User Input
    query: str
    depth: str

    # Planner Output
    plan: List[str]

    # Search Results
    search_results: List[Dict[str, Any]]

    # Research Papers
    papers: List[Dict[str, Any]]

    # Fact Checked Data
    verified_data: List[Dict[str, Any]]

    # Final Report
    report: str

    # Observability
    metrics: List[Dict[str, Any]]

    # Agent Logs
    logs: List[str]