from cfg import accs
import aiohttp
import asyncio
import json

async def get_balance(session,acc):
    url = f'https://nearblocks.io/api/account/balance?address={acc}'
    async with session.get(url) as resp:
        assert resp.status == 200
        resp_text = await resp.text()
        balance = round(float(json.loads(resp_text)['balance']),2)
        sl.update({acc:balance})
    return resp_text


async def get_acc(accounts):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for acc in accounts:
            task = asyncio.create_task(get_balance(session,acc))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def get_res(accounts):
    global sl
    sl = {}
    output = '<b>        Ежедневный отчет\n(Аккаунты отсортированы по балансу сверху вниз):</b> \n'
    await get_acc(accounts)
    for i, acc in enumerate(sorted(sl.items(), key=lambda x: x[1], reverse=True)):
        if i == len(accs) - 3:
            output += '\n<b>АУТСАЙДЕРЫ:</b> \n'
        output += f'\n•<em>{acc[0].split(".")[0]}</em>: <b>{acc[1]}Ⓝ</b> \nКто работает:\n{accs[acc[0]]} '
        output += '\n——————————————————'
    return output
