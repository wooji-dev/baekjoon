def solution(genres, plays):
    answer = []
    genres_dict = {}

    for i in range(len(genres)):
        genres_dict.setdefault(genres[i], []).append((plays[i], i))

    # 장르별 총 재생 수 내림차순
    for genre, songs in sorted(genres_dict.items(), key=lambda x: -sum(p for p, _ in x[1])):
        # 재생 수 내림차순, 동점이면 고유 번호 오름차순
        songs.sort(key=lambda x: (-x[0], x[1]))
        for _, idx in songs[:2]:
            answer.append(idx)

    return answer