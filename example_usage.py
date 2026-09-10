from client import VietorisRipsFiltration

def main():
    print("=== Testing Vietoris-Rips Filtration ===")
    pts = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    vr = VietorisRipsFiltration(pts)

    e_small = vr.edges_at_radius(0.5)
    e_large = vr.edges_at_radius(1.05)

    print(f"Edges at eps=0.5: {e_small}")
    print(f"Edges at eps=1.05: {e_large}")

    assert len(e_small) == 0
    assert len(e_large) == 2
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
