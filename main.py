from pipeline import Pipeline
from input_module.reader import Reader
from data_processing_module.processor import Processor
from consolidation_module.consolidator import Consolidator
from output_module.exporter import Exporter

if __name__ == "__main__":
    pipeline = Pipeline([
        Reader(),
        Processor(),
        Consolidator(),
        Exporter()
    ])
    pipeline.process(None)