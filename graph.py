
from langgraph.graph import StateGraph, START, END

from state import EmailState
from nodes import read_email


# Create the graph
builder = StateGraph(EmailState)

# Register the node
builder.add_node("read_email", read_email)

# Connect START to read_email
builder.add_edge(START, "read_email")

# Connect read_email to END
builder.add_edge("read_email", END)

# Compile the graph
email_graph = builder.compile()
