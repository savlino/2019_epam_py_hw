"""
example of implementing Observer pattern on python
"""


class MyTubeUser:
    def __init__(self, name):
        self.name = name

    def update(self, message: str):
        print(f"Dear {self.name}, {message}")


class YoutubeChannel:
    def __init__(self, channel_name: str, channel_owner: MyTubeUser):
        self.channel_name = channel_name
        self.channel_owner = channel_owner
        self.playlists = []
        self.subscribers = set()

    def subscribe(self, user):
        self.subscribers.add(user)

    def del_subscriber(self, user):
        if user not in self.subscribers:
            raise TypeError()
        self.subscribers.remove(user)

    def publish_video(self, video: str):
        self.notify(f"there is new video \
            on '{self.channel_name}' channel: '{video}'")

    def publish_playlist(self, playlist: dict):
        self.playlists.append(playlist)
        self.notify(f"there is new playlist \
            on '{self.channel_name}' channel: '{next(iter(playlist))}'")

    def notify(self, message: str):
        for sub in self.subscribers:
            if sub != self.channel_owner:
                sub.update(message)


if __name__ == '__main__':
    matt = MyTubeUser('Matt')
    john = MyTubeUser('John')
    erica = MyTubeUser('Erica')
    dogs_life = YoutubeChannel('All about dogs', matt)
    dogs_life.subscribe(john)
    dogs_life.subscribe(erica)
    dogs_nutrition_videos = [
        'What do dogs eat?', 'Which Pedigree pack to choose?'
    ]
    dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}
    for video in dogs_nutrition_videos:
        dogs_life.publish_video(video)
    dogs_life.publish_playlist(dogs_nutrition_playlist)
