#!/usr/bin/python
#coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import os
import urllib
#deactivate the warning about the 
#017-12-11 06:51:50.748014: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
tf.logging.set_verbosity(tf.logging.ERROR)              #日志级别设置成 ERROR，避免干扰
np.set_printoptions(threshold='nan')                    #打印内容不限制长度


def main():

	# Specify that all features have real-value data
        feature_columns = [tf.contrib.layers.real_valued_column("", dimension=12)]
        classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,optimizer=tf.train.ProximalAdagradOptimizer(learning_rate=0.01,l1_regularization_strength=0.001),model_dir="./customer_model34",hidden_units=[12, 6],n_classes=5)

        # Classify two new flower samples.
	# enhance to use two sample with same offset to make predictions of next level of customer
        def new_samples():
                offset = input("input offset: ")
		sample = np.random.random((1,12))*offset
		print(sample)	
		return np.array(sample, dtype=np.int)
	
        predictions = list(classifier.predict(input_fn=new_samples))

        print("New Samples, Class Predictions:    {}n".format(predictions))

if __name__ == "__main__":
        main()

exit(0)
