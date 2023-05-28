# Model Training Lib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam

from data_preprocessing import preprocess_train_data

def train_bot_model(train_x, train_y):
    


    

# Calling Methods to Train Model
train_x, train_y = preprocess_train_data()

train_bot_model(train_x, train_y)

