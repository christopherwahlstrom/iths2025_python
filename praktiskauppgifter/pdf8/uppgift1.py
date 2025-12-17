import functools

def log_decorator(func):
    """
    En decorator som loggar namnet på funktionen och dess argument.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Anropar funktion: '{func.__name__}'")
        print(f"[LOG] Argument: args={args}, kwargs={kwargs}")
        
        # Kör den faktiska funktionen
        result = func(*args, **kwargs)
        
        print(f"[LOG] Resultat: {result}")
        print("-" * 30)
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

@log_decorator
def subtract(x, y):
    return x - y

@log_decorator
def multiply(x, y):
    return x * y

if __name__ == "__main__":
    print("Testar log_decorator:\n")
    add(10, 5)
    subtract(20, 7)
    multiply(3, 3)
    
    print("Testar med kwargs (namngivna argument):")
    subtract(x=100, y=50)
