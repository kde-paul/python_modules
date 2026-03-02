if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
        }
    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")
    all_unique = alice.union(charlie).union(bob)

    print("All unique achievements:", all_unique)
    print("Total unique achievements:", len(all_unique))

    print(
        "\nCommon to all players:",
        alice.intersection(bob).intersection(charlie)
        )
    inter_ab = alice.intersection(bob)
    inter_ac = alice.intersection(charlie)
    inter_bc = bob.intersection(charlie)
    all_inter = inter_ab.union(inter_ac).union(inter_bc)
    print("Rare achievements (1 player):", all_unique.difference(all_inter))

    print("\nAlice vs Bob common:", alice.intersection(bob))
    print("Alice unique:", alice.difference(bob))
    print("Bob unique:", bob.difference(alice))
