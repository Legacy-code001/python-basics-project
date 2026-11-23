def cadence_sum(n):
    total = 0
    for i in range(3, n+1, 3):
        total += i
        
    return total

def process_requisition(item, quantity):
    if not item:
        return "missing item"
    if quantity <= 0:
        return "invalid quantity"
    if quantity > 100:
        return "exceeds limit"
    return f"approved: {quantity} x {item}"


process_requisition('rifle', 5)
