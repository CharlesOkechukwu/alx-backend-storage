#!/usr/bin/env python3
"""module to provide stats about nginx logs stored in mongodb"""
from pymongo import MongoClient


def mongodb_nginx_logs():
    """print nginx logs stored in mongodb"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    logs = "{} logs\nMethods:".format(collection.count_documents({}))
    print(logs)
    for method in methods:
        count = collection.count_documents({"method": method})
        log_stat = "\tmethod {}: {}".format(method, count)
        print(log_stat)
    stat_count = collection.count_documents({"path": "/status"})
    status = "{} status check".format(stat_count)
    print(status)
    print("IPs:")
    ips = collection.aggregate([
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}, {'$limit': 10}
    ])
    for ip in ips:
        top_ip = "\t{}: {}".format(ip.get("_id"), ip.get("count"))
        print(top_ip)


if __name__ == '__main__':
    mongodb_nginx_logs()
