# SRHiC
We developed a novel and simple computational method based on deep learning to enhance the resolution of Hi-C data. 
![image](https://github.com/hzlzldr/SRHiC/blob/master/pic/Fig1.jpg)

Recovering high-resolution Hi-C data from low-resolution Hi-C data
![image](https://github.com/hzlzldr/SRHiC/blob/master/pic/Fig2.png)


## Dependency
[ python ](https://www.python.org) (3.6)

[ Tensorflow ](https://www.tensorflow.org/)(v.1.13.1)

We recommand use the [anaconda3/5.2.0] (https://www.continuum.io) distribution to install the Dependency.

## Usage

### Training
In the data processing stage, we combined the corresponding high-resolution Hi-C sub-matrix and low-resolution Hi-C sub-matrix into a sub-matrix in which its shape is (X1,y1+y2),where x1 is the abscissa of low-resolution and x2 is the abscissa of high-resolution, y1 and y2 is the ordinate of low-resolution sub-matrix and high-resolution sub-matrix,respectively. For example, if the low-resolution sub-matrix is (40,40) and high-resolution sub-matrix is (28,28), so the combined sub-matrix is (40,68).

In the training stage, the input matrix shape should be in the shape as (N, n1, n2,1), where N is the number of the input matrix, n1 and is the size of the combined sub-matrix and 1 is the number of channel.



### Prediction
Just low-resolution Hi-C samples are needed. The shape of the samples should be the same with the training stage. The prediction generates the enhanced Hi-C data, which is a bunch of sub-matrices. The user need to recombine them into a big matrix.


