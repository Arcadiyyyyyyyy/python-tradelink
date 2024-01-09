# TradeLink.pro API unofficial wrapper

### How to use 
Currently the package is being developed. \
Currently only async version is available. \
The easiest way to start is to fetch some indicator of the particular portfolio. 
Here is the easy example
```python
from tradelink import Portfolio
import asyncio


async def main():
    print(Portfolio("portfolio unique id").get_unrpnl_last_balance())


if __name__ == "__main__":
    asyncio.run(main())
```

### How to contribute
Simply create a branch, write some code, and open a pull request. \
If your PR ends up being merged - the package version will automatically be updated, and the package will be released.
