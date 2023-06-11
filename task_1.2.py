from random import *

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02], ]

songs_random = sample(my_favorite_songs, 3)

total_time = sum([songs_random[i][1] for i in range(len(songs_random))])
print(f' Три песни звучат {int(total_time)} минут')