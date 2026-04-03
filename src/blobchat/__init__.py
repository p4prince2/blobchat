"""Top-level package for blobchat."""


from .cleaner import ChatCleaner

def clean(text):
    return ChatCleaner().clean(text)