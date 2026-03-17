import time
import random

class BottleSpawner:
    def __init__(self, spawn_interval):
        self.spawn_interval = spawn_interval

    def spawn_bottle(self):
        bottle_id = random.randint(1, 1000)
        print(f'Bottle {bottle_id} spawned!')

    def start_spawning(self):
        while True:
            self.spawn_bottle()
            time.sleep(self.spawn_interval)

if __name__ == '__main__':
    spawner = BottleSpawner(spawn_interval=5)  # Spawns a bottle every 5 seconds
    spawner.start_spawning()