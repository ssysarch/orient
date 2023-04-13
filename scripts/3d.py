import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import matplotlib
from matplotlib import cm
from colorspacious import cspace_converter
from collections import OrderedDict
from mpl_toolkits.mplot3d import Axes3D


#csfont = {'fontname':'serif'}
if (0):
	n_groups = 2
	x1 = (1, 1)
	x2 = (0.92, 0.81)

	# create plot
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.3
	opacity = 1

	rects1 = plt.bar(index, x1, bar_width,
	alpha=opacity,
	color='C7',
	edgecolor = "black",
	linewidth=2.0,
	label='Max-Ent')

	rects2 = plt.bar(index + bar_width, x2, bar_width,
	alpha=opacity,
	color='C1',
	fill='false',
	hatch='///',
	edgecolor = "black",
	linewidth=2.0,
	label='Our Approach',
	zorder=3)

	plt.xlabel('')
	plt.ylim([0.6,1.09])
	plt.ylabel('Normalized Attacker Accuracy', fontsize=20)
	plt.title('Prediction Accuracy Reduction < 5%', fontsize=20)
	ax.yaxis.set_major_locator(MultipleLocator(0.1))
	ax.yaxis.set_minor_locator(MultipleLocator(0.02))

	plt.yticks(fontsize=18)
	plt.xticks(index + bar_width/2, ('T1', 'T2'),fontsize=18)
	plt.xlim([0-bar_width,1+3*bar_width])
	red_patch = mpatches.Patch(facecolor='C1', label='Our Method', fill='false',hatch='///')
	maxEnt = mpatches.Patch(facecolor='C7', label='MaxEnt')
	plt.legend(handles=[maxEnt, red_patch], prop={'size': 20}, bbox_to_anchor=(0.05, 0.86, 0.9, .03), loc=3,
	       ncol=2, mode="expand", borderaxespad=0.)
	#plt.legend(loc=1)
	plt.grid(color = 'gray', axis='y', which= 'major', linestyle = '--', linewidth = 0.5, zorder=0)
	plt.grid(color = 'gray', axis='y', which= 'minor', linestyle = '--', linewidth = 0.1,zorder=0)

	#ax.annotate('', xy=(bar_width, 0.91),  xycoords='data',
	#            xytext=(0.15,0.85), textcoords='axes fraction',
	#            arrowprops=dict(facecolor='black', shrink=0.05),
	#            horizontalalignment='right', verticalalignment='top',
	#            )
	plt.tight_layout()
	plt.savefig('line_plot.pdf') 
	plt.show()
elif(0):
	ax = plt.axes(projection='3d')

	# Data for a three-dimensional line
	zline = np.linspace(0, 1, 10)
	xline = np.linspace(0, 1, 10)
	yline = np.linspace(0, 1, 10)
	#ax.plot3D(xline, yline, zline, 'gray')

	# Data for three-dimensional scattered points
	zdata = [10 ,6, 7, 8, 9] # accuracy
	xdata = [1,5, 10, 8, 8] # privacy
	ydata = [1, 7, 9, 5, 3] # latency
	cdata=[1, 2,3,4,5] #'Plain',  'ARL','HE','Orient', 'OrientExpress'
	cdata2=[0, 1,2,3,4]
	markerdata=["v","x","P","o","*"]
	myplot=[0,0,0,0,0]
	cm = plt.cm.get_cmap('tab20')
	c = [cm.colors[10], cm.colors[3],cm.colors[4],cm.colors[7], cm.colors[12]]
	for i in cdata2:
		myplot[i]=ax.scatter(xdata[i], ydata[i], zdata[i], c=c[i],marker=markerdata[i], s=100);

	mys=[500, 600, 400, 700, 900]
	#ax.scatter3D(xdata,ydata, zdata, facecolor="none",edgecolor='black', s=mys)
	ax.set_xlim(0, 10)
	ax.set_ylim(0, 10)
	ax.set_zlim(5, 10)
	ax.yaxis.set_major_locator(MultipleLocator(10))
	#ax.yaxis.set_minor_locator(MultipleLocator(1))
	ax.xaxis.set_major_locator(MultipleLocator(10))
	ax.zaxis.set_major_locator(MultipleLocator(10))
	ax.set_ylabel('Latency',fontweight='bold', family='serif')
	ax.set_zlabel('Accuracy',fontweight='bold', family='serif')
	ax.set_xlabel('Privacy',fontweight='bold', family='serif')
	ax.set_xticks((0,10))
	ax.set_xticklabels(('low', 'high'), family='serif')
	ax.set_yticks((0,10))
	ax.set_yticklabels(('low', 'high'), family='serif')
	ax.set_zticks((5,10))
	ax.set_zticklabels(('med', 'high'), family='serif')
	ax.grid(False)
	#ax.xaxis.pane.set_edgecolor('black')
	#ax.yaxis.pane.set_edgecolor('black')
	#ax.zaxis.pane.set_edgecolor('black')
	ax.xaxis.pane.fill = False
	ax.yaxis.pane.fill = False
	ax.zaxis.pane.fill = False
	ax.legend(['Plain',  'ARL','HE','Orient', 'OrientExpress'], prop={'size': 8, 'weight':'bold', 'family':'serif'}, ncol=2, loc='upper left')
	for i in cdata2:
		ax.plot(xdata[i], ydata[i],marker=markerdata[i] ,c='gray', zdir='z', zs=5)
		ax.plot(ydata[i], zdata[i],marker=markerdata[i] ,c='lightsteelblue', zdir='x', zs=0)
	ax.text(0, 3, 6.5, 'Lat-Acc','y',color='lightsteelblue')
	ax.text(3.5, 5, 4.4, 'Priv-Lat','x',color='gray')
	plt.tight_layout()
	plt.savefig('3d.pdf') 
	plt.show()
elif(1): 
	ax = plt.axes(projection='3d')

	# Data for a three-dimensional line
	zline = np.linspace(0, 1, 10)
	xline = np.linspace(0, 1, 10)
	yline = np.linspace(0, 1, 10)
	#ax.plot3D(xline, yline, zline, 'gray')

	# Data for three-dimensional scattered points
	zdata = [10 ,6, 7, 8, 9] # accuracy
	xdata = [1,5, 10, 8, 8] # privacy
	ydata = [1, 7, 9, 5, 3] # latency
	cdata=[1, 2,3,4,5] #'Plain',  'ARL','HE','Orient', 'OrientExpress'
	cdata2=[0, 1,2,3,4]
	markerdata=["v","x","P","o","*"]
	myplot=[0,0,0,0,0]
	cm = plt.cm.get_cmap('tab20')
	c = [cm.colors[10], cm.colors[3],cm.colors[4],cm.colors[7], cm.colors[12]]
	#for i in cdata2:
		#myplot[i]=ax.scatter(xdata[i], ydata[i], zdata[i], c=c[i],marker=markerdata[i], s=100);

	mys=[500, 600, 400, 700, 900]
	#ax.scatter3D(xdata,ydata, zdata, facecolor="none",edgecolor='black', s=mys)
	ax.set_xlim(0, 10)
	ax.set_ylim(0, 10)
	ax.set_zlim(5, 10)
	ax.yaxis.set_major_locator(MultipleLocator(10))
	#ax.yaxis.set_minor_locator(MultipleLocator(1))
	ax.xaxis.set_major_locator(MultipleLocator(10))
	ax.zaxis.set_major_locator(MultipleLocator(10))
	ax.set_ylabel('Latency',fontweight='bold', family='serif')
	ax.set_zlabel('Accuracy',fontweight='bold', family='serif')
	ax.set_xlabel('Privacy',fontweight='bold', family='serif')
	ax.set_xticks((0,10))
	ax.set_xticklabels(('low', 'high'), family='serif')
	ax.set_yticks((0,10))
	ax.set_yticklabels(('low', 'high'), family='serif')
	ax.set_zticks((5,10))
	ax.set_zticklabels(('med', 'high'), family='serif')
	ax.grid(False)
	#ax.xaxis.pane.set_edgecolor('black')
	#ax.yaxis.pane.set_edgecolor('black')
	#ax.zaxis.pane.set_edgecolor('black')
	ax.xaxis.pane.fill = True
	ax.yaxis.pane.fill = False
	ax.zaxis.pane.fill = True
	ax.xaxis.set_pane_color((228/256, 241/256, 254/256, .2))
	ax.zaxis.set_pane_color((246/256,246/256,246/256, .9))
	for i in cdata2:
		ax.plot(xdata[i], ydata[i],marker=markerdata[i] ,c=c[i], zdir='z', zs=5)
	
	#	ax.plot(xdata[i], zdata[i],marker=markerdata[i] ,c='red', zdir='y', zs=5)
	ax.legend(['Plain',  'ARL','HE','Orient', 'OrientExpress'], prop={'size': 8, 'weight':'bold', 'family':'serif'}, ncol=2, loc='upper right')
	for i in cdata2:
		ax.plot(ydata[i], zdata[i],marker=markerdata[i] ,c=c[i], zdir='x', zs=0)
	ax.text(0, 3, 6.5, 'Lat-Acc','y',color='black')
	ax.text(3.5, 3, 4.4, 'Priv-Lat','y',color='black')
	#ax.text(3.5, 5, 4.4, 'Priv-Lat','x',color='gray')
	plt.tight_layout()
	plt.savefig('3d.pdf') 
	plt.show()
