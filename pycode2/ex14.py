#prompting the user and passing
"""
Usage:
      ex14.py <username>
"""
from sys import argv

script, user = argv
prompt = '$> '

print "Hi %s, I'm in the %s script" % (user, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user
likes = raw_input(prompt)

print"Where do you live %s?"
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
