# tflite
Tutorial on how to convert Tensorflow model to Tensorflow lite in order to run Tensorflow code on the IOT2050.

Five steps: Detailed explanation: [tfliteIOT_SE.pptx](https://github.com/ArijanaBohr/tflite/files/8548443/tfliteIOT_SE.pptx)


Step 1: Create Model
                  
    Example Model's task: Learn the relationship between X and Y. After having trained the model it should predict Y for a given X. (It will be an approximative value)

Step 2: Save Model

Step 3: Convert Model from Tensorflow to Tensorflow lite

Step 4: Get Code to the IOT
    
    The only files you need to get to your IOT is the .tflite file and the run_Inference.py file.

Step 5: Run Inference Model (use run_Inference.py)

For further information please see: https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/hello_world/README.md

# Files:

Five_step_example/my_model: this is the saved model of the "Five_step_example"

Five_step_example.py: this is the example code. This is a very simple neural network

saved_Five_step_example.tflite: This is the tflite file that was converted from Tensorflow to Tensorflow lite as seen in the tfliteIOT.pptx

run_inference.py: this is the code to run an inference model on the IOT using the .tflite file



