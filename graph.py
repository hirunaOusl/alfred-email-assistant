
from langgraph.graph import StateGraph, START, END

from state import EmailState
from nodes import (
    read_email,
    classify_email,
    route_email,
    handle_spam,
    draft_response
)


# Create the graph
builder = StateGraph(EmailState)


# Register nodes
builder.add_node("read_email", read_email)
builder.add_node("classify_email", classify_email)
builder.add_node("handle_spam", handle_spam)
builder.add_node("draft_response", draft_response)


# Connect normal edges
builder.add_edge(START, "read_email")
builder.add_edge("read_email", "classify_email")


# Add conditional routing
builder.add_conditional_edges(
    "classify_email",
    route_email,
    {
        "spam": "handle_spam",
        "legitimate": "draft_response"
    }
)


# Connect destination nodes to END
builder.add_edge("handle_spam", END)
builder.add_edge("draft_response", END)


# Compile graph
email_graph = builder.compile()
