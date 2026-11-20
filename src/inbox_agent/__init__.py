from . import auth
from googleapiclient.discovery import build


def main() -> None:
    creds = auth.get_credentials()
    service = build("gmail", "v1", credentials=creds)
    profile = service.users().getProfile(userId="me").execute()
    print("emails: ", profile["emailAddress"], "messages: ", profile["messagesTotal"])

    result = service.users().messages().list(userId="me", maxResults=10).execute()

    for m in result.get("messages", []):
        print(m["id"])
