# SRHiC
We developed a novel and simple computational method based on deep learning to enhance the resolution of Hi-C data. 



## Dependency
[python](https://www.python.org) (3.6)

[Tensorflow](https://www.tensorflow.org/)(v.1.13.1)

We recommand use the [anaconda3/5.2.0] (https://www.continuum.io) distribution to install the Dependency.

## Usage

### Training
In the training stage, high-resolution Hi-C samples and low-resolution Hi-C samples should be in the same shape as (N, n, n,1), where N is the number of the samples, n is the size of the samples and 1 is the number of channel.

### Prediction
Just low-resolution Hi-C samples are needed. The shape of the samples should be the same with the training stage. The prediction generates the enhanced Hi-C data, which is a bunch of sub-matrices. The user need to recombine them into a big matrix.


