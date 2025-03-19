# For installation 
from setuptools import setup, find_ackages 

# Call setup 
setup(name="magnetic", description= "2D B vector field generator",\ author = "ADSG" , license="GNU", author_email="angel.salazar@yachaytech.edu.ec", packages = find_packages(), install_requires = ["numpy", "matplotlib"])
