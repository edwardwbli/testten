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


def main():

	# Specify that all features have real-value data
        feature_columns = [tf.contrib.layers.real_valued_column("", dimension=12)]
        classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,optimizer=tf.train.ProximalAdagradOptimizer(learning_rate=0.01,l1_regularization_strength=0.001),model_dir="/tmp/customer_model9",hidden_units=[12, 12],n_classes=5)

        # Classify two new flower samples.
        def new_samples():
		customer1 = np.random.random((1,12))*5000
                return np.array(customer1, dtype=np.int)

        predictions = list(classifier.predict(input_fn=new_samples))

        print("New Samples, Class Predictions:    {}n".format(predictions))

if __name__ == "__main__":
        main()

exit(0)
