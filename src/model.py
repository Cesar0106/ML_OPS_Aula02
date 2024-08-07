import pickle

def load_model():
    with open(r'C:\Users\cesar\OneDrive\Desktop\Insper\Eletivas\ml_ops\Aula2\models\model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def load_encoder():
    with open(r'C:\Users\cesar\OneDrive\Desktop\Insper\Eletivas\ml_ops\Aula2\models\model.pkl', 'rb') as file:
        encoder = pickle.load(file)
    return encoder