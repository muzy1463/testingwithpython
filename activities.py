#With unite tests, we test small units such as modules, functions, classes etc.

def eat(food, is_healthy):
    ending = "because YOLO!"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    return "I'm feeling refreshed after 1 hour of nap" if num_hours < 3 else "Ughhh, I overslept"
