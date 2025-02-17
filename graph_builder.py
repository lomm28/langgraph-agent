from calculator import calculator
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState, StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

class GraphBuilder:
    initial_messages = [SystemMessage(content="You are a helpful assistant that can answer questions and do math.")]
    graph = None

    def __init__(self, model: str, temperature: float):
        llm = ChatOpenAI(model=model, temperature=temperature)
        self.llm = llm.bind_tools([calculator])

    def assistant(self, state: MessagesState):
        return {"messages": [self.llm.invoke(self.initial_messages + state["messages"])]}
    
    def build_graph(self):
        builder = StateGraph(MessagesState)
        builder.add_node("assistant", self.assistant)
        builder.add_node("tools", ToolNode([calculator]))   
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges("assistant", tools_condition)
        builder.add_edge("tools", "assistant")
        self.graph = builder.compile()

    def add_message(self, message):
        self.initial_messages.append(message)