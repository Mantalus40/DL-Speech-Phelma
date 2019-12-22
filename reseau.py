from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, Conv2DTranspose, MaxPooling2D, UpSampling2D, Reshape, ZeroPadding2D, Cropping2D


Xtrain = noised_spectrogrammes
Ytrain = clean_spectrogrammes
Xtest = test_noised_spectrogrammes
Ytest = test_clean_spectrogrammes

#Add the 4th dimension (one channel)
Xtrain = Xtrain.reshape(Xtrain.shape[0],Xtrain.shape[1],Xtrain.shape[2],1)
Ytrain = Ytrain.reshape(Ytrain.shape[0],Ytrain.shape[1],Ytrain.shape[2],1)
Xtest = Xtest.reshape(Xtest.shape[0],Xtest.shape[1],Xtest.shape[2],1)
Ytest = Ytest.reshape(Ytest.shape[0],Ytest.shape[1],Ytest.shape[2],1)

#Reshape data according to Keras expectations
Xtrain = np.transpose(Xtrain,(2,0,1,3))
Ytrain = np.transpose(Ytrain,(2,0,1,3))
Xtest = np.transpose(Xtest,(2,0,1,3))
Ytest = np.transpose(Ytest,(2,0,1,3))

#Delete the first zero-values spectrogram
Xtrain = Xtrain[1:,:,:,:]
Ytrain = Ytrain[1:,:,:,:]
Xtest = Xtest[1:,:,:,:]
Ytest = Ytest[1:,:,:,:]

##



input_shape = Xtrain.shape[1:]



model = Sequential()
model.add( Conv2D(filters=6,kernel_size=(6,6),activation='linear',padding='same',input_shape=input_shape) )
model.add( Conv2D(filters=4,kernel_size=(4,4),activation='sigmoid',padding='same') )
# model.add( MaxPooling2D(pool_size=(2,2)) )
# model.add( Conv2D(filters=4,kernel_size=(4,4),activation='sigmoid',padding='same') )
# # model.add( MaxPooling2D(pool_size=(2,2)) )
# # model.add( Conv2D(filters=5,kernel_size=(3,3),activation='tanh',padding='same') )
# model.add( MaxPooling2D(pool_size=(2,2)) )
# model.add( Conv2D(filters=3,kernel_size=(3,3),activation='sigmoid',padding='same') )


model.add( Conv2D(filters=1,kernel_size=(3,3),activation='tanh',padding='same') )
# model.add( UpSampling2D((2,2)) )
# model.add( Conv2D(filters=4,kernel_size=(4,4),activation='sigmoid',padding='same') )
# model.add( UpSampling2D((2,2)) )
# model.add( ZeroPadding2D(padding=(0,0)) )
# model.add( Cropping2D(cropping=((0,0),(0,0))) )
# model.add( Conv2D(filters=2,kernel_size=(5,5),activation='tanh',padding='same') )
# model.add( UpSampling2D((2,2)) )
# model.add( Conv2D(filters=1,kernel_size=(4,4),activation='sigmoid',padding='same') )
# model.add( ZeroPadding2D(padding=(1,1)) )
# model.add( Cropping2D(cropping=((1,0),(1,0))) )

model.summary()

model.compile(optimizer='rmsprop',loss='mean_squared_error')

history = model.fit(Xtrain,Ytrain,batch_size=500,epochs=4,verbose=1,validation_data=(Xtest,Ytest))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['train_error','test_error'])
plt.show()


# score = model.evaluate(Xtest,Ytest,batch_size=500)