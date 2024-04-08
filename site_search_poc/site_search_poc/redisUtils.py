import redis

def RedisClient():
    client = redis.StrictRedis(host='scrapy-demo.redis.cache.windows.net',
            port=6380, db=0, password='', ssl=True)
#     client.ping()
#     client.rpush('mycrawler:start_urls', 'https://pulsar.apache.org')
    # client.lpush('mycrawler:start_urls', "https://quotes.toscrape.com/page/1/")
    
    # client.rpush('my_list', 'element5')
    list_values = client.lrange('mycrawler:start_urls', 0, -1)

    # Print the values
    for value in list_values:
        print(value.decode())
    
RedisClient()