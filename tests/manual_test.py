from typing import Awaitable
from tradelink import Portfolio
import asyncio
import logging
from datetime import datetime


async def main():
    logging.basicConfig(level=10)
    start_time = datetime.utcnow()
    portfolios: list[Awaitable[datetime]] = []
    for _ in range(100):
        portfolios.append(Portfolio("f7ac1da1-59a5-43e4-a629-88e65a411e17", start_date=datetime(2023, 12, 1)).get_end_date())
    
    x = await asyncio.gather(*portfolios)
    print(x)
    end_time = datetime.utcnow()
    print(end_time - start_time)


if __name__ == "__main__":
    asyncio.run(main())
