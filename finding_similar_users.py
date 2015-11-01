from recommendations import critics
from recommendations import similarity_distance
from recommendations import similarity_pearson
from math import sqrt

print critics['Lisa Rose']['Lady in the Water']
print critics['Toby']
print critics['Mick LaSalle']

# Euclidean Distance Score
#   Use to calculate the distance between 2 critics for 2 different movies to see how similar their tastes are.
#   The smaller the number, the closer they are.
# this example with be for Snakes and Dupree movies
distance_between_toby_lasalle = sqrt((pow(critics['Toby']['Snakes on a Plane']-critics['Toby']['You, Me and Dupree'], 2) +
                                      (pow(critics['Mick LaSalle']['Snakes on a Plane']-critics['Mick LaSalle']['You, Me and Dupree'], 2))))
print 'distance_between_toby_lasalle: ', distance_between_toby_lasalle

# This time make the values increase when people are similar
# Returns a value between 0 and 1. 1 means they match exactly
increasing_distance_between_toby_lasalle = 1/(1 + sqrt((pow(critics['Toby']['Snakes on a Plane']-critics['Toby']['You, Me and Dupree'], 2) +
                                      (pow(critics['Mick LaSalle']['Snakes on a Plane']-critics['Mick LaSalle']['You, Me and Dupree'], 2)))))
print 'increasing_distance_between_toby_lasalle', increasing_distance_between_toby_lasalle

print '------------------------------------------------------------------------------------------'

print 'similarity_distance', similarity_distance(critics, 'Lisa Rose', 'Gene Seymour')
print 'similarity_distance', similarity_distance(critics, 'Lisa Rose', 'Jack Matthews')
print 'similarity_distance', similarity_distance(critics, 'Lisa Rose', 'Claudia Puig')
print 'similarity_distance', similarity_distance(critics, 'Lisa Rose', 'Michael Phillips')
print 'similarity_distance', similarity_distance(critics, 'Lisa Rose', 'Mick LaSalle')
print 'similarity_distance', similarity_distance(critics, 'Lisa Rose', 'Toby')

print '------------------------------------------------------------------------------------------'

# Pearson correlation coefficient
#   Measures how well two sets of data fit on the same line.
print 'similarity_pearson', similarity_pearson(critics, 'Lisa Rose', 'Gene Seymour')
print 'similarity_pearson', similarity_pearson(critics, 'Lisa Rose', 'Jack Matthews')
print 'similarity_pearson', similarity_pearson(critics, 'Lisa Rose', 'Claudia Puig')
print 'similarity_pearson', similarity_pearson(critics, 'Lisa Rose', 'Michael Phillips')
print 'similarity_pearson', similarity_pearson(critics, 'Lisa Rose', 'Mick LaSalle')
print 'similarity_pearson', similarity_pearson(critics, 'Lisa Rose', 'Toby')