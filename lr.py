import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


# random data that shows a rough linear relationship between page speed and amount purchased

page_speed = np.random.normal(3.0, 1.0, 1000)
purchase_amount = 100 - (page_speed +  np.random.normal(0, 0.1, 1000)) * 3

# finding the best fit line

slop, intercept, r_value, p_value, std_err = stats.linregress(page_speed, purchase_amount)

# checking if  R-squared value shows a really good fit

print(f'R-squared: {r_value ** 2}')


def predict(x):
    return slop * x * intercept

fit_line = predict(page_speed)

plt.scatter(page_speed, purchase_amount)
plt.plot(page_speed, fit_line, c='r')
plt.show()

