### The BuzzWord

----

* Type : Knowledge and Reference
* Invocation Name : Tech Word Finder
* Skill Name : The BuzzWord

----

#### Skill Description

The skill's target audience are those new techies who are keen to learn new terms of their world and want to grow their 
knowledge Base. Also people with an interest in the booming technology can have a gist of the new terms using this skill.
The skill generates a new word (randomly) everytime we ask for it. A new term adn a precise definition capturing the crux of
that term is presented. 

----

#### Intent Schema 

```json
{
  "intents": [
    {
      "intent": "knowWordIntent"
    },
    {
      "intent": "AMAZON.HelpIntent"
    },
    {
      "intent": "AMAZON.StopIntent"
    },
    {
      "intent": "AMAZON.CancelIntent"
    }
  ]
}
```

----

#### Sample Utterances

```
knowWordIntent Tell Me a word
knowWordIntent New Word
knowWordIntent Tell me something new
knowWordIntent What's new
knowWordIntent yes
knowWordIntent yepp
knowWordIntent Tell me
knowWordIntent Tell me a new Tech Term
knowWordIntent Another
knowWordIntent more
knowWordIntent today's word
knowWordIntent get the word of the day
AMAZON.HelpIntent Help
AMAZON.StopIntent Stop
AMAZON.CancelIntent cancel
```

-----

#### Lmabda Function

The Lambda function is written inpython and hosted on AWS.

[Here is the full code for the same][https://github.com/DEEZZU/ALEXA_SKILL/blob/master/LambdaFunction_TechWordoo.py]

_The main Logic of my Lambda function :_

