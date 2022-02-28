import unittest
from survey import AnnoymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_sigle_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnnoymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnnoymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()