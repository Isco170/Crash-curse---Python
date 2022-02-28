import unittest
from survey import AnnoymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_sigle_response(self):
        question = "What language did you first learn to speak? "
        my_survey = AnnoymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
    unittest.main()