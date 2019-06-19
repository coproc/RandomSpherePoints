import math
import random

def randomPointOnSphere(r=1., center=(0.,0.,0.)):
	"""compute random point on sphere with uniform distribution on surface.

	   Usage can be as simple as that:
	   >>> p = randomPointOnSphere()

	   We expect a point with 3 coordinates and distance 1 from the origin:
	   >>> len(p) # three coordinates
	   3
	   >>> r2 = sum(c*c for c in p) # radius squared
	   >>> round(r2, 10)
	   1.0

	   Scaling (i.e. having a radius different from 1) ...
	   >>> r = 2
	   >>> p = randomPointOnSphere(r)
	   >>> r2 = sum(c*c for c in p) # radius squared
	   >>> round(r2, 10)
	   4.0

	   ... and shifting (i.e. specifying a center different from the origin)
	   is also possible.
	   >>> center = (1,-1,2)
	   >>> p = randomPointOnSphere(center=center)
	   >>> p0 = (c-center[i] for i,c in enumerate(p)) # subtract center
	   >>> r2 = sum(c*c for c in p0) # radius squared
	   >>> round(r2, 10)
	   1.0

	   Let's test for uniform distribution by computing a bunch of random points:
	   >>> n = 2000
	   >>> pl = [randomPointOnSphere() for _ in range(n)]

	   Counting points in a cap of r/2 = 0.5 should yield roughly a quarter (0.25):
	   >>> xTopFrac = sum(p[0]>0.5 for p in pl)/n
	   >>> 0.2 < xTopFrac < 0.3
	   True
	   >>> yTopFrac = sum(p[1]>0.5 for p in pl)/n
	   >>> 0.2 <= yTopFrac <= 0.3
	   True
	   >>> zTopFrac = sum(p[2]>0.5 for p in pl)/n
	   >>> 0.2 <= zTopFrac <= 0.3
	   True
	   >>> # xTopFrac, yTopFrac, zTopFrac
	"""
	# The surface area of a spherical segment of a unit sphere *only* dependes on its height
	# (see http://mathworld.wolfram.com/Zone.html),
	# so when projecting points uniformly distributed on the surface to an axis,
	# the projected points are uniformly distributed in [-1,1].
	z0 = random.uniform(-1.,1.)
	r0_xy = math.sqrt(1. - z0*z0)
	# rotation angle around z-axis
	theta = 2.*math.pi*random.uniform(0., 1.)
	x0 = r0_xy*math.cos(theta)
	y0 = r0_xy*math.sin(theta)
	return (center[0] + r*x0,
	        center[1] + r*y0,
	        center[2] + r*z0)

def randomPointInsideSphere(r=1., center=(0.,0.,0.)):
	"""compute random point inside sphere with uniform distribution.

	   >>> p = randomPointInsideSphere()
	   >>> len(p) # three coordinates
	   3
	   >>> r2 = sum(c*c for c in p) # radius squared
	   >>> r2 <= 1.0
	   True

	   >>> r = 2
	   >>> n = 1000
	   >>> pl = [randomPointInsideSphere(r) for _ in range(n)]
	   >>> r2l = [sum(c*c for c in p) for p in pl] # list of radius squared
	   >>> 3.9 < max(r2l) <= 4.0
	   True
	   >>> min(r2l) < 0.2
	   True

	   >>> center = (1,-1,2)
	   >>> p = randomPointInsideSphere(center=center)
	   >>> p0 = (c-center[i] for i,c in enumerate(p)) # subtract center
	   >>> r2 = sum(c*c for c in p0) # radius squared
	   >>> r2 <= 1.0
	   True

	   Let's test for uniform distribution:
	   >>> n = 2000
	   >>> pl = [randomPointInsideSphere() for _ in range(n)]
	   >>> r2l = [sum(c*c for c in p) for p in pl]
	   >>> pInnerFrac = sum(r2<0.25 for r2 in r2l)/n # r < 0.5
	   >>> abs(pInnerFrac - 0.125) < 0.03 # 0.5^3 = 0.125
	   True
	   >>> h = 0.5 # for spherical caps
	   >>> volCap = h*h*(3.-h)*math.pi/3.
	   >>> volSphere = 4*math.pi/3.
	   >>> volCapFrac = volCap/volSphere
	   >>> xTopFrac = sum(p[0]>0.5 for p in pl)/n
	   >>> abs(xTopFrac - volCapFrac) < 0.03
	   True
	   >>> yTopFrac = sum(p[1]>0.5 for p in pl)/n
	   >>> abs(yTopFrac - volCapFrac) < 0.03
	   True
	   >>> zTopFrac = sum(p[2]>0.5 for p in pl)/n
	   >>> abs(zTopFrac - volCapFrac) < 0.03
	   True
	   >>> # xTopFrac, yTopFrac, zTopFrac
	"""
	done = False
	while not done:
		p0 = random.uniform(-1.,1.), random.uniform(-1.,1.), random.uniform(-1.,1.)
		done = sum(c*c for c in p0) <= 1
	return (center[0] + r*p0[0],
	        center[1] + r*p0[1],
	        center[2] + r*p0[2])

if __name__ == "__main__":
	import doctest
	doctest.ELLIPSIS_MARKER = '[...]'
	doctest.testmod()
