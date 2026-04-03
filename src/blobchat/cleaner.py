import re
from .slang_dict import CHAT_DICT

class ChatCleaner:
    
    def __init__(self):
        self.slang = CHAT_DICT

    def expand_slang(self, text):
        words = text.split()
        return " ".join([self.slang.get(w.lower(), w) for w in words])

    def remove_repeated_chars(self, text):
        return re.sub(r"(.)\1{2,}", r"\1\1", text)

    def remove_noise(self, text):
        text = re.sub(r"<.*?>", "", text)
        text = re.sub(r"[^\w\s]", "", text)
        return text

    def clean(self, text):
        text = self.expand_slang(text)
        text = self.remove_repeated_chars(text)
        text = self.remove_noise(text)
        return text.lower()