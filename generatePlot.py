def generatePlot(x, y, name):
    coordinates = ''
    for i in range(len(x)):
        coordinates = coordinates + \
            '({},{})'.format(x[i], y[i])
    plot = "\\addplot[color=red,mark=square,line width=2pt] \n coordinates {" + \
        coordinates + "}; \n \\addlegendentry{" + \
        name + "}\n"
    print("\\begin{"+"tikzpicture}[x=15cm, y=10cm]\n\\begin{" +
          "axis}[xmin=0, xmax="+str(max(x))+", ymin=0, ymax="+str(max(y))+",title=Comparativa, ymajorgrids=false,axis lines = left,legend pos=north west,width=.9\\textwidth,height=.4\\textheight,xlabel={Numero (datos)},ylabel={Tiempo (segundos)}]" + plot + " \end{"+"axis}\end{"+"tikzpicture}")


# Pasale 2 matrices de misma longitud y el nombre del grafico
generatePlot([1, 2, 3, 1, 12], [12, 2, 2, 1, 12], 'Burbuja')
