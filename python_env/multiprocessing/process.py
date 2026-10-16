# roaster_audit.py
import multiprocessing
import time

def audit_branch_roaster(branch_name, duration):
    """Simulate running an automated diagnostic audit on a branch roaster."""
    print(f"[{branch_name}] Starting roaster audit...")
    time.sleep(duration) # Simulate audit delay
    print(f"[{branch_name}] Audit complete!")

'''Note: In Python, you must always wrap process creations inside the 
if __name__ == "__main__": guard to prevent infinite process loops on Windows.'''


if __name__ == "__main__":
    # Create two separate processes (True parallel execution)
    p1 = multiprocessing.Process(target=audit_branch_roaster, args=("Branch-Alpha", 2))
    p2 = multiprocessing.Process(target=audit_branch_roaster, args=("Branch-Beta", 1))

    # Launch the processes
    p1.start()
    p2.start()

    # Wait for both to complete
    p1.join()
    p2.join()

    print("All branch roaster diagnostics complete.")