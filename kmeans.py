from utils import distance, mean, sample, zip


def k_means(restaurants, k, max_updates = 100):
    old_centroids, n = [], 0
    centroids = [r[1] for r in sample(restaurants, k)]
    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        centroids_clusters = group_by_centroid(restaurants, old_centroids)
        centroids = [find_centroid(i) for i in centroids_clusters]
        n += 1
    return centroids

def find_centroid(cluster):
    restaurants_location = [i[1] for i in cluster]
    x = [i[0] for i in restaurants_location]
    y = [i[1] for i in restaurants_location]
    return [mean(x),mean(y)]

def group_by_centroid(restaurants, centroids):
    restaurants_location = [i[1] for i in restaurants]
    closest_centroids = [find_closest(i, centroids) for i in restaurants_location]
    return group_by_first(zip(closest_centroids, [i for i in restaurants]))

def group_by_first(pairs):
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]

def find_closest(location, centroids):
    return min(centroids, key = lambda x : distance(location, x))
