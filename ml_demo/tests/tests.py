import unittest

from mage_ai.data_preparation.models.pipeline import Pipeline

class ExamplePipelineTest(unittest.TestCase):
    def test_pipeline_execution(self):
        ml_pipeline = Pipeline.get('ml_model_training')
        ml_pipeline.execute_sync()

        ml_prediction_pipeline = Pipeline.get('prediction')
        ml_prediction_pipeline.execute_sync()
