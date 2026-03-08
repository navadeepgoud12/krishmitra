from tensorflow.keras.preprocessing.image import ImageDataGenerator

class DataTransformation:

    def __init__(self):

        self.train_path = "artifacts/train"
        self.test_path = "artifacts/test"

    def transform(self):

        train_gen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            zoom_range=0.2,
            horizontal_flip=True
        )

        test_gen = ImageDataGenerator(rescale=1./255)

        train_data = train_gen.flow_from_directory(
            self.train_path,
            target_size=(128,128),
            batch_size=32,
            class_mode='categorical'
        )

        test_data = test_gen.flow_from_directory(
            self.test_path,
            target_size=(128,128),
            batch_size=32,
            class_mode='categorical'
        )

        return train_data, test_data