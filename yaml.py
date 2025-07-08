import yaml

with open("config.yaml", 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
print(config)