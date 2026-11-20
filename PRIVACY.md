# Privacy

Inbox Agent runs on your own computer. There is no server and no account with
me. I never see your email, your sign-in or anything the agent does.

## What it can access

It signs in to your Gmail with Google's OAuth. Right now it asks for read-only
access. Later steps ask for permission to add labels and write drafts. Google
has no permission that covers only labels and drafts, so the broader one also
allows sending mail and moving it to the trash. The code itself only allows
labels and drafts.

## Where your data goes

- **Google.** The agent reads your mail through the Gmail API.
- **Anthropic, from step 2.** Mail the rules can't sort is sent to the
  Anthropic API so a model can pick a label. Anthropic's API terms apply to
  that text.
- **Telegram, from step 1.** An important email triggers a short message to
  your own Telegram bot naming the sender. It never includes the email's body
  or links.

Nothing else leaves your machine. No analytics, no tracking.

## What it stores

Your sign-in token and Google client file stay in a folder on your computer
that only your user account can read. Labels and drafts it creates live in
your Gmail.

## Turning it off

Remove Inbox Agent under Google Account → Security → Third-party apps with
account access, and delete the token file. That ends its access.

## Questions

Open an issue on this repository.
