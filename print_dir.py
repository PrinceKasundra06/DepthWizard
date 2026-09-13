import os
BASE_DIR = os.path.dirname(os.path.abspath("website/backend/main.py"))
print(os.path.join(os.path.dirname(BASE_DIR), "frontend"))
