## Segmentation tool with GUI based on pyQT5 and OpenCV for Python 3

For the convenience of starting the examples, we recommend you to install Anaconda and PyCharm packages on your PC.
[Link to the article with a detailed description](https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444).

The project uses: Python 3.х, libraries [pyQT5](https://stackoverflow.com/questions/16846501/how-to-install-pyqt5-on-windows), [scikit-image](http://scikit-image.org), [opencv 3](https://opencv.org/opencv-3-0.html), [NumPy](https://pypi.org/project/numpy/).

--------------------------------------

**For the correct functioning of the program _segmentation_tool.py_, you need to do the following steps (for Windows):**

Create dependencies between **Python 3**, **pyQT5**, package **scikit-image** and **OpenCV 3**.

**1.1** Press the key combination **Win + R**, enter the command _cmd_ in the appeared window (call the command line)

**1.2** Create a python 35 environment with the command:  

	conda create –n python35 python=3.5 anaconda
    
**1.3** Activate the python 35 environment with the command:

	activate python 35

**1.4** Now you can check the version of python using the command 

	python --version

**1.5** Now you need to install the necessary libraries for work:

OpenCV:

	conda install -c conda-forge opencv

scikit-image:

	pip install scikit-image or conda install -c conda-forge scikit-image

NumPy:

	pip install numpy

pyQT5: [link to the official website.](https://riverbankcomputing.com/software/pyqt/download5)

------------------------------------------------------------------------

Next, you need to **clone files from [repository](https://github.com/yuddim/multi_class_segmentation_tool)** and run the program in 
**PyCharm**. 

**Example of program operation:**

![alt text](1.jpg)
----------------------------------
[Video showing the work with the program](https://www.youtube.com/watch?v=bjM5I21gQFw)

[![Video showing the work with the program](https://i9.ytimg.com/vi/bjM5I21gQFw/mq3.jpg?sqp=CNjB4toF&rs=AOn4CLAl9VX6nNk0mjbAnuoHcSOHTqQbFw)](https://www.youtube.com/watch?v=bjM5I21gQFw)
