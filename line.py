__author__ = 'fay'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x=[0,1000,3000,5000,7000,9000,10000]
y1=[1,0.94,0.90,0.85,0.80,0.75,0.56]
y2=[1,0.86,0.80,0.77,0.53,0.33,0.35]

pdf= PdfPages('1.pdf')
plt.figure()
plt.plot(x,y1,color='red',label='y1')
plt.plot(x,y2,color='blue',label='y2')

# plt.title("precision@k")
xlabel=plt.xlabel('k',fontsize=16)
ylabel=plt.ylabel('precision@k',fontsize=16)

plt.xlim(0,10000)
plt.ylim(0,1)
legend = plt.legend(loc='upper right')
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize=18)
# legend.set_title().set_fontsize(fontsize=20)

pdf.savefig()
pdf.close()
