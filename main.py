from input_module import reader
from data_processing_module import processor
from consolidation_module import consolidator
from output_module import exporter

if __name__ == "__main__":
    statements = reader.read_csv_files_in_directory()
    processed_statements = processor.process_statements(statements)
    consolidated_statement = consolidator.consolidate_statements(processed_statements)
    exporter.export_statement(consolidated_statement)