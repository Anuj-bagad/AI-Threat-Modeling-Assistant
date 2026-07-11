import yaml


with open("framework_mapping.yaml", "r") as f:
    FRAMEWORKS = yaml.safe_load(f)


def map_framework(threat_id):

    return FRAMEWORKS.get(threat_id, {})