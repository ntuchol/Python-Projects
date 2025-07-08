import asyncio

async def my_coroutine():
    print("Starting coroutine")
    await asyncio.sleep(1)  # Simulate I/O operation
    print("Coroutine finished")

async def main():
    await asyncio.gather(my_coroutine(), my_coroutine()) # Execute coroutines concurrently

if __name__ == "__main__":
    asyncio.run(main())