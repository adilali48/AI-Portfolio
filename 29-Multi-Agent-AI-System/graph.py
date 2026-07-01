from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents import research_agent, coding_agent


class AgentState(TypedDict):
    query: str
    research: str
    code: str


def research_node(state):
    print("\n🔍 Research Agent Working...")

    result = research_agent(state["query"])

    return {
        "research": result
    }


def coding_node(state):
    print("\n💻 Coding Agent Working...")

    result = coding_agent(state["query"])

    return {
        "code": result
    }


builder = StateGraph(AgentState)

builder.add_node("Research", research_node)
builder.add_node("Coding", coding_node)

builder.set_entry_point("Research")

builder.add_edge("Research", "Coding")
builder.add_edge("Coding", END)

graph = builder.compile()