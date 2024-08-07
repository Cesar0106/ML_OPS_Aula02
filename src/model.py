import pickle

def load_model():
    with open('API/models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def load_encoder():
    with open('API/models/ohe.pkl', 'rb') as file:
        encoder = pickle.load(file)
    return encoder