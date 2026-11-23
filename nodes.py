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


def classify_email(state: EmailState) -> dict:
    """Classify incoming email as spam or legitimate."""

    email = state["email"]
    subject = email["subject"].lower()
    body = email["body"].lower()

    spam_keywords = [
        "win money",
        "claim your prize",
        "free gift",
        "click here",
        "urgent payment"
    ]

    email_text = subject + " " + body

    for keyword in spam_keywords:
        if keyword in email_text:
            return {
                "is_spam": True,
                "spam_reason": f"Suspicious keyword detected: {keyword}"
            }

    return {
        "is_spam": False,
        "spam_reason": None
    }

def route_email(state: EmailState) -> str:
    """Route email based on spam classification."""

    if state["is_spam"]:
        return "spam"

    return "legitimate"


def handle_spam(state: EmailState) -> dict:
    """Handle an email classified as spam."""

    print("Alfred detected a spam email.")
    print(f"Reason: {state['spam_reason']}")

    return {
        "messages": state["messages"] + [
            {
                "role": "system",
                "content": "Spam email detected and flagged."
            }
        ]
    }


def draft_response(state: EmailState) -> dict:
    """Create a response draft for a legitimate email."""

    email = state["email"]

    print("Alfred is preparing a response...")
    
    draft = (
        f"Hello,\n\n"
        f"Thank you for your email regarding '{email['subject']}'.\n\n"
        f"We will get back to you soon.\n\n"
        f"Best regards"
    )

    return {
        "email_draft": draft
    }

def categorize_email(state: EmailState) -> dict:
    """Categorize a legitimate email."""

    email = state["email"]

    subject = email["subject"].lower()
    body = email["body"].lower()

    email_text = subject + " " + body

    if any(word in email_text for word in ["invoice", "payment", "bank", "billing"]):
        category = "Finance"

    elif any(word in email_text for word in ["meeting", "project", "office", "work"]):
        category = "Work"

    elif any(word in email_text for word in ["help", "issue", "problem", "support"]):
        category = "Support"

    elif any(word in email_text for word in ["friend", "family", "birthday", "personal"]):
        category = "Personal"

    else:
        category = "Other"

    print(f"Email category: {category}")

    return {
        "email_category": category
    }

