import os

def shutdown():
    print("Shutting down the system...")
    os.system("shutdown /s /t 1")   # For Windows

shutdown()