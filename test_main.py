import unittest
from app import app
import pandas as pd
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_classify(self):
        with app.test_client() as client:
            row = pd.read_csv("data/fashion-mnist_test.csv").iloc[6].values
            img = row[1:].reshape(1,28,28)
            img = (img/255).tolist()

            result = client.post(
                '/classify',
                data=json.dumps({'image': img})
            )

            self.assertEqual(result.data,b'Bag')

if __name__ == '__main__':
    unittest.main()