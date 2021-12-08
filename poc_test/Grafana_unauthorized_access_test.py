import json
from pocsuite3.api import init_pocsuite, start_pocsuite, get_results


def run_poc():
    config = {
        "url": ["http://139.196.240.149:3000/"],
        "poc": ["../plugins/unauthorized_access/Grafana_unauthorized_access.py"],
    }

    init_pocsuite(config)
    start_pocsuite()
    results = get_results()
    for result in results:
        result_dict = result.get("result")
        if result_dict:
            print(json.dumps(result_dict, indent=4))


if __name__ == "__main__":
    run_poc()
