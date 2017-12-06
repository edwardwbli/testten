#!/usr/bin/python
#coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import os
import urllib

tf.logging.set_verbosity(tf.logging.ERROR)              #日志级别设置成 ERROR，避免干扰
np.set_printoptions(threshold='nan')                    #打印内容不限制长度

# Data sets
IRIS_TRAINING = "sample2.csv"

IRIS_TEST = "test2.csv"

def main():

        # Load datasets.
        training_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=IRIS_TRAINING,
                target_dtype=np.int,
                features_dtype=np.int)

        test_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=IRIS_TEST,
                target_dtype=np.int,
                features_dtype=np.int)

        # Specify that all features have real-value data
        feature_columns = [tf.contrib.layers.real_valued_column("", dimension=12)]

        # Build 3 layer DNN with 10, 20, 10 units respectively.
	# model8 is a better version till now , with DDNClassifier option
	# classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,hidden_units=[12, 12],n_classes=5,
        #                                            optimizer=tf.train.ProximalAdagradOptimizer(learning_rate=0.01,l1_regularization_strength=0.001),
        #                                            model_dir="/tmp/customer_model8")
        classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,hidden_units=[12, 12],n_classes=5,
						    optimizer=tf.train.ProximalAdagradOptimizer(learning_rate=0.01,l1_regularization_strength=0.001),
						    model_dir="/tmp/customer_model9")
        # Define the training inputs
        def get_train_inputs():
                x = tf.constant(training_set.data)
                y = tf.constant(training_set.target)
                return x, y

        # Fit model.
	for _ in range(1,53):
		classifier.fit(input_fn=get_train_inputs, steps=1000)

        # Define the test inputs
        def get_test_inputs():
                x = tf.constant(test_set.data)
                y = tf.constant(test_set.target)

                return x, y

        # Evaluate accuracy.
        print(classifier.evaluate(input_fn=get_test_inputs, steps=1))
        accuracy_score = classifier.evaluate(input_fn=get_test_inputs, steps=1)["accuracy"]

        print("nTest Accuracy: {0:f}n".format(accuracy_score))

        # Classify two new flower samples.
        def new_samples():
		customer1 = np.random.random((1,12))*20000
                return np.array(customer1, dtype=np.int)

        predictions = list(classifier.predict(input_fn=new_samples))

        print("New Samples, Class Predictions:    {}n".format(predictions))

if __name__ == "__main__":
        main()

exit(0)
