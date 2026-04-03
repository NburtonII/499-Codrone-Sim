#!/usr/bin/env python3
"""
Lab script: Fly a square path with progress printouts.
This demonstrates the square flight capability using the DroneSquare module.
"""

import asyncio
import sys
import os

# Add the sdk/client directory to the path so we can import UserControl
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'client'))

from UserControl import UserControl

async def main():
    print("Starting square path lab...")

    # Initialize UserControl (this will connect to AirSim)
    uc = UserControl()
    uc.connect()

    try:
        # Fly the square using the Square command
        print("Initiating square flight...")
        await uc.commandParse("Square", 0)  # Duration not used for square
        print("Square flight completed successfully.")
    except Exception as e:
        print(f"Error during square flight: {e}")
    finally:
        # Close the connection
        uc.close()

if __name__ == "__main__":
    asyncio.run(main())
