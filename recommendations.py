# A dictionary of movie critics and their ratings of a small
from math import sqrt

# function for calculating (Euclidean Distance Score) distance-based similarity score for person1 and person2
def similarity_distance(input_recs, person1, person2):
    # Gather list of shared_items
    shared_items = {}
    for item_key in input_recs[person1]:
        if item_key in input_recs[person2]:
            shared_items[item_key] = 1
    # Return 0 if no common ratings
    if len(shared_items) == 0:
        return 0

    # Add the squares of the differences
    sum_of_squares = sum(pow(input_recs[person1][item_key]- input_recs[person2][item_key], 2)
                         for item_key in input_recs[person1]
                         if item_key in input_recs[person2])

    # Return the Euclidean Distance Score
    return 1/(1 + sqrt(sum_of_squares))


# function for calculating (Pearson correlation coefficient) for p1 and p2
def similarity_pearson(input_recs, p1, p2):
    # Gather list of shared_items
    shared_items = {}
    for each_critic_movie_rating_key in input_recs[p1]:
        if each_critic_movie_rating_key in input_recs[p2]:
            shared_items[each_critic_movie_rating_key] = 1

    # Were any matches found?
    match_length = len(shared_items)
    if match_length == 0:
        return 0

    # Add up all of the ratings for each person
    sum_p1 = sum([input_recs[p1][each_critic_movie_rating_key] for each_critic_movie_rating_key in shared_items])
    sum_p2 = sum([input_recs[p2][each_critic_movie_rating_key] for each_critic_movie_rating_key in shared_items])

    # Sum up the squares
    sqr_sum_p1 = sum([pow(input_recs[p1][each_critic_movie_rating_key], 2) for each_critic_movie_rating_key in shared_items])
    sqr_sum_p2 = sum([pow(input_recs[p2][each_critic_movie_rating_key], 2) for each_critic_movie_rating_key in shared_items])



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