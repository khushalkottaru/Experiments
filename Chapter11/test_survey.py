from survey import AnonymousSurvey


def test_store_single_response():
    '''Checks that a single response is stored correctly.'''
    lang_survey = AnonymousSurvey('What language did you first learn?')
    lang_survey.store_response('English')
    assert 'English' in lang_survey.responses


def test_store_multiple_individual_responses():
    '''Test if responses from multiple different people are stored correctly.'''
    lang_survey = AnonymousSurvey('What language did you first leanr?')
    for response in ['English', 'Spanish', 'Mandarin']:
        lang_survey.store_response(response)
    for response in ['English', 'Spanish', 'Mandarin']:
        assert response in lang_survey.responses
