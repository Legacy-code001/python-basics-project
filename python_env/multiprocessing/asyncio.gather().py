# concurrent_sensors.py

# We use asyncio.gather() to launch multiple coroutines concurrently, letting them overlap their waiting times.

import asyncio
import time

async def check_sensor_status(sensor_name, delay):
    print(f"Querying {sensor_name}...")
    await asyncio.sleep(delay) # Non-blocking wait
    print(f"[{sensor_name}] Query complete!")
    return f"{sensor_name} OK"

async def main():
    start_time = time.time()
    
    # Run all three sensor queries concurrently
    results = await asyncio.gather(
        check_sensor_status("Boiler-Temp", 2.0),
        check_sensor_status("Water-Pressure", 1.0),
        check_sensor_status("Cup-Dispenser", 1.5)
    )
    
    print("Audit Results:", results)
    print(f"Total time elapsed: {time.time() - start_time:.2f} seconds")

asyncio.run(main())