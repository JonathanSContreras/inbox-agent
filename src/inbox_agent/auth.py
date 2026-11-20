import os
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.exceptions import RefreshError

CONFIG_DIR = Path(
    os.environ.get("INBOX_AGENT_DIR", "~/.config/inbox-agent")
).expanduser()
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """

    client_secrets_path = CONFIG_DIR / "client_secret.json"
    token_path = CONFIG_DIR / "token.json"
    creds = None
    if token_path.exists():  # 1. load whats saved
        creds = Credentials.from_authorized_user_file(token_path)
        if not creds.has_scopes(SCOPES):
            creds = None  # granted scopes don't cover what we need: sign in again
    if creds and creds.expired and creds.refresh_token:  # 2. quiet renewal
        try:
            creds.refresh(Request())
        except RefreshError as e:
            print(f"Error refreshing credentials: {e}")
            creds = None  # refresh failed: sign in again
    if not creds or not creds.valid:  # 3. anything left over: sign in
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_path, SCOPES)
        creds = flow.run_local_server(port=0)

    # 4. save
    fd = os.open(token_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as token:
        token.write(creds.to_json())

    return creds
