import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        i += 1
        await asyncio.sleep(i / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    man1 = asyncio.create_task(start_strongman("Ultra Power", 6))
    man2 = asyncio.create_task(start_strongman("Mega Power", 4))
    man3 = asyncio.create_task(start_strongman("Power Drish", 2))
    # await man1
    # await man2
    await man3  # Так как "Power Drish" выполняет поднятие шаров дольше всех то можно дождаться только его


asyncio.run(start_tournament())
