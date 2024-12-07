import pymorphy2

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
        print(normalized_text)
        for keyword in keywords:
            if keyword.lower() in normalized_text:
                return True
        return False

mes =[
  'Тверь и Пермь лес']



keywords = [
"Дубна",
"Калязин",
"Калязинский",
"Кашин",
"Кашинский",
"Кимрский",
"Кимры",
"Рамешки",
"Рамешковский",
"Талдом",
"Талдомский",
"Тверская",
"Тверь",
]
message_filter_service = MessageFilterService()
filtered_messages = []
for message in mes:
    if message_filter_service.contains_keywords(message, keywords):
        filtered_messages.append(message)
        
print(filtered_messages)