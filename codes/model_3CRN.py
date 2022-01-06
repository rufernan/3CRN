
from tensorflow import keras



def model_3CRN(INPUT_SIZE, n_out=1):

    ts=3
    h1, h2, b1, b2, t1 = 32, 64, 64, 64, 256
    
    model_input = keras.Input(shape=INPUT_SIZE) # (None, rows, cols, bands, temp)
    x = model_input

    # H1
    x = keras.layers.Conv3D(h1, kernel_size=(3, 3, ts), strides=(1, 1, 1), padding="same", data_format='channels_last', input_shape=INPUT_SIZE)(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation('relu')(x)
    x = keras.layers.MaxPooling3D((2, 2, 1), strides=(1, 1, 1), padding='same', data_format='channels_last')(x)
    # H2
    x = keras.layers.Conv3D(h2, kernel_size=(3, 3, ts), strides=(1, 1, 1), padding="same", data_format='channels_last')(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation('relu')(x)
    x = keras.layers.MaxPooling3D((2, 2, 1), strides=(1, 1, 1), padding='same', data_format='channels_last')(x)

    # B1
    x = keras.layers.Conv3D(b1, kernel_size=(3, 3, ts), strides=(1, 1, 1), padding="same", data_format='channels_last')(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation('relu')(x)
    b1_1 = x
    x = keras.layers.Conv3D(b1, kernel_size=(3, 3, ts), strides=(1, 1, 1), padding="same", data_format='channels_last')(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation('relu')(x)
    x = keras.layers.MaxPooling3D((2, 2, 1), strides=(1, 1, 1), padding='same', data_format='channels_last')(x)
    b1 = x + b1_1
    
    # B2
    x = keras.layers.Conv3D(b2, kernel_size=(3, 3, ts), strides=(1, 1, 1), padding="same", data_format='channels_last')(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation('relu')(x)
    b2_1 = x
    x = keras.layers.Conv3D(b2, kernel_size=(3, 3, ts), strides=(1, 1, 1), padding="same", data_format='channels_last')(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation('relu')(x)
    x = keras.layers.MaxPooling3D((2, 2, 1), strides=(1, 1, 1), padding='same', data_format='channels_last')(x)
    b2 = x + b2_1
    
    # T1
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(t1)(x)
    x = keras.layers.BatchNormalization()(x)
    x = keras.layers.Activation('relu')(x)
    
    model_output = keras.layers.Dense(n_out, activation='linear')(x) # regression layer
    model = keras.Model(inputs=model_input, outputs=model_output)
    
    return model
   
   
