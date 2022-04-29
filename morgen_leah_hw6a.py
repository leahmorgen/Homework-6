import numpy as np
import matplotlib.pyplot as plt
from morgen_leah_hw6b import function_1
x_1 = np.arange(10**3)
from morgen_leah_hw6b import function_2
x_2 = np.arange(10**3)
from morgen_leah_hw6b import function_3
x_3 = np.arange(100)
from morgen_leah_hw6b import function_4
x_4 = np.arange(100)

fig,axs = plt.subplots(2,2,figsize = (10,5)) 

axs[0,0].plot(x_1, function_1(x_1), color = "cadetblue")
axs[0,0].set_ylabel(r'$x^2$ - 2x +1')
axs[0,0].yaxis.set_label_position("left")


axs[0,1].plot(x_2, function_2(x_2), color = "blueviolet")
axs[0,1].set_ylabel(" sin(x) + 5")
axs[0,1].yaxis.tick_right()
axs[0,1].yaxis.set_label_position("right")

axs[1,0].plot(x_3, function_3(x_3), color = "darkorchid")
axs[1,0].set_ylabel("ln(x+1) + x^2 +x")
axs[1,0].yaxis.set_label_position("left")

axs[1,1].plot(x_4, function_4(x_4), color = "lightseagreen")
axs[1,1].set_ylabel("cos(x) - 5 +x^3")
axs[1,1].yaxis.set_label_position("right")
axs[1,1].yaxis.tick_right()

axs[0,0].set_yscale('log')
axs[0,0].set_xscale('log')
axs[0,1].set_xscale('log')

axs[1,0].set_yscale('log')

axs[1,1].set_yscale('log')


plt.savefig("LeahsHW6.png",dpi = 300)  
 
print("hi")