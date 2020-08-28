
import svgwrite
import sys
import svgwrite
import operator
import numbers
from collections import defaultdict
from svgwrite import cm, mm

str=defaultdict(list) # Structure values
origin=[]
colors=['0,0,0','255,0,0','255,212,0','255,255,0','191,255,0','106,255,0','0,234,255','0,149,255','0,64,255','170,0,255','255,127,0','255,0,170','237,185,185','231,233,185','185,237,224','185,215,237','220,185,237','143,35,35','143,106,35','79,143,35','35,98,143','107,35,143','0,255,0','115,115,115','204,204,204','0,0,128','128,128,0','255,250,200','255,215,180']


def getstructure():
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.strip('\n')
			linedata = line.split('\t')
			#linedata2=linedata.split('\t')
			#print( linedata[1])
			str[linedata[0]].append(linedata[1:])
			
def rgbval(minimum, maximum, value):
	minimum, maximum = float(minimum), float(maximum)
	ratio = 2 * (value-minimum) / (maximum - minimum)
	b = int(max(0, 255*(1 - ratio)))
	r = int(max(0, 255*(ratio - 1)))
	g = 255 - b - r
	return r, g, b

def drawimg(name):
	svg_width=40*cm
	svg_hight=130*cm
	dwg = svgwrite.Drawing(name,(svg_width, svg_hight), debug=True)
	dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))	
	lines = dwg.add(dwg.g(stroke_width=5, stroke='green', fill='none'))
	text = dwg.add(dwg.g(font_family="sans-serif", font_size=20, fill='black'))
	text.add(dwg.text("K4", insert=(400, 400), font_size=90, font_weight='bold'))
	#print(val)
	#(maxval,minval)=getrange(val)
	row=500
	#ecol=0
	for id in str: # Each structure ID and values in list
		scol=300
		i=1
		for vallist in str[id]: # List of values for above id
			#print(id, vallist, "++++++++")
			for val in range(0,len(vallist)):
				#print(id, vallist, vallist[val], "++++++++")
				ecol=scol+(float(vallist[val])*500) # Set width of structure plot
				(r,g,b)=rgbval(1,100,i)
				#print(r,g,b, val, vallist)
				lines.add(dwg.line(start=(scol, row), end=(ecol, row),  stroke=svgwrite.rgb(r, g, b, '%'), stroke_width=10))
				#print(int(val), scol, row, ecol, row)
				scol=ecol
				i=i+40 # Set colours
				
		row=row + 10


    #Scale
	lines.add(dwg.line(start=(275, 500), end=(275, row), stroke_linecap='round', stroke='black', stroke_width=4))
	for i in range(500,row,500):
        label=int((i-500)/10)
		lines.add(dwg.line(start=(270, i), end=(275, i), stroke_linecap='round', stroke='black', stroke_width=4))
		text.add(dwg.text(label, insert=(250, i), font_size=50, text_anchor='end'))
	
	# Legend
	row=800
	for idx in range(0,len(origin)):
		orgval=origin[idx]
		#print(idx, origin[idx])
		orgval=idx
		orgval=orgval+1
		(a,b,c)=rgbval(1,30,orgval)
		#rgb1 = colors[idx].split(',')
		#print(rgb1[0],rgb1[1],rgb1[2],idx)
		lines.add(dwg.line(start=(scol-400, row), end=(ecol-400, row),  stroke=svgwrite.rgb(a,b,c, '%'), stroke_width=8))
		#text.add(dwg.text(origin[idx], insert=(ecol-400, row), font_size=40))
		text.add(dwg.text(colors[idx], insert=(ecol-400, row), font_size=40))
		row=row+50
	lines.add(dwg.line(start=(scol-400, row), end=(ecol-400, row),  stroke="black", stroke_width=8))

	dwg.save()

# ======================
getstructure()
print("Finished parsing structure data")
drawimg('Structure.svg')
print("Image ready")

'''
AUTHOR: R.PRADEEP
CONTACT: r.pradeep@cgiar.org
USAGE: python3 StructureAnnotation.py k2.txt
DESCRIPTION: Script parse the structure output file (modified to provide the unique id for each row) and generate the plot. It is good to sort the input file (by column) before feeding to script.
The k label and image size values are static and may need to change accordingly.

INPUTFILE FORMAT: k2.txt
IDs	Val1	Val2
NSL54318        0.310601        0.689399
PI285042.3      0.408036        0.591964
PI285042        0.410141        0.589859
IS3923  0.422596        0.577404
SC35    0.423407        0.576593
PI665108        0.439546        0.560454
PI148084.3      0.443044        0.556956
SC283   0.447336        0.552664
PI148084        0.451514        0.548486
NSL51981        0.462085        0.537915
PI276820        0.486437        0.513563
PI276800        0.517266        0.482734
PI660602        0.551405        0.448595
NSL50449        0.559950        0.440050
PI285042.2      0.570699        0.429301



'''