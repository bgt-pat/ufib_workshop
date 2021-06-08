wort = deltat*UA/M/Cp
glycol = deltat*UA/mj/cpj

A = np.array([[1 - wort, wort],
              [glycol,1 - glycol]])