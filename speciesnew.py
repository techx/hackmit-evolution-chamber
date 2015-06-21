from flask import Markup
from itertools import product
import random
import genetic

geneSize = 10;
numPolygons = 125
numVertices = 3
canvasSize = 200

# maps strings to dictionaries
def domains():
    # use same domain for something to make it easier
    params = {}
    for x in xrange(0, numPolygons):
        for y in xrange(0, numVertices):
            params[str(x) + '#' + str(y) + 'vertex' + 'DiffX'] = range(canvasSize)
            params[str(x) + '#' + str(y) + 'vertex' + 'DiffY'] = range(canvasSize)
        params[str(x) + '#r'] = range(canvasSize)
        params[str(x) + '#g'] = range(canvasSize)
        params[str(x) + '#b'] = range(canvasSize)
        params[str(x) + '#a'] = range(canvasSize)
        params[str(x) + '#baseX'] = range(canvasSize)
        params[str(x) + '#baseY'] = range(canvasSize)
    return params

def mutate(parameters):
    new = dict(**parameters)
    for param in parameters:
        if random.random() < 0.02:
            new[param] += random.random() * canvasSize * 0.2 - 0.1 * canvasSize
    return new

def combine(parent_a, parent_b):
    new = genetic.combine_random(parent_a, parent_b)
    return new

# returns Markup object
def generate(parameters):
    polygons = ""
    objects = {}
    for param in parameters:
        paramparts = param.split('#')
        print "PARAM PARTS" + str(paramparts)
        objectkey = paramparts[0]
        if objectkey not in objects:
            objects[objectkey] = {}
        objects[objectkey][paramparts[1]] = parameters[param]

    for anobjectkey in objects:
        points = ""
        anobject = objects[anobjectkey]
        for x in xrange(0, numVertices):
            xval = anobject[str(x) + 'vertex' + 'DiffX']
            yval = anobject[str(x) + 'vertex' + 'DiffY']
            xval -= canvasSize / 2
            yval -= canvasSize / 2
            xval = anobject["baseX"] + xval
            yval = anobject["baseY"] + yval
            xval = min(max(0, xval), canvasSize - 1)
            yval = min(max(0, yval), canvasSize - 1)
            xstr = str(xval)
            ystr = str(yval)
            points += xstr + ',' + ystr + ' '

        r = int(anobject["r"] * 256. / canvasSize)
        g = int(anobject["g"] * 256. / canvasSize)
        b = int(anobject["b"] * 256. / canvasSize)
        a = float(anobject["a"] * 1. / canvasSize)

        newFiller = '''
        <polygon points="{points}" style="fill:rgba({r},{g},{b},{a});fill-rule:nonzero;" />
        '''.format(points=points, r=r, g=g, b=b, a=a)
        polygons += newFiller

    logo = '''
    <svg xmlns="http://www.w3.org/2000/svg" height="{height}" width="{width}" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
      <rect height="{width}" width="{height}" fill="#ecf0f1"/>
      {polygons}
    </svg>
    '''.format(width=canvasSize, height=canvasSize, polygons=polygons)
    return Markup(logo)
