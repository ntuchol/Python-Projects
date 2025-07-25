import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates a network delay
    print("Data fetched!")
    return {"data": "Sample data"}

async def process_data():
    print("Processing data...")
    await asyncio.sleep(1)  # Simulates processing time
    print("Data processed!")
    return "Processed data"

async def main():
    fetch_task = asyncio.create_task(fetch_data())
    process_task = asyncio.create_task(process_data())

    results = await asyncio.gather(fetch_task, process_task)
    print("Results:", results)

asyncio.run(main())
