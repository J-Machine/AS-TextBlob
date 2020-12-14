from textblob import TextBlob

text = "As an employer that promotes the benefits of a diverse workforce, DOL recognizes that employees who speak languages other than English may wish to communicate in another language outside of performing their job duties, such as in casual conversations with coworkers or while engaged in personal matters."


blob = TextBlob(text)
tags = blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

phrases = blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
print(tags)
print("\n")
print(phrases)

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)