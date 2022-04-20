#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
def run_inference(model_path, topredict):
    import numpy as np
    import tflite_runtime.interpreter as tflite
    interpreter = tflite.Interpreter(model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape)*0 + float(topredict), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print("input data: " , input_data,"output data:" , output_data)
if __name__ == '__main__':
    run_inference(sys.argv[1], sys.argv[2])
    
#How to run programm in terminal:
#Go to the directory tflite: cd tflite
#run programm: python run_Inference.py saved_Five_step_example.tflite 8.0
# In[ ]:




