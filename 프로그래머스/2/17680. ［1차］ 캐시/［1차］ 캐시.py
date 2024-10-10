def solution(cacheSize, cities):
    answer = 0
    cache = []

    cities = [city.lower() for city in cities]

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            answer += 5
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                cache.append(city)

    return answer
