import yaml

from framework_mapper import map_framework


with open("threat_rules.yaml", "r") as f:
    RULES = yaml.safe_load(f)["rules"]


def extract_asset_types(architecture):

    asset_types = set()

    for node in architecture["nodes"]:
        asset_types.add(node["type"])

    return asset_types


def evaluate_rules(asset_types):

    detected = []

    for rule in RULES:

        required = set(rule["requires"])

        if required.issubset(asset_types):

            threat = rule["threat"]

            framework = map_framework(threat["id"])

            detected.append({

                "id": threat["id"],

                "name": threat["name"],

                "severity": threat["severity"],

                "reason": threat["reason"],

                "framework": framework
            })

    return detected


def analyze_architecture(architecture):

    asset_types = extract_asset_types(architecture)

    threats = evaluate_rules(asset_types)

    return threats