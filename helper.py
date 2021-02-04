import numpy as np
import matplotlib.pyplot as plt
import cv2
import cmath
import scipy as scipy
from math import *
class Helper:
    def __init__(self):
        self.changed_basis=None
        self.fully_reconstructed=None
        self.partial_reconstructed=None
        print("Press (1) to provide the input in the form of two arrays. The first one having x co-ordinates or the real part and the second having y co-ordinates or the imaginary part")
        print("Press (2) to provide a size of input. We will generate a random input from size")
        i=input()
        if i!='1' and i!='2':
            print("Please provide valid input")
        else:
            if i=='1':
                x=[int(ty) for ty in input("Please enter x co-ordinates/real parts").split()]
                y=[int(ty) for ty in input("Please enter y co-ordinates/imaginary parts").split()]
                if len(x)!=len(y):
                    print("The number of x(real) and y(imag) must be equal")
                else:
                    original_data=[]
                    for i in range(len(x)):
                        original_data.append(complex(x[i],y[i]))
                    self.original_data=original_data
            else:
                n=int(input("Enter the input size"))
                if n>1000:
                    print("Too many points")
                    self.original_data=[]
                else:
                    data=np.random.rand(n,2)*1000
                    original_data=[]
                    for i in range(len(data)):
                        original_data.append(complex(data[i][0],data[i][1]))
                    self.original_data=original_data
    def plot_original(self):
        x=[]
        y=[]
        my_data=self.original_data.copy()
        for i in my_data:
            x.append(i.real)
            y.append(i.imag)
        plt.scatter(x,y)
        plt.title("Original Plot",color='blue')
        plt.xlabel("Real",color='green')
        plt.ylabel("Imaginary",color='pink')
        plt.show()

    def change_basis(self):
        length=len(self.original_data)
        changed_vector=[]
        m=self.original_data
        for i in range(length):
            s=0
            for j in range(length):
                s+=m[j]*(complex(cos(-2*pi*j*i/length),sin(-2*pi*j*i/length)))
            changed_vector.append(s)
        self.changed_basis=changed_vector.copy()
    def full_reconstruction(self):  
        length=len(self.original_data)
        recovered_vector=[]
        m=self.changed_basis.copy()
        for i in range(length):
            s=0
            for j in range(length):
                s+=(m[j]*(complex(cos(2*pi*j*i/length),sin(2*pi*j*i/length))))/length
            recovered_vector.append(s)
        self.fully_reconstructed=recovered_vector.copy()
    def partial_reconstruction(self):
        pass
    def show_changed(self):
        changed_data_x=[]
        changed_data_y=[]
        m=self.changed_basis.copy()
        for i in m:
            changed_data_x.append(i.real)
            changed_data_y.append(i.imag)
        plt.scatter(changed_data_x,changed_data_y)
        plt.title("Changed Basis",color='blue')
        plt.xlabel("Real",color='green')
        plt.ylabel("Imaginary",color='pink')
        plt.show()
        
    def show_full_reconstructed(self):
        recovered_data_x=[]
        recovered_data_y=[]
        m=self.fully_reconstructed.copy()
        for i in m:
            recovered_data_x.append(i.real)
            recovered_data_y.append(i.imag)
        plt.scatter(recovered_data_x,recovered_data_y)
        plt.title("100% Reconstruction",color='blue')
        plt.xlabel("Real",color='green')
        plt.ylabel("Imaginary",color='pink')
        plt.show()
    
                
