import pymorphy2
import datetime
class MessageFilterService:
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
    
    def normalize_text(self, text):
        if text is None:
            return ''
        words = text.split()
        normalized_words = [self.morph.parse(word)[0].normal_form for word in words]
        return ' '.join(normalized_words)
    
    def contains_keywords(self, text, keywords):
        normalized_text = self.normalize_text(text)
        for keyword in keywords:
            if keyword.lower() in normalized_text:
                return True
        return False



class ParseMessagesService:
    @staticmethod
    def FilterLastMinuteMessages(message):
        now = datetime.datetime.now(tz=message.date.tzinfo)
        time_difference = now - message.date
        return time_difference.total_seconds() < 60