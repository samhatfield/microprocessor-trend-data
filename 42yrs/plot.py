import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
transistors    = np.loadtxt("transistors.dat")
specint        = np.loadtxt("specint.dat")
frequency      = np.loadtxt("frequency.dat")
power          = np.loadtxt("watts.dat")
cores          = np.loadtxt("cores.dat")
supercon_cores = np.loadtxt("supercomputer_cores.dat")

# Plot all series
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
plt.figure(figsize=(8,5))

plt.scatter(transistors[:,0], transistors[:,1], marker='^', s=20, color=colors[0])
plt.text(2021, transistors[-1,1], "Transistors (thousands)", va="center", color=colors[0])

plt.scatter(specint[:,0], specint[:,1], marker='o', s=20, color=colors[1])
plt.text(2021,specint[-1,1], "Single-thread performance\n(SpecINT $\\times10^3$)", va="center",
         color=colors[1])

plt.scatter(frequency[:,0], frequency[:,1], marker='s', s=20, color=colors[2])
plt.text(2021,frequency[-1,1], "Frequency (MHz)", va="center", color=colors[2])

plt.scatter(power[:,0], power[:,1], marker='v', s=20, color=colors[3])
plt.text(2021,power[-1,1], "Typical power (W)", va="center", color=colors[3])

plt.scatter(cores[:,0], cores[:,1], marker='v', s=20, color=colors[4])
plt.text(2021,cores[-1,1], "Number of cores", va="center", color=colors[4])

plt.scatter(supercon_cores[:,0], supercon_cores[:,1], marker='D', s=20, color=colors[5])
plt.text(2021,supercon_cores[-1,1], "Number of cores\n(#1 supercomputer)", va="center",
         color=colors[5])

plt.subplots_adjust(right=0.72)
plt.yscale("log")
plt.xlim([1970, 2020])
plt.ylim([10**-1, 10**8])
plt.gca().grid()
plt.savefig("42-years.pdf", bbox_inches="tight")
plt.savefig("42-years.png", bbox_inches="tight")
plt.savefig("42-years.eps", bbox_inches="tight")
