from state import EmailState

def read_email(state: EmailState)-> dict:
    """Read the incoming email from the workflow state."""

    email = state["email"]

    sender = email["sender"]
    subject = email["subject"]
    body = email["body"]

    print("Alfred received a new email")
    print(f"Sender:{sender}")
    print(f"Subject:{subject}")
    print(f"Body:{body}")

    return{
        "messages": state["messages"]+[
            {
                "role": "system",
                "content": f"Email received from {sender}"
            }
        ]
    }
