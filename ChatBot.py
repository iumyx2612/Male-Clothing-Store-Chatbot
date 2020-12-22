import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import json

tokenizer = Tokenizer(oov_token="<OOV>")

max_len = 30
_padding = "post"
_truncating = "post"

labels = []
sentences = []
label_sentence = []

with open("intents.json", 'rb') as f:
    data = json.load(f)

for intent in data["intents"]:
    if intent["tag"] not in labels:
        labels.append(intent["tag"])
    for pattern in intent["inputs"]:
        sentences.append(pattern)
        label_sentence.append(intent["tag"])

tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, maxlen=max_len, padding=_padding, truncating=_truncating)

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
enc.fit(label_sentence)
label_sentence = enc.transform(label_sentence)

input_dim = 106
print(len(word_index))
output_dim = 32
classes = len(labels)

'''model = keras.models.Sequential([
    keras.layers.Embedding(input_dim, output_dim, input_length=max_len),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(classes, activation='softmax')
])

model.summary()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(padded, label_sentence, epochs=500, verbose=2, validation_split=0.1)
model.save("Chat Bot Model")
'''

def Response(user_input):
    pass

def _Chat():
    pass

def Chat(user_input):
    model = keras.models.load_model("Chat Bot Model")
    model.summary()
    while True:
        string = input('Enter: ')
        if string.lower() == 'quit':
            break
        input_sequences = tokenizer.texts_to_sequences([string])
        padded_input = keras.preprocessing.sequence.pad_sequences(input_sequences, maxlen=max_len, padding=_padding,
                                                                  truncating=_truncating)
        predict = model.predict(padded_input)
        print(predict)
        predict = predict[0]
        print(np.argmax(predict))
        if predict[np.argmax(predict)] > 0.7:
            category = enc.inverse_transform([np.argmax(predict)])
            print(category)
            for i in data["intents"]:
                if i["tag"] == category:
                    print(np.random.choice(i["responses"]))
        else:
            print("Sorry I don't get it")



