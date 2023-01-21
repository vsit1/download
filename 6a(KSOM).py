# KSOM
!pip install minisom
from minisom import MiniSom

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
%load_ext autoreload
#training input RGBcolors
colors=[[0.,0.,0.], [0.,0.,1.], [0.,0.,0.5], [0.125,0.529,1.0], [0.33,0.4,0.64],
        [0.6,0.5,1.0], [0.,1.,0.], [1.,0.,0.], [0.,1.,1.], [1.,1.,0.], [1.,1.,1.],
        [.33,.33,.33], [.5,.5,.5], [.66,.66,.66],]
color_names=['black','blue','darkblue','skyblue','greyblue','lilac','green','red','cyan','violet','yellow','white','darkgrey',
'mediumgrey','lightgrey']
som=MiniSom(30,30,3,sigma=3.,learning_rate=2.5, neighborhood_function='gaussian')
plt.imshow(abs(som.get_weights()),interpolation='none')
#plt.show()
som.train(colors, 500, random_order=True, verbose=True)
plt.imshow(abs(som.get_weights()),interpolation='none')
som=MiniSom(30,30,3,sigma=8.,learning_rate=.5, neighborhood_function='bubble')
som.train_random(colors, 500, verbose=True)
plt.imshow(abs(som.get_weights()),interpolation='none')