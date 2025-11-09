def approximate_pi(n_terms):
  leibniz_series = []
  for i in range(n_terms):
      sign = (-1)**i/(2*i+1)
      leibniz_series.append(sign)
  return (sum(leibniz_series)*4)

