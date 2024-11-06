 
import re
text = input()
text = re.sub(r'\.\.\.|!\?|!\!|\?\!', '', text)
sentence_endings = [".", "!", "?"]
sentence_count = sum([text.count(char) for char in sentence_endings])
print(sentence_count)