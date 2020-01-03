"""main module"""
from articulations import readArticulationsFile
from exprmap import createExpressionMap
articulations = readArticulationsFile()
exprsmap = createExpressionMap(articulations)