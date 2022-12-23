# Learn German

A spaced-repitition gamified German learning app. In early development.


## Background

This project began as a text file containing ~3000 common German words and an idea to create a language learning app utilising the grammar-translation method.

## Current Version And How to Use

Version 0.1.0.0 is a very basic command-line game. From a list of common German nouns, the user is prompted to identify whether it is masculine, feminine or neuter.

It includes a scoring and health/lives system, and a leaderboard.

Further exercises and a frontend website are in development. Watch this space.

### How to use

Download the german.py and german.db files into a folder. Navigate to the folder in a Terminal window and run:  

    python3 german.py


## Current and Future Development

Nouns have been categorised into gender in the SQL database. Further categorisation is necessary to develop sentences for users to identify features such as grammatical case. 

The pool of words should also be reduced.

Nouns will be categorised as follows:

* Whether or not the gender adheres to a general rule, or is an exception to a rule


* Whether the plural form adheres to a general rule


* A fully fleshed back- and frontend utilising Flask, Bootstrap etc. Individual user scores. Animations and custom CSS. 


## Why? A different approach to learning

Most gamified language learning applications primarily utilise a phrase-translation method, where users are prompted to translate sentences from their target language to their native language (and vice versa). Some have questioned the efficacy of this method. Extensive evidence shows that more immersive approaches lead to faster language acquisition. That is to say, students have more success when they attempt to *think in their target language*.

Moreover, the approach taken by many applications can arguably lead to other, more important language features being undertrained. Particularly overlooked are grammar rules, which are important for fluid, accurate and confident communication. 

In contrast to phrase-translation methods, the grammar-translation method focusses more heavily on understanding the grammar features of the target language. This method, which originated in the 16th century and has been used frequently since the 19th century, is under-utilised in gamified learning applications. 

German's grammatical complexity makes it a particularly suitable language for this approach.


## German's Grammatical Features Make it Difficult

German is a relatively difficult language to learn. The US Foreign Service Institute, which has extensive experience educating diplomats in languages, rates German as a Category II, medium difficulty language for Enlish native speakers to learn. 

Compared to languages such as French, Italian, Spanish, Swedish and Dutch (which are considered more similar to English) German requires an average of 50% more study-hours to reach professional proficiency.

Dutch, by contrast, is rated Category I. German and Dutch are closely related. They share approximately 70& lexical similarity, with a large number of cognates and similarities in syntax. So why is German so much more difficult than Dutch?

A comparison of the two languages' grammatical features helps to contextualise this.

German has:

* 4 Grammatical cases
Nominative, accusitive, genitive, dative.


* 3 noun genders and a plural form
Masculine, feminine, neuter and plural.


* Definite and indefinite articles that vary based on noun gender **and** grammatical case

This means that there are essentially 12 versions of the German word for 'the' and 12 versions of the word for 'a/an'. 


* Complicated Plural Suffixes

English plural nouns usually take the suffix 's' (one cat => two cats; one dog => two dogs), with a few exceptions (one sheep => two sheep). 

German has six different plural suffix possiblilities:
    1. No change
    2. Add e
    3. Add e and umlaut
    4. Add s
    5. Add er and umlaut
    6. Add (e)n


* Declensions

If memorising 24 definite and indefinite articles isn't difficult enough, there are also adjective declensions to remember!


* Confusing Word Order



## For every rule, an exception

Thankfully, there are patterns and rules which simplify the learning process. But of course there exceptions to many rules!

This project aims to create an application teaches users to understand and recognise the 4 grammatical cases, various grammar rules *and their exceptions*. 



## Future Future Development 

* Machine learning and data analysis to identify the most effective learning patterns. 

* Algorithm development to personalise spaced-repetition and difficulty to each user's progress
