
words = 'hello word school Python php go hi C'
stop = ['Python', 'php', 'go', 'C']

print(' '.join([word for word in words.split() if word not in stop]))

