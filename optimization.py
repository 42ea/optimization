'''
    Script containing an optimization problem class, which contains methods for
    solving optimization problems using different methods
                                                                            '''
import numpy as np
import scipy

class Optimization(object):

    def __init__(self,objective_function,gradient=None):
        self.objective_function = objective_function
        if gradient != None:
            self.gradient = gradient
    
    @methodclass
    def optimize(cls,opt_object,methods):
        
    def compute_gradient(self,x_k,x_km1):
        if self.gradient != None:
            return self.gradient(x_k)
        gradient_k = np.zeros(1,len(x_k))
        delta_x0 = x_k[0]-x_km1[0] 
        delta_x1 = x_k[1]-x_km1[1]
        x0 = np.array([delta_x0, x_k[1]])
        x1 = np.array([x_k[0], delta_x1])
        return np.array([self.objective_function(x0)/delta_x0, self.objective_function(x1)/delta_x1])





    