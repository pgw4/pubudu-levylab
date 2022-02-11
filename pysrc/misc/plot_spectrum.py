import numpy as np
import matplotlib.pyplot as plt
import os

sp_lim = [400, 1000]  # in nm
plt_xrange = [500,1000]  # in nm 

path = "C:\\Users\\pubud\\Desktop\\Spectrum Files"
os.chdir(path)

fig = plt.figure()
plt.xlabel("Wavelength (nm)")
plt.ylabel("Strength")
plt.title("Spectrum Comparison")
for file in os.listdir():
    if file.endswith(".txt"):
        datafile = f"{path}\{file}"
        with open(datafile,'r') as datafile:
            datalist = np.genfromtxt(datafile, delimiter='\t')
            x_scale = [sp_lim[0] + (sp_lim[1]-sp_lim[0])*i/len(datalist) for i in range(len(datalist))]
            plt.plot(x_scale, datalist, label=file)
    print("file done")

plt.xlim(plt_xrange[0], plt_xrange[1])
plt.legend()
plt.show()