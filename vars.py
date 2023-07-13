import os
from dotenv import load_dotenv

load_dotenv()

env_vars = dict(os.environ) # using environmental variables for security