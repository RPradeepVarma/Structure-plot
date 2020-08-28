# Structure plot

The script will parse the tab-delimited input file with accession ids followed by structure output values. 

# Note
Script parse the structure output file (modified to provide the unique id for each row) and generate the plot. It is good to sort the input file (by column) before feeding to script. The k label and image size values are static and may need to change accordingly.

USAGE: python3 StructurePlot.py k2.txt

# Input
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

# Output
![PAV image](https://github.com/pradeepruperao/Structure-plot/blob/master/structure.jpg)
Structure.svg
