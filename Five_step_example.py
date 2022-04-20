#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units =1,input_shape=[1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')
xs = np.array([-1.0,0.0,1.0,2.0,3.0,4.0], dtype = float)
ys = np.array([-2.0, 1.0,4.0,7.0,10.0,13.0], dtype=float)
model.fit(xs, ys, epochs=500)


# In[4]:


# Save the entire model as a SavedModel.
#!mkdir -p Five_step_example
#model.save('Five_step_example/my_model')


# In[5]:


#new_model = tf.keras.models.load_model('Five_step_example/my_model')
# Check its architecture
#new_model.summary()


# In[6]:


# Convert the model
#converter = tf.lite.TFLiteConverter.from_saved_model('Five_step_example/my_model') # path to the SavedModel directory
#tflite_model = converter.convert()

# Save the model.
#with open('saved_Five_step_example.tflite', 'wb') as f:
#    f.write(tflite_model)


# In[ ]:





# In[ ]:




