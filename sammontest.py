def main():

   import numpy as np 
   from sklearn import datasets
   import matplotlib.pyplot as plt
   from sammon import sammon

   """Test sammon.py by plotting a projection of iris flower data. 
      Run sammontest() with no arguments.

   File        : sammontest.py
   Date        : 18 April 2014
   Author      : Tom J. Pollard (tom.pollard.11@ucl.ac.uk)

   Description : Script to test sammon.py by applying it
   				  to Fisher's iris dataset
                 http://en.wikipedia.org/wiki/Iris_flower_data_set

   Copyright   : (c) 2014, Tom J. Pollard

   Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
   The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
   (MIT License, http://www.opensource.org/licenses/mit-license.php)

   """
   # Load the iris data
   data_BC = datasets.load_breast_cancer();
   X = data_BC.data
   target = data_BC.target
   names = data_BC.target_names
   
   #New Patient
   NewPatient = np.array([19.55,15.49,128,1000,0.1079,0.18347,0.4352,0.1196,0.2616,0.06752,1.223,0.4489,7.87,168.8,0.01101,0.04272,0.08624,0.02737,0.06041,0.007503,23.73,17.21,153.4,1633,0.1534,0.3391,0.5819,0.22,0.4714,0.09721])
   X = np.vstack([X, NewPatient]) 
   names = np.hstack([names, 'diagnosis'])   
   target = np.hstack([target, 2])

   # Run the Sammon projection
   [y,E] = sammon(X, inputdist = 'raw', maxiter = 50)

   # Plot
   plt.scatter(y[target ==0, 0], y[target ==0, 1], s=20, c='r', marker='o',label=names[0])
   plt.scatter(y[target ==1, 0], y[target ==1, 1], s=20, c='b', marker='D',label=names[1])
   plt.scatter(y[target ==2, 0], y[target ==2, 1], s=20, c='y', marker='v',label=names[2])
   plt.title('Sammon projection for Breast Cancer Data')
   plt.legend(loc=2)
   plt.annotate('patient', xy=(y[target ==2, 0], y[target ==2, 1]), xytext = (min([y[target ==2, 0]+800, plt.axis()[1]]), min([y[target ==2, 1]+800, plt.axis()[3]])), arrowprops=dict(facecolor='black', shrink=0.05),)
   plt.show()

   #plt.scatter(y[target ==0, 0], y[target ==0, 1], s=20, c='r', marker='o',label=names[0])
   #plt.scatter(y[target ==1, 0], y[target ==1, 1], s=20, c='b', marker='D',label=names[1])
   plt.scatter(y[target ==2, 0], y[target ==2, 1], s=20, c='y', marker='v',label=names[2])
   plt.title('Sammon projection for Breast Cancer Data - patient')
   plt.legend(loc=2)
   plt.show()
   
   
if __name__ == "__main__":
    main()

