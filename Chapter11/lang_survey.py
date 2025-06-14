from survey import AnonymousSurvey

lang_survey = AnonymousSurvey(
    'What language did you first learn how to speak?')

lang_survey.show_question()

print("Type 'q' at any time to quit.")
while True:
    new_response = input("Answer: ")
    if new_response == 'q':
        break
    lang_survey.store_response(new_response)

print('\nThank you to everyone who responded!')
print("\nSurvey Results:")
lang_survey.show_respones()
