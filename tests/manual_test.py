from tradelink import Portfolio
import asyncio
import logging
from datetime import datetime


async def main():
    logging.basicConfig(level=10)
    start_time = datetime.utcnow()
    x = Portfolio("f7ac1da1-59a5-43e4-a629-88e65a411e17", start_date=datetime(2023, 12, 1))
    print(await x.get_start_date())
    end_time = datetime.utcnow()
    print(end_time - start_time)


if __name__ == "__main__":
    asyncio.run(main())
