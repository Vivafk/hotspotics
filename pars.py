def parser(keywords):
    import asyncio, time
    from telethon import TelegramClient

    client = TelegramClient('shtein', '21950170', 'b6a36f4b1ab40aebd3a75c3e47e698d2')
    client.start()
    mes1 = ''
    i = 0
    while i != 3:
        async def main():
            global mes1
            channel = await client.get_entity('fsstecru')
            messages = await client.get_messages(channel, limit=1)
            for i in keywords:
                mes = ''.join(list(x.text for x in messages))
                if mes1 != mes:
                    mes1 = mes
                    if i in mes1:
                        return mes1
                    else:
                        return ("Новых угроз не найдено")
                else:
                    return("Новых угроз не найдено")


        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        i += 1
        time.sleep(5)