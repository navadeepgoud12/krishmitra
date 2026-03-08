from Backend.exception.exception import Krishmitra
from Backend.logger.logger import logging
import os
import shutil
import random
import sys

class DataIngestion:

    def __init__(self):
        self.dataset_path = "Backend/disease_prediction/dataset/raw"
        self.train_path = "artifacts/train"
        self.test_path = "artifacts/test"
        self.split_ratio = 0.8

    def split_dataset(self):
        try:
            for folder in os.listdir(self.dataset_path):

                folder_path = os.path.join(self.dataset_path, folder)

                images = os.listdir(folder_path)

                random.shuffle(images)

                split_index = int(len(images) * self.split_ratio)

                train_images = images[:split_index]
                test_images = images[split_index:]

                os.makedirs(os.path.join(self.train_path, folder), exist_ok=True)
                os.makedirs(os.path.join(self.test_path, folder), exist_ok=True)

                for img in train_images:
                    shutil.copy(
                        os.path.join(folder_path, img),
                        os.path.join(self.train_path, folder, img)
                    )

                for img in test_images:
                    shutil.copy(
                        os.path.join(folder_path, img),
                        os.path.join(self.test_path, folder, img)
                    )

            print("Data Ingestion Completed")
        except Exception as e:
            raise Krishmitra(e,sys)