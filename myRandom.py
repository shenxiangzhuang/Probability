import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.special import erfinv

class MyRandom:
    def __init__(self, n=500):
        self._n = n
        self._uniform_points = np.random.uniform(0, 1, n)
        self._comput_points = None
        self._mydist_points = None

    def get_comput_points(self):
        pass

    def get_mydist_point(self):
        pass

    def plot(self):
        pass


# Normal
class MyNormal(MyRandom):
    def __init__(self, mu=0, sigma=1, n=500):
        super().__init__(n)
        self._mu = mu
        self._sigma = sigma

    def get_comput_points(self):
        self._comput_points = np.random.normal(self._mu, self._sigma, self._n)

    def get_mydist_point(self):
        self._mydist_points = erfinv(2*self._uniform_points-1)*(self._sigma/np.sqrt(2))+self._mu

    def plot(self):
        self.get_comput_points()
        self.get_mydist_point()

        plt.subplot(211)
        sns.distplot(self._comput_points)
        plt.subplot(212)
        sns.distplot(self._mydist_points)
        plt.suptitle('X~N(%s, %s)' % (self._mu, self._sigma))
        plt.show()

# Exponential
class MyExp(MyRandom):
    def __init__(self, lamb=1, n=500):
        super().__init__(n)
        self._lamb = lamb

    def get_comput_points(self):
        self._comput_points = np.random.exponential(self._lamb, self._n)

    def get_mydist_point(self):
        self._mydist_points = (1/self._lamb)*np.log(1/(1-self._uniform_points))

    def plot(self):
        self.get_comput_points()
        self.get_mydist_point()

        plt.subplot(211)
        sns.distplot(self._comput_points)
        plt.subplot(212)
        sns.distplot(self._mydist_points)
        plt.suptitle('X~Exp(%s)' % self._lamb)
        plt.show()


if __name__ == '__main__':
    myexp = MyExp(2, 500)
    myexp.plot()

    mynorm = MyNormal(0, 1, 500)
    mynorm.plot()