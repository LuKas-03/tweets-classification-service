import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_URL(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r' ',text)

# убрать HTML разметку
def remove_html(text):
    html=re.compile(r'<.*?>')
    return html.sub(r' ',text)

def remove_mail(text):
    mail=re.compile(r'^([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})$')
    return mail.sub(r' ',text)

# убрать эмодзи
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r' ', text)

def join_list(tab):
    return " ".join(tab)

def tokenize(text):
    stop_words = set(stopwords.words("russian"))

    text = remove_html(text)
    text = remove_URL(text)
    text = remove_emoji(text)
    text = remove_mail(text)
    text = text.lower()
    #text = re.sub("[^а-яёйa-z0-9]", " ", text)
    #text = re.sub("\s+", " ", text)
    text = word_tokenize(text)
    text = [word for word in text if word.isalpha()]
    text = [word for word in text if not word in stop_words]
    
    #text = [lemmatizer.lemmatize(word) for word in text]
    
    return " ".join(text)