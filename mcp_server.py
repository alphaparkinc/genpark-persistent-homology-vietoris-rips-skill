import sys
import json
from client import VietorisRipsFiltration

def handle_call(name, arguments):
    if name == "filtration":
        pts = [tuple(p) for p in arguments["points"]]
        eps = arguments.get("epsilon", 1.0)
        vr = VietorisRipsFiltration(pts)
        return {"edges": vr.edges_at_radius(eps)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
