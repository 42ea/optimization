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
    def optimize(cls,opt_object,methods)

    def compute_gradient(self,f,x)





    