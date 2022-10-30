from better_profanity import profanity
text = input("Enter a sentence to check: ")
censored = profanity.censor(text)
print(censored)

