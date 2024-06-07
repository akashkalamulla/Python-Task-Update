<<<<<<< HEAD
import os
import importlib

def discover_models():
  from app.models import user
  models_dir = os.path.dirname(__file__)
  for filename in os.listdir(models_dir):
    if filename.endswith('.py') and filename !='__init__.py':
      module_name = f'app.modules.{filename[:-3]}'
      importlib.import_module(module_name)

discover_models()
=======
import importlib
import os

def discover_models():
    models_dir = os.path.dirname(os.path.abspath(__file__))
    module_name = 'app.models'

    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            model_module_name = f"{module_name}.{filename[:-3]}"
            print(f"Importing model: {model_module_name}")  # Debugging line
            importlib.import_module(model_module_name)
>>>>>>> a2dae55 (commit)
