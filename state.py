from typing import TypedDict, List, Dict, Any, Optional

class EmailState(TypedDict):
    #incoing email details
    email : Dict[str, Any]

    #Emailclassification details
    email_category : Optional[str]
    spam_reason :Optional[str]
    is_spam: Optional[bool]

    #Generated email response
    email_draft : Optional[str]

    #Converstiion history
    messages: List[Dict[str , Any]]
