# correlations
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)
print("Positive Correlation with some noise")
y = x + np.random.normal(0, 10, 1000)
np.corrcoef(x, y)
plt.style.use('ggplot')
plt.scatter(x, y)
plt.show()

print("Negative Correlation with some noise")
np.random.seed(1)
# 1000 random integers between 0 and 50
a = np.random.randint(0, 50, 1000)
# Negative Correlation with some noise
b = 100 - a + np.random.normal(0, 5, 1000)
np.corrcoef(a, b) 
plt.scatter(a, b) 
plt.show()

print("No/ Weak correlation")
p = np.random.randint(0, 50, 1000)
q = np.random.randint(0, 50, 1000) 
np.corrcoef(p, q)
plt.scatter(p, q) 	
plt.show()