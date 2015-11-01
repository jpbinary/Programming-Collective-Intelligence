# A dictionary of movie critics and their ratings of a small
from math import sqrt

# function for calculating distance-based similarity score for person1 and person2
def similarity_score(input_recs, person1, person2):
    # Gather list of shared_items
    shared_items = {}
    for item in input_recs[person1]:
        if item in input_recs[person2]:
            shared_items[item] = 1
    # Return 0 if no common ratings
    if len(shared_items) == 0:
        return 0

    # Add the squares of the differences
    sum_of_squares = sum(pow(input_recs[person1][item]-input_recs[person2][item], 2)
                         for item in input_recs[person1]
                         if item in input_recs[person2])

    return 1/(1 + sqrt(sum_of_squares))



# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}