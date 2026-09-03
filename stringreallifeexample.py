statement = "arnav is writing a book titled 'python made easy'. His book is expected to release in March"
sentence_list = statement.split('.')
print(sentence_list)

statement = statement.replace("arnav", "Arnav")
print(statement)

statement = statement.replace("python made easy", "python made easy".title())
print(statement)

reschedule_date = "April"
statement = statement.replace("March", reschedule_date)