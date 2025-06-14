class AnonymousSurvey:
    '''Collect anonymous answers to a survey question.'''

    def __init__(self, question):
        '''Store a question, prepare for responses.'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Show the survey question.'''
        print(self.question)

    def store_response(self, new_response):
        '''Stores a response.'''
        self.responses.append(new_response)

    def show_respones(self):
        '''Displays all responses.'''
        for response in self.responses:
            print(f'-{response}')
