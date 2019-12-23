import nltk, string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings

warnings.filterwarnings("ignore")
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


'''remove punctuation, lowercase, stem'''


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new = new + ' ' + x

        # return string
    return new


def stop_word(test):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(test)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    filtered_sentence = convert(filtered_sentence)
    return filtered_sentence


def cosine_sim(text1, text2):
    text1 = stop_word(text1)
    text2 = stop_word(text2)
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


ans = ['abstraction, encapsulation, inheritance, and polymorphism',
       'Primary data types: These are fundamental data types in C namely integer(int), floating point(float), character(char) and void. Derived data types: Derived data types are nothing but primary datatypes but a little twisted or grouped together like array, stucture, union and pointer.,' \
       'Integer,Floating point type,Character type,void,Double',
       'Python is a programming language with objects, modules, threads, exceptions and automatic memory management. The benefits of pythons are that it is simple and easy, portable, extensible, build-in data structure and it is an open source',
       'A fully object-oriented language needs to have all the 4 oops concepts. In addition to that, all predefined and, user-defined types must be objects and, all the operations should be performed only by calling the methods of a class.' \
       'Though java follows all the four object-oriented concepts,Java has predefined primitive data types (which are not objects).You can access the members of a static class without creating an object of it.',
       'Waterfall model,Incremental Approach,V-model,Agile model,Spiral model']

result=[]
def function(javab):
    result.append(cosine_sim(ans[0], javab[0]) * 100)
    result.append(cosine_sim(ans[1], javab[1]) * 100)
    result.append(cosine_sim(ans[2], javab[2]) * 100)
    result.append(cosine_sim(ans[3], javab[3]) * 100)
    result.append(cosine_sim(ans[4], javab[4]) * 100)
    return result
# print(cosine_sim(str1,str2)*100)
