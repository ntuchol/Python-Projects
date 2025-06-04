def get_triangle(a,b,c):
  z = np.array([a,b,c])
  while z[-1] != z.max():
    z = z[[2,0,1]] # make sure last entry is largest
  alpha, beta, _ = calc_angles(*z)