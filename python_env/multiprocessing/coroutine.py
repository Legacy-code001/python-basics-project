# sensor_audit.py

# We define a coroutine using async def. We use await to pause execution, yielding control back to the event loop so other tasks can run.
import asyncio


async def check_sensor_status(sensor_name):
    """A coroutine simulating an IoT hardware status check."""
    print(f"Querying {sensor_name}...")
    await asyncio.sleep(1.0) # Pause here, letting other sensors be queried
    print(f"{sensor_name} is online and calibrated.")
    return "Status: OK"

async def main():
    # Calling the coroutine returns a coroutine object; "await" starts it
    status = await check_sensor_status("Boiler-Water-Sensor")
    print(status)

# Execute the main entry-point coroutine
asyncio.run(main())