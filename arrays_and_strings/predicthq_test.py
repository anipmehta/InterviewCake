from predicthq import Client

phq = Client(access_token="dGfUEpQxUUw6ZMeMQd7ChLArsq3KVj")
emotions_to_category_dict = {"Introvert": ["Sports", "Music"]}

for emotion in emotions_to_category_dict.keys():
    for category in emotions_to_category_dict[emotion]:
        for event in phq.events.search(q=category):
            try:
                print('Title - {} : Description - {} : Location - {}'.format(str(event.title), str(event.description), str(event.location)))
            except:
                continue