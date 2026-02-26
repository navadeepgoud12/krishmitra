from dataclasses import dataclass


#data class for the dataingestion
@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str

