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

elif(1):
	n_groups = 2
	i = 0
	mm =[1]*8
	with open('../code/res.txt') as f:
		lines = f.readlines()
		for l in lines:
			mm[i] = float(lines[i].rstrip())
			print(mm[i])
			i = i+1 
	for i in range (1,8):
		mm[i] = mm[i]/mm[0]
	mm[0] = 1

	baseline = 50
	cm = plt.cm.get_cmap('tab20')

	# create plot
	fig, ax = plt.subplots(figsize=(9, 5))
	index = np.arange(n_groups)
	bar_width = 0.1
	opacity = 1

	rects1 = plt.bar(index, mm[0], bar_width,
	alpha=opacity,
	color='C7',
	edgecolor = "black",
	linewidth=2.0,
	label='Plain')

	rects2 = plt.bar(index + bar_width, mm[1], bar_width,
	alpha=opacity,
	color=cm.colors[3],
	fill='false',
	hatch='///',
	edgecolor = "black",
	linewidth=2.0,
	label='TEE',
	zorder=3)
	rects22 = plt.bar(index + 2*bar_width, mm[2], bar_width,
	alpha=opacity,
	color=cm.colors[9],
	fill='false',
	hatch='--',
	edgecolor = "black",
	linewidth=2.0,
	label='Occlumency',
	zorder=3)
	rects3 = plt.bar(index + 3*bar_width, mm[3], bar_width,
	alpha=opacity,
	color=cm.colors[2],
	fill='false',
	hatch='|',
	edgecolor = "black",
	linewidth=2.0,
	label='Slalom',
	zorder=3)
	rects33 = plt.bar(index + 4*bar_width, mm[4], bar_width,
	alpha=opacity,
	color=cm.colors[1],
	fill='false',
	hatch='*',
	edgecolor = "black",
	linewidth=2.0,
	label='Origami',
	zorder=3)
	rects4 = plt.bar(index + 5*bar_width, mm[5], bar_width,
	alpha=opacity,
	color=cm.colors[7],
	fill='false',
	hatch='o',
	edgecolor = "black",
	linewidth=2.0,
	label='CraterLake',
	zorder=3)
	# rects5 = plt.bar(index + 5*bar_width, x5, bar_width,
	# alpha=opacity,
	# color=cm.colors[6],
	# fill='false',
	# hatch='..',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='Orient',
	# zorder=3)
	# rects6 = plt.bar(index + 6*bar_width, x6, bar_width,
	# alpha=opacity,
	# color=cm.colors[15],
	# fill='false',
	# hatch='XX',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='OrientExp',
	# zorder=3)
	# rects61 = plt.bar(index + 7*bar_width, x61, bar_width,
	# alpha=opacity,
	# color=cm.colors[0],
	# fill='false',
	# hatch='--',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='OrientExp+TEE',
	# zorder=3)
	rects62 = plt.bar(index + 6*bar_width, mm[6], bar_width,
	alpha=opacity,
	color=cm.colors[5],
	fill='false',
	hatch='\\',
	edgecolor = "black",
	linewidth=2.0,
	label='Orient+TEE',
	zorder=3)
	rects7 = plt.bar(index + 7*bar_width, mm[7], bar_width,
	alpha=opacity,
	color=cm.colors[16],
	fill='false',
	hatch='+',
	edgecolor = "black",
	linewidth=2.0,
	label='Ori+Cra',
	zorder=3)
	# rects8 = plt.bar(index + 9*bar_width, x8, bar_width,
	# alpha=opacity,
	# color=cm.colors[19],
	# fill='false',
	# hatch='O.',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='OriExp+Cra',
	# zorder=3)

	plt.xlabel('')
	plt.ylim([.5,1500])
	plt.ylabel('Latency\n (w.r.t. Plain)', fontsize=24)
	#plt.title('Constant encoder', fontsize=20)
	ax.yaxis.set_major_locator(MultipleLocator(1000))
	ax.yaxis.set_minor_locator(MultipleLocator(100))
	#ax.bar_label(rects4,
    #         padding=8, color='b', fontsize=14)
	plt.yticks(fontsize=22)
	plt.xticks(index + 3.5*bar_width, ('HW/SW Methods', ''),fontsize=22)
	plt.xlim([0-1*bar_width,8*bar_width])
	x2_patch = mpatches.Patch(facecolor=cm.colors[3], label='TEE', fill='false',hatch='///')
	x22_patch = mpatches.Patch(facecolor=cm.colors[9], label='Occlumency', fill='false',hatch='--')
	x3_patch = mpatches.Patch(facecolor=cm.colors[2], label='Slalom', fill='false',hatch='|')
	x33_patch = mpatches.Patch(facecolor=cm.colors[1], label='Origami', fill='false',hatch='*')
	x4_patch = mpatches.Patch(facecolor=cm.colors[7], label='CraterLake', fill='false',hatch='o')
	x5_patch = mpatches.Patch(facecolor=cm.colors[6], label='Orient', fill='false',hatch='..')
	x6_patch = mpatches.Patch(facecolor=cm.colors[15], label='OrientExp', fill='false',hatch='XX')
	x61_patch = mpatches.Patch(facecolor=cm.colors[0], label='OriExp+TEE', fill='false',hatch='--')
	x62_patch = mpatches.Patch(facecolor=cm.colors[5], label='Orient+TEE', fill='false',hatch='\\')
	x7_patch = mpatches.Patch(facecolor=cm.colors[16], label='Orient+CraterLake', fill='false',hatch='+')
	x8_patch = mpatches.Patch(facecolor=cm.colors[19], label='OriExp+Cra', fill='false',hatch='O.')

	#print(x1,x2,x3,x33,x4,x62,x7)
	
	base = mpatches.Patch(facecolor='C7', label='Plain')
	plt.legend(handles=[base, rects2,rects22, rects3,rects33, rects4,rects62,rects7], prop={'size': 18}, bbox_to_anchor=(0.15, 0.78, 0.9, .03), loc=3,
	       ncol=2, borderaxespad=0.)
	#plt.legend(loc=1)
	plt.grid(color = 'gray', axis='y', which= 'major', linestyle = '--', linewidth = 0.5, zorder=0)
	plt.grid(color = 'gray', axis='y', which= 'minor', linestyle = '--', linewidth = 0.1,zorder=0)
	ax.set_yscale('log')
	#ax.annotate('', xy=(bar_width, 0.91),  xycoords='data',
	#            xytext=(0.15,0.85), textcoords='axes fraction',
	#            arrowprops=dict(facecolor='black', shrink=0.05),
	#            horizontalalignment='right', verticalalignment='top',
	#            )
	plt.tight_layout()
	plt.savefig('sens.pdf') 
	plt.show()
