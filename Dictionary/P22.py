# 22.	Find if "Python" is a subject in a course dictionary.
# Answer:
# User provides subject:info pairs and we check for "Python".

pairs = input("Enter subject:info pairs comma separated: ")
courses = dict((p.split(':')[0].strip(), p.split(':')[1].strip()) for p in pairs.split(',') if p.strip())
print("Python is a subject?" , "Python" in courses)
