import os

PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../")

MAP_DIR = os.path.join(PROJECT_DIR, './utils/levels/')

graphics_dir = os.path.join(PROJECT_DIR, './misc/game/graphics/')

print(PROJECT_DIR, "new", MAP_DIR)

def agent_settings(arglist, agent_name):
    if agent_name[-1] == "1": return arglist.model1
    elif agent_name[-1] == "2": return arglist.model2
    elif agent_name[-1] == "3": return arglist.model3
    elif agent_name[-1] == "4": return arglist.model4
    else: raise ValueError("Agent name doesn't follow the right naming, `agent-<int>`")

