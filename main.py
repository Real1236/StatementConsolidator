from pipeline import Pipeline
from input_module import reader
from data_processing_module import processor
from consolidation_module import consolidator
from output_module import exporter

if __name__ == "__main__":
    pipeline = Pipeline([
        reader,
        processor,
        consolidator,
        exporter
    ])
    pipeline.process(None)