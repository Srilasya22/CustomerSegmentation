"""
This is a boilerplate pipeline 'Clustering'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node
from .nodes import cluster

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(
        func=cluster,
        inputs=["processed_data","scaled_data"],
        outputs="processed1_data"
    )])
