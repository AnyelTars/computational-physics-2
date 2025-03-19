#  Import modules
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Create main class
class MagneticField2D:
	"""
	
	"""
	# init function -> Grid information 
	def __init__(self, x_l =-10., x_r=+10, y_l=-10, y_r=+10,n=50):
		"""
		
		
		"""
		self.x_l=x_l
		self.x_r=x_r
		self.y_l=y_l
		self.y_r=y_r
		self.n = n
		
	# First method for grid generation 
	def grid_generator(self):
		"""
		
		"""
		
		# first 1d vector
		x = np.linspace(self.x_l,self.x_r,self.n)
		y = np.linspace(self.y_l,self.y_r,self.n)
		# create 2d grid
		x_2d, y_2d=np.meshgrid(x,y)
		#return
		return x_2d,y_2d
	# second method: static method for uniform field
	@staticmethod
	def uniform_bfield(x_2d,y_2d):
		"""
		
		
		"""
		# field components 
		bx_2d = np.full_like(x_2d,1)
		by_2d = np.full_like(y_2d,1)
		return bx_2d, by_2d
	@staticmethod
	def dipolar_bfield(x_2d,y_2d):
		"""
		
		
		"""
		# constans 
		b0=1e-5 
		R = 5.
		# radial coordinate
		r = np.sqrt(x_2d**2 + y_2d**2)

		# Define theta
		theta = np.arctan2(y_2d,x_2d)
		# field components in spherical coordinates 
		
		b_r = -2.*b0*(R**3/r**3)*np.cos(theta)
		b_theta = -b0*(R**3/r**3)*np.sin(theta)
		# conversion to cartesian coordiantes
		bx_2d = -b_theta*np.sin(theta)+b_r*np.cos(theta)
		by_2d = b_theta*np.cos(theta)+b_r*np.sin(theta)

		# temporary check 
		#return b_r, b_theta
		return bx_2d, by_2d
	

	# DIPOLAR FIELD
	# Ploting method
	def plot_2dfield(self,field_type):
		"""
		"""
		# call the grid information
		x_2d,y_2d=self.grid_generator()

		if field_type=="uniform":

			# call the field generators 
			bx_2d,by_2d=self.uniform_bfield(x_2d,y_2d)
	
		elif field_type=="dipolar":
			# call the field generators 
			bx_2d,by_2d=self.dipolar_bfield(x_2d,y_2d)
				
		else:
			raise ValueError("The argument field_type only accepts: 'uniform' or 'dipolar'")# value error
		
		# Compute B
		b_mod = np.sqrt(bx_2d**2+by_2d**2)

# # create a figure environment 
		plt.figure(figsize=(8,8))
		# Reference of stream plots : link 
		#plt.quiver(x_2d,y_2d,bx_2d,by_2d,np.log10(b_mod),arrowsize=1.5) #this is good for the unifrom map
		plt.streamplot(x_2d,y_2d,bx_2d,by_2d,color=b_mod,linewidth=1,arrowsize=1.5,cmap=plt.cm.inferno, density=2,arrowstyle='->')
		plt.savefig(field_type+".png")

	

# call the class	
if __name__=="__main__":

	# Parsing the code
	parser= argparse.ArgumentParser(description="Generate and make a map of 2D B fields")
	# Add arguments 
	parser.add_argument("--btype",choices=["uniform","dipolar"],required=True,help="Type of magnetic field")
	args=parser.parse_args()
	# instance of the class
	mag=MagneticField2D()
	"""
	
	"""
	#acess methods
	xx,yy=mag.grid_generator()
	#testing 
	b_r, b_theta = mag.dipolar_bfield(xx, yy)
	print("We should see the x and y shapes: ",b_r.shape)
	print("executed successfully")
	#print("We should see the x and y shapes: ",xx.shape,yy.shape)
	
	#PLot the uniform field

	#mag.plot_2dfield(field_type="dipolar")
	#Plot the unifrom field
	mag.plot_2dfield(field_type=args.btype)

		
		
