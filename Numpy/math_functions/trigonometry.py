import numpy as np

# Trigonometric Function	         Computes (in radians)

# sin()	                         the sine of an angle
# cos()	                         cosine of an angle
# tan()                          	 tangent of an angle
# arcsin()	                     the inverse sine
# arccos()	                     the inverse cosine
# arctan()	                     the inverse tangent
# degrees()	                     converts an angle in radians to degrees
# radians()	                     converts an angle in degrees to radians


angles = np.array([2, 4, 6])
sin_values = np.sin(angles)
cos_values = np.cos(angles)

inverse_sin = np.arcsin(angles)

print("Sin Values are: ", sin_values)
print("Inverse values are: ", inverse_sin)
print(f"Cosine values are {cos_values}")