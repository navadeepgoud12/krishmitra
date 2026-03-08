from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

class ModelTrainer:

    def train(self, train_data, test_data):

        model = Sequential()

        model.add(Conv2D(32,(3,3),activation='relu',input_shape=(128,128,3)))
        model.add(MaxPooling2D(2,2))

        model.add(Conv2D(64,(3,3),activation='relu'))
        model.add(MaxPooling2D(2,2))

        model.add(Conv2D(128,(3,3),activation='relu'))
        model.add(MaxPooling2D(2,2))

        model.add(Flatten())

        model.add(Dense(128,activation='relu'))

        model.add(Dense(train_data.num_classes,activation='softmax'))

        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        model.fit(
            train_data,
            validation_data=test_data,
            epochs=10
        )

        model.save("final_model/disease_model.h5")
        import json

        with open("final_model/class_indices.json", "w") as f:
            json.dump(train_data.class_indices, f)

    

        print("Model Training Completed")

    