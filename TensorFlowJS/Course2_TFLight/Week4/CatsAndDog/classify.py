# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from tflite_runtime.interpreter import Interpreter
import numpy as np
import argparse
from PIL import Image

#parser = argparse.ArgumentParser(description='Image Classification')
#parser.add_argument('--filename', type=str, help='Specify the filename', required=True)
#parser.add_argument('--model_path', type=str, help='Specify the model path', required=True)
#parser.add_argument('--label_path', type=str, help='Specify the label map', required=True)
#parser.add_argument('--top_k', type=int, help='How many top results', default=3)

#args = parser.parse_args()

fileList = os.listdir("./test_images")
#print(fileList[0:5])
for i in range(len(fileList)):
	filename = "./test_images/{}".format(fileList[i])
	model_path = "converted_model.tflite"
	label_path = "labels.txt"
	top_k_results = 3

	with open(label_path, 'r') as f:
		labels = list(map(str.strip, f.readlines()))

	# Load TFLite model and allocate tensors
	interpreter = Interpreter(model_path=model_path)
	interpreter.allocate_tensors()

	# Get input and output tensors.
	input_details = interpreter.get_input_details()
	output_details = interpreter.get_output_details()

	# Read image
	img = Image.open(filename).convert('RGB')

	# Get input size
	input_shape = input_details[0]['shape']
	size = input_shape[:2] if len(input_shape) == 3 else input_shape[1:3]

	# Preprocess image
	img = img.resize(size)
	img = np.array(img,dtype=np.float32)
	img = img / 255.
	# Add a batch dimension
	input_data = np.expand_dims(img, axis=0)

	# Point the data to be used for testing and run the interpreter
	interpreter.set_tensor(input_details[0]['index'], input_data)
	interpreter.invoke()

	# Obtain results and print the predicted category
	predictions = interpreter.get_tensor(output_details[0]['index'])
	predicted_label = np.argmax(predictions)
	predictionLabel = 'cat' if predicted_label == 0 else 'dog'
	print(predictions,fileList[i],predictionLabel,predictionLabel in fileList[i],predictions.sum())
	
