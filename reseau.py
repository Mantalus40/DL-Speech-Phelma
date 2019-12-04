from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, Conv2DTranspose, MaxPooling2D




Xtrain = noised_spectrogrammes
Ytrain =  clean_spectrogrammes
#Xtest, Ytest
input_shape = (257,None,1)



model = Sequential()
model.add( Conv2D(filters=3,kernel_size=(5,5),activation='relu',input_shape=input_shape) )
model.add( MaxPooling2D(pool_size=(2,2)) )
model.add( Conv2D(filters=4,kernel_size=(4,4),activation='relu') )
model.add( MaxPooling2D(pool_size=(2,2)) )
model.add( Conv2D(filters=6,kernel_size=(3,3),activation='relu') )
model.add( MaxPooling2D(pool_size=(2,2)) )

model.add( Conv2DTranspose(filters=6,kernel_size=(3,3),activation='relu') )
model.add( Conv2DTranspose(filters=4,kernel_size=(4,4),activation='relu') )
model.add( Conv2DTranspose(filters=3,kernel_size=(5,5),activation='relu') )


model.compile(optimizer='sgd',loss='mean_squared_error')

model.fit(Xtrain,Ytrain,batch_size=500,epochs=5,verbose=1,validation_data=(Xtest,Ytest))

