#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tensorflow as tf
import numpy as np
import os

epoch_size=256

def predict(test_input_dir,
            checkpoint_dir,
            predict_save_dir,):


    ckpt = tf.train.get_checkpoint_state(checkpoint_dir)

    if ckpt and ckpt.model_checkpoint_path:
        graph_path = ckpt.model_checkpoint_path + '.meta'
        with tf.Session() as sess:

            # load model
            tf.local_variables_initializer().run()
            saver = tf.train.import_meta_graph(graph_path)
            saver.restore(sess, ckpt.model_checkpoint_path)
            graph = tf.get_default_graph()
            output_x = tf.get_collection('output_x')[0]
            input_x = graph.get_operation_by_name('input_x').outputs[0]
            print("restoration is done...")
            test_files=os.listdir(test_input_dir)
            print(test_files)
            for test_file in test_files:
                test=test_input_dir+test_file
                x = np.load(test).astype(np.float32)
                x = np.reshape(x, [x.shape[0], 40, 40, 1])
                size = int(x.shape[0] / epoch_size) + 1
                Out = np.zeros([1, 28, 28, 1])
                for z in range(size):
                    out = sess.run(
                        [output_x],
                        feed_dict={input_x: x[z * epoch_size:z * epoch_size + epoch_size]}
                    )

                    out_temp=np.array(out).reshape([-1,28,28,1])
                    Out = np.concatenate((Out, out_temp), axis=0)
                name ="enhanced_{0}".format(test_file)
                Out = Out[1:]
                np.save(predict_save_dir + '/predict/' + name, Out)
    else:
        print("---no checkpoint found---")



