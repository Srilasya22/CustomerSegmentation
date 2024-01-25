"""
This is a boilerplate pipeline 'PCA'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node
from .nodes import pc

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(
           func=pc,
            inputs=["processed1_data","scaled_data"],
            outputs=None
            )
             ])
