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