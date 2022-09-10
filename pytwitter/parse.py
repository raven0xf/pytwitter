import json
def json_dump(rsp, rspcode):
    print("[/] Response code: {}".format(rspcode))

    print(json.dumps(rsp.json(), indent=4, sort_keys=True))
