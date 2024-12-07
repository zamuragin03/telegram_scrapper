from Config import Repository, client
from .MessageFilterService import MessageFilterService
class KeywordService:
    def GetAllKeywords():
        words = Repository.get_all_keywords()
        text = ''
        for word  in words:
            text+=f'{word[0]}. "{word[1]}" \n'
        return text  
    def GetAllPlainKeywords():
        return [el[1] for el in Repository.get_all_keywords()]
    
    def AddNewKeyWord(keyword):
        return Repository.add_keyword(keyword)
    
    def RemoveKeywordById(id):
        return Repository.delete_keyword(id)
        
    async def FilterMessage(messages):
        keywords = KeywordService.GetAllPlainKeywords()
        message_filter_service = MessageFilterService()
        filtered_messages = []
        for message in messages:
            if message_filter_service.contains_keywords(message.text, keywords):
                async with client:
                    print(message)
                    sender = await client.get_entity(message.peer_id)
                filtered_messages.append({
                    'message':message,
                    'entity':sender
                    }) 
        return filtered_messages

