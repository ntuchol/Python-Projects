import yaml

def generate_mosn_config(cluster_name, backend_addresses):
    config = {
        "listeners": [],
        "clusters": [
            {
                "name": cluster_name,
                "type": "SIMPLE",
                "lb_type": "RANDOM",
                "hosts": [
                    {"address": address, "port": 8080} for address in backend_addresses
                ]
            }
        ],
        "routes": []
    }
    return yaml.dump(config)

cluster_name = "my_backend_cluster"
backend_addresses = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
mosn_config = generate_mosn_config(cluster_name, backend_addresses)
print(mosn_config)