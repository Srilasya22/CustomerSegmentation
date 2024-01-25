"""
This is a boilerplate pipeline 'Testing'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node

from .nodes import test
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline( [node(func=test,
            inputs="processed1_data",
            outputs=None)]
            )
