import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")


class GraphState(TypedDict):
    prompt: str
    response: str


def _call_ollama(state: GraphState) -> GraphState:
    llm = ChatOllama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
    result = llm.invoke([HumanMessage(content=state["prompt"])])

    return {"prompt": state["prompt"], "response": result.content}


def _build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("call_ollama", _call_ollama)
    graph.add_edge(START, "call_ollama")
    graph.add_edge("call_ollama", END)

    return graph.compile()


_graph = _build_graph()

async def send_prompt(prompt: str) -> str:
    result = await _graph.ainvoke({"prompt": prompt, "response": ""})

    return result["response"]
