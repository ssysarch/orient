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
	n_groups = 2
	x1 = (1, 1)
	x2 = (0.92, 0.9) # AdvFg
	x3 = (0.93, 0.9) # FCRL
	x4 = (0.94, 0.91) # HE (LOLA)
	x5 = (0.96, 0.94) # Orient
	#x6 = (0.84, 0.88) # Orient Exp 
	cm = plt.cm.get_cmap('tab20')

	# create plot
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.15
	opacity = 1

	rects1 = plt.bar(index, x1, bar_width,
	alpha=opacity,
	color='C7',
	edgecolor = "black",
	linewidth=2.0,
	label='Plain')

	rects2 = plt.bar(index + bar_width, x2, bar_width,
	alpha=opacity,
	color=cm.colors[1],
	fill='false',
	hatch='///',
	edgecolor = "black",
	linewidth=2.0,
	label='AdvFg',
	zorder=3)
	rects3 = plt.bar(index + 2*bar_width, x3, bar_width,
	alpha=opacity,
	color=cm.colors[4],
	fill='false',
	hatch='|',
	edgecolor = "black",
	linewidth=2.0,
	label='FCRL',
	zorder=3)
	rects4 = plt.bar(index + 3*bar_width, x4, bar_width,
	alpha=opacity,
	color=cm.colors[13],
	fill='false',
	hatch='o',
	edgecolor = "black",
	linewidth=2.0,
	label='LoLa',
	zorder=3)
	rects5 = plt.bar(index + 4*bar_width, x5, bar_width,
	alpha=opacity,
	color=cm.colors[6],
	fill='false',
	hatch='..',
	edgecolor = "black",
	linewidth=2.0,
	label='Orient',
	zorder=3)
	# rects6 = plt.bar(index + 5*bar_width, x6, bar_width,
	# alpha=opacity,
	# color='C5',
	# fill='false',
	# hatch='XX',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='OrientExp',
	# zorder=3)
	plt.xlabel('')
	plt.ylim([0.7,1.09])
	plt.ylabel('Accuracy\n (w.r.t. Plain)', fontsize=24)
	#plt.title('α=0.5', fontsize=18)
	ax.yaxis.set_major_locator(MultipleLocator(0.1))
	ax.yaxis.set_minor_locator(MultipleLocator(0.02))

	plt.yticks(fontsize=22)
	plt.xticks(index + 2.4*bar_width, ('Resnet-18', 'VGG16'),fontsize=22)
	plt.xlim([0-1.5*bar_width,1+5.5*bar_width])
	x2_patch = mpatches.Patch(facecolor=cm.colors[1], label='AdvFg', fill='false',hatch='///')
	x3_patch = mpatches.Patch(facecolor=cm.colors[4], label='FCRL', fill='false',hatch='|')
	x4_patch = mpatches.Patch(facecolor=cm.colors[13], label='LoLa', fill='false',hatch='o')
	x5_patch = mpatches.Patch(facecolor=cm.colors[6], label='Orient', fill='false',hatch='..')
#	x6_patch = mpatches.Patch(facecolor=cm.colors[13], label='OrientExp', fill='false',hatch='XX')
	
	base = mpatches.Patch(facecolor='C7', label='Plain')
	plt.legend(handles=[base, rects2, rects3, rects4, rects5], prop={'size': 22}, bbox_to_anchor=(0.025, 0.86, 0.9, .03), loc=3,
	       ncol=2, borderaxespad=0.)
	#plt.legend(loc=1)
	plt.grid(color = 'gray', axis='y', which= 'major', linestyle = '--', linewidth = 0.5, zorder=0)
	plt.grid(color = 'gray', axis='y', which= 'minor', linestyle = '--', linewidth = 0.1,zorder=0)

	#ax.annotate('', xy=(bar_width, 0.91),  xycoords='data',
	#            xytext=(0.15,0.85), textcoords='axes fraction',
	#            arrowprops=dict(facecolor='black', shrink=0.05),
	#            horizontalalignment='right', verticalalignment='top',
	#            )
	plt.tight_layout()
	plt.savefig('acc.pdf') 
	plt.show()
elif(0):
	n_groups = 2
	
	x1 = (1, 1)
	x2 = (1, 1)
	x3 = (1, 1)
	x4 = (1, 1)
	x5 = (1, 1)
	#print(x3[0]/x3[1])
	#x6 = (0.84, 0.88) # Orient Exp 
	cm = plt.cm.get_cmap('tab20')

	# create plot
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.15
	opacity = 1

	rects1 = plt.bar(index, x1, bar_width,
	alpha=opacity,
	color='C7',
	edgecolor = "black",
	linewidth=2.0,
	label='Plain')

	rects2 = plt.bar(index + bar_width, x2, bar_width,
	alpha=opacity,
	color=cm.colors[1],
	fill='false',
	hatch='///',
	edgecolor = "black",
	linewidth=2.0,
	label='AdvFg',
	zorder=3)
	rects3 = plt.bar(index + 2*bar_width, x3, bar_width,
	alpha=opacity,
	color=cm.colors[4],
	fill='false',
	hatch='|',
	edgecolor = "black",
	linewidth=2.0,
	label='FCRL',
	zorder=3)
	rects4 = plt.bar(index + 3*bar_width, x4, bar_width,
	alpha=opacity,
	color=cm.colors[13],
	fill='false',
	hatch='o',
	edgecolor = "black",
	linewidth=2.0,
	label='LoLa',
	zorder=3)
	rects5 = plt.bar(index + 4*bar_width, x5, bar_width,
	alpha=opacity,
	color=cm.colors[6],
	fill='false',
	hatch='..',
	edgecolor = "black",
	linewidth=2.0,
	label='Orient',
	zorder=3)
	# rects6 = plt.bar(index + 5*bar_width, x6, bar_width,
	# alpha=opacity,
	# color='C5',
	# fill='false',
	# hatch='XX',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='OrientExp',
	# zorder=3)
	plt.xlabel('')
	plt.ylim([.5,500000])
	plt.ylabel('Latency\n (w.r.t. Plain)', fontsize=24)
	#plt.title('Constant encoder', fontsize=20)
	ax.yaxis.set_major_locator(MultipleLocator(1000))
	ax.yaxis.set_minor_locator(MultipleLocator(100))
	#ax.bar_label(rects4,
    #         padding=8, color='b', fontsize=14)
	plt.yticks(fontsize=22)
	plt.xticks(index + 2.4*bar_width, ('Resnet-18', 'VGG16'),fontsize=22)
	plt.xlim([0-1.5*bar_width,1+5.5*bar_width])
	x2_patch = mpatches.Patch(facecolor=cm.colors[1], label='AdvFg', fill='false',hatch='///')
	x3_patch = mpatches.Patch(facecolor=cm.colors[4], label='FCRL', fill='false',hatch='|')
	x4_patch = mpatches.Patch(facecolor=cm.colors[13], label='LoLa', fill='false',hatch='o')
	x5_patch = mpatches.Patch(facecolor=cm.colors[6], label='Orient', fill='false',hatch='..')
#	x6_patch = mpatches.Patch(facecolor=cm.colors[13], label='OrientExp', fill='false',hatch='XX')
	
	base = mpatches.Patch(facecolor='C7', label='Plain')
	plt.legend(handles=[base, rects2, rects3, rects4, rects5], prop={'size': 22}, bbox_to_anchor=(0.025, 0.86, 0.9, .03), loc=3,
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
	plt.savefig('lat.pdf') 
	plt.show()
elif(0):
	n_groups = 2

	#x1 = (1, 1)
	x2= (62, 66)
	x3= (59, 62)
	x5= (49, 53)
	x4= (20, 42.5)
	#x2= (48, 51)
	#x3= (44, 50)
	#x5= (35, 43)

	#x6 = (0.84, 0.88) # Orient Exp 
	cm = plt.cm.get_cmap('tab20')

	# create plot
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.18
	opacity = 1

	# rects1 = plt.bar(index, x1, bar_width,
	# alpha=opacity,
	# color='C7',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='Plain')

	rects2 = plt.bar(index, x2, bar_width,
	alpha=opacity,
	color=cm.colors[1],
	fill='false',
	hatch='///',
	edgecolor = "black",
	linewidth=2.0,
	label='AdvFg',
	zorder=3)
	rects3 = plt.bar(index + 1*bar_width, x3, bar_width,
	alpha=opacity,
	color=cm.colors[4],
	fill='false',
	hatch='|',
	edgecolor = "black",
	linewidth=2.0,
	label='FCRL',
	zorder=3)
	rects4 = plt.bar(index + 3*bar_width, x4, bar_width,
	alpha=opacity,
	color=cm.colors[13],
	fill='false',
	hatch='o',
	edgecolor = "black",
	linewidth=2.0,
	label='LoLa',
	zorder=3)
	rects5 = plt.bar(index + 2*bar_width, x5, bar_width,
	alpha=opacity,
	color=cm.colors[6],
	fill='false',
	hatch='..',
	edgecolor = "black",
	linewidth=2.0,
	label='Orient',
	zorder=3)
	# rects6 = plt.bar(index + 5*bar_width, x6, bar_width,
	# alpha=opacity,
	# color='C5',
	# fill='false',
	# hatch='XX',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='OrientExp',
	# zorder=3)
	plt.xlabel('')
	plt.ylim([10,104])
	plt.ylabel('Private Attribue\n Accuracy (%)', fontsize=24)
	#plt.title('α=0.5', fontsize=20)
	ax.yaxis.set_major_locator(MultipleLocator(10))
	ax.yaxis.set_minor_locator(MultipleLocator(5))
	#ax.bar_label(rects4,
    #         padding=8, color='b', fontsize=14)
	plt.yticks(fontsize=22)
	plt.xticks(index + 1.5*bar_width, ('Resnet-18', 'VGG16'),fontsize=22)
	plt.xlim([0-1*bar_width,1+4*bar_width])
	x2_patch = mpatches.Patch(facecolor=cm.colors[1], label='AdvFg', fill='false',hatch='///')
	x3_patch = mpatches.Patch(facecolor=cm.colors[4], label='FCRL', fill='false',hatch='|')
	x4_patch = mpatches.Patch(facecolor=cm.colors[13], label='LoLa', fill='false',hatch='o')
	x5_patch = mpatches.Patch(facecolor=cm.colors[6], label='Orient', fill='false',hatch='..')
#	x6_patch = mpatches.Patch(facecolor=cm.colors[13], label='OrientExp', fill='false',hatch='XX')
	
	#base = mpatches.Patch(facecolor='C7', label='Plain')
	plt.legend(handles=[rects2, rects3, rects5, rects4], prop={'size': 22}, bbox_to_anchor=(0.02, 0.66, 0.7, .03), loc=3,
	       ncol=2, borderaxespad=0.)
	#plt.legend(loc=1)
	plt.grid(color = 'gray', axis='y', which= 'major', linestyle = '--', linewidth = 0.5, zorder=0)
	plt.grid(color = 'gray', axis='y', which= 'minor', linestyle = '--', linewidth = 0.1,zorder=0)

	#ax2 = ax1.twinx()
	#ax2.axhline(y=20000)
	#ax.set_yscale('log')
	#ax.annotate('', xy=(bar_width, 0.91),  xycoords='data',
	#            xytext=(0.15,0.85), textcoords='axes fraction',
	#            arrowprops=dict(facecolor='black', shrink=0.05),
	#            horizontalalignment='right', verticalalignment='top',
	#            )
	plt.tight_layout()
	plt.savefig('priv1.pdf') 
	plt.show()
elif(0):
	n_groups = 3

	x1 = (1, 1, 1) # acc, lat, priv
	x2= (1.11, 1,1)
	#x3= (59, 62)
	#x5= (49, 53)

	#x2= (48, 51)
    #x3= (44, 50)
    #x5= (35, 41)


	#x6 = (0.84, 0.88) # Orient Exp 
	cm = plt.cm.get_cmap('tab20')

	# create plot
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.25
	opacity = 1

	# rects1 = plt.bar(index, x1, bar_width,
	# alpha=opacity,
	# color='C7',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='Plain')

	# rects2 = plt.bar(index, x2, bar_width,
	# alpha=opacity,
	# color=cm.colors[1],
	# fill='false',
	# hatch='///',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='AdvFg',
	# zorder=3)
	# rects3 = plt.bar(index + 1*bar_width, x3, bar_width,
	# alpha=opacity,
	# color=cm.colors[4],
	# fill='false',
	# hatch='|',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='FCRL',
	# zorder=3)
	# rects4 = plt.bar(index + 3*bar_width, x4, bar_width,
	# alpha=opacity,
	# color=cm.colors[13],
	# fill='false',
	# hatch='o',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='LoLa',
	# zorder=3)
	rects5 = plt.bar(index, x1, bar_width,
	alpha=opacity,
	color=cm.colors[6],
	fill='false',
	hatch='..',
	edgecolor = "black",
	linewidth=2.0,
	label='Orient',
	zorder=3)
	rects6 = plt.bar(index + bar_width, x2, bar_width,
	alpha=opacity,
	color=cm.colors[15],
	fill='false',
	hatch='XX',
	edgecolor = "black",
	linewidth=2.0,
	label='OrientExp',
	zorder=3)

	plt.xlabel('')
	plt.ylim([.05,1.39])
	plt.ylabel('Normalized Ratio\n (w.r.t. Orient)', fontsize=20)
	#plt.title('α=0.5', fontsize=20)
	ax.yaxis.set_major_locator(MultipleLocator(.2))
	ax.yaxis.set_minor_locator(MultipleLocator(.1))
	#ax.bar_label(rects4,
    #         padding=8, color='b', fontsize=14)
	plt.yticks(fontsize=18)
	plt.xticks(index+.5*bar_width , ('Accuracy', 'Latency', 'Privacy'),fontsize=20)
	plt.xlim([0-1*bar_width,2+2*bar_width])
	x2_patch = mpatches.Patch(facecolor=cm.colors[1], label='AdvFg', fill='false',hatch='///')
	x3_patch = mpatches.Patch(facecolor=cm.colors[4], label='FCRL', fill='false',hatch='|')
	#x4_patch = mpatches.Patch(facecolor=cm.colors[13], label='LoLa', fill='false',hatch='o')
	x5_patch = mpatches.Patch(facecolor=cm.colors[6], label='Orient', fill='false',hatch='..')
	x6_patch = mpatches.Patch(facecolor=cm.colors[15], label='OrientExp', fill='false',hatch='XX')
	
	#base = mpatches.Patch(facecolor='C7', label='Plain')
	plt.legend(handles=[rects5,rects6], prop={'size': 20}, bbox_to_anchor=(0.04, 0.86, 0.9, .03), loc=3,
	       ncol=2, borderaxespad=0.)
	#plt.legend(loc=1)
	plt.grid(color = 'gray', axis='y', which= 'major', linestyle = '--', linewidth = 0.5, zorder=0)
	plt.grid(color = 'gray', axis='y', which= 'minor', linestyle = '--', linewidth = 0.1,zorder=0)

	#ax2 = ax1.twinx()
	#ax2.axhline(y=20000)
	#ax.set_yscale('log')
	#ax.annotate('', xy=(bar_width, 0.91),  xycoords='data',
	#            xytext=(0.15,0.85), textcoords='axes fraction',
	#            arrowprops=dict(facecolor='black', shrink=0.05),
	#            horizontalalignment='right', verticalalignment='top',
	#            )
	plt.tight_layout()
	plt.savefig('sysp.pdf') 
	plt.show()
elif(0):
	n_groups = 2

	x1 = (1, 1)
	x2 = (13.4,21.7) # AdvFg
	x3 = (13.4,21.7) # FCRL
	x4 = (1,1) # HE (LOLA)
	x5 = (4.5,6.3) # Orient
	#print(x3[0]/x3[1])
	#x6 = (0.84, 0.88) # Orient Exp 
	cm = plt.cm.get_cmap('tab20')

	# create plot
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.15
	opacity = 1

	rects1 = plt.bar(index, x1, bar_width,
	alpha=opacity,
	color=cm.colors[6],
	edgecolor = "black",
	fill='false',
	linewidth=2.0,
	hatch='..',
	label='Orient',
	zorder=3)

	rects2 = plt.bar(index + bar_width, x2, bar_width,
	alpha=opacity,
	color=cm.colors[1],
	fill='false',
	hatch='///',
	edgecolor = "black",
	linewidth=2.0,
	label='AdvFg',
	zorder=3)
	rects3 = plt.bar(index + 2*bar_width, x3, bar_width,
	alpha=opacity,
	color=cm.colors[4],
	fill='false',
	hatch='|',
	edgecolor = "black",
	linewidth=2.0,
	label='FCRL',
	zorder=3)
	rects4 = plt.bar(index + 3*bar_width, x4, bar_width,
	alpha=opacity,
	color=cm.colors[13],
	fill='false',
	hatch='o',
	edgecolor = "black",
	linewidth=2.0,
	label='LoLa',
	zorder=3)
	rects5 = plt.bar(index + 4*bar_width, x5, bar_width,
	alpha=opacity,
	color=cm.colors[15],
	fill='false',
	hatch='XX',
	edgecolor = "black",
	linewidth=2.0,
	label='OrientExp',
	zorder=3)
	# rects6 = plt.bar(index + 5*bar_width, x6, bar_width,
	# alpha=opacity,
	# color='C5',
	# fill='false',
	# hatch='XX',
	# edgecolor = "black",
	# linewidth=2.0,
	# label='OrientExp',
	# zorder=3)
	plt.xlabel('')
	plt.ylim([0,30])
	plt.ylabel('Energy Consumption\n (w.r.t. Orient)', fontsize=20)
	#plt.title('Constant encoder', fontsize=20)
	ax.yaxis.set_major_locator(MultipleLocator(5))
	ax.yaxis.set_minor_locator(MultipleLocator(1))
	#ax.bar_label(rects4,
    #         padding=8, color='b', fontsize=14)
	plt.yticks(fontsize=18)
	plt.xticks(index + 2.4*bar_width, ('Resnet-18', 'VGG16'),fontsize=20)
	plt.xlim([0-1.5*bar_width,1+5.5*bar_width])
	x2_patch = mpatches.Patch(facecolor=cm.colors[1], label='AdvFg', fill='false',hatch='///')
	x3_patch = mpatches.Patch(facecolor=cm.colors[4], label='FCRL', fill='false',hatch='|')
	x4_patch = mpatches.Patch(facecolor=cm.colors[13], label='LoLa', fill='false',hatch='o')
	x5_patch = mpatches.Patch(facecolor=cm.colors[6], label='Orient', fill='false',hatch='..')
	x6_patch = mpatches.Patch(facecolor=cm.colors[15], label='OrientExp', fill='false',hatch='XX')
	
	base = mpatches.Patch(facecolor='C7', label='Plain')
	plt.legend(handles=[rects1, rects2, rects3, rects4,rects5 ], prop={'size': 20}, bbox_to_anchor=(0.05, 0.8, 0.9, .03), loc=3,
	       ncol=2, borderaxespad=0.)
	#plt.legend(loc=1)
	plt.grid(color = 'gray', axis='y', which= 'major', linestyle = '--', linewidth = 0.5, zorder=0)
	plt.grid(color = 'gray', axis='y', which= 'minor', linestyle = '--', linewidth = 0.1,zorder=0)
	#ax.set_yscale('log')
	#ax.annotate('', xy=(bar_width, 0.91),  xycoords='data',
	#            xytext=(0.15,0.85), textcoords='axes fraction',
	#            arrowprops=dict(facecolor='black', shrink=0.05),
	#            horizontalalignment='right', verticalalignment='top',
	#            )
	plt.tight_layout()
	plt.savefig('energy.pdf') 
	plt.show()

