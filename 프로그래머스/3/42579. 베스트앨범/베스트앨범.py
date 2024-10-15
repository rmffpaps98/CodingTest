def solution(genres, plays):
    answer = []
    p = {}
    m = []

    for idx, genre in enumerate(genres):
        p[genre] = p.get(genre, 0) + plays[idx]
        m.append((plays[idx], genre, idx))

    sorted_genres = sorted(p.items(), key=lambda x: x[1], reverse=True)

    genre_count = {}
    
    for genre, _ in sorted_genres:
        genre_songs = [song for song in m if song[1] == genre]
        
        genre_songs = sorted(genre_songs, key=lambda x: -x[0]) 
        
        for i in range(min(2, len(genre_songs))):
            answer.append(genre_songs[i][2])

    return answer