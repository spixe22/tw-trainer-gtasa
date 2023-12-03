import random
from functools import reduce
from services.process_service import ProcessService
from services.memory_service import MemoryService
from commands import HealthCommand, ArmorCommand, MoneyCommand, FlyingCarsCommand
from exceptions import ProcessNotFoundException

PROCESS_NAME = 'gta_sa.exe'

commands_dict = {
    "health": HealthCommand,
    "armor": ArmorCommand,
    "money": MoneyCommand,
    "flyingcars": FlyingCarsCommand,
}

def main():
    try:
        process_service = ProcessService()
        game_process = process_service.get_process_by_name(PROCESS_NAME)
        memory_service = MemoryService(game_process)

        # Commands list
        commands: dict = reduce(lambda acc, command: {**acc, command: commands_dict[command](game_process, memory_service)}, commands_dict.keys(), {})
        # Health command
        healthCommand = commands.get('health')
        healthCommand.execute(random.choice([25, 50, 75]))

    except ProcessNotFoundException as e:
        print(e)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

