from collections import defaultdict

def solution(genres, plays):
    genre_ids = defaultdict(list)
    genre_plays = defaultdict(int)
    
    for i in range(len(genres)):
        genre_ids[genres[i]].append(i)
        genre_plays[genres[i]] += plays[i]
        
    sorted_genres = sorted(genre_ids.keys(), key=lambda genre: genre_plays[genre], reverse=True)
    
    ans = []
    for genre in sorted_genres:
        ans += sorted(genre_ids[genre], key=lambda id: (-plays[id], id))[:2]
    
    return ans