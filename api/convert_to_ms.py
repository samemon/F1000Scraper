import datetime

epoch = datetime.datetime.utcfromtimestamp(0)
print(epoch)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


