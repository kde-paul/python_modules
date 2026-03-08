if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    players = ['alice', 'bob', 'charlie', 'diana']

    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
        }

    actives = {
        "alice": True,
        "bob": True,
        "charlie": True,
        "diana": False
    }

    achievements = {
        "alice": "level_10",
        "bob": "first_kill",
        "charlie": "boss_slayer",
        "diana": "first_kill"
        }

    categories = {
        "high": 3,
        "medium": 2,
        "low": 1
    }

    ach_cat = {
        "boss_slayer": "high",
        "level_10": "medium",
        "first_kill": "low"
    }

    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north"
    }

    print("=== List Comprehension Examples ===")
    high_scorers = [dict_key for dict_key in scores if scores[dict_key] > 2000]
    print("High scorers (>2000):", high_scorers)
    scores_doubled = [scores[dict_key] * 2 for dict_key in scores]
    print("Scores doubled:", scores_doubled)
    active_players = [dict_key for dict_key in actives
                      if actives[dict_key] is True]
    print("Active players:", active_players)

    print("\n=== Dict Comprehension Examples ===")
    top_3 = {player: val for i, (player, val) in
             enumerate(scores.items()) if i < 3}
    print("Player scores:", top_3)
    print("Score categories:", categories)
    top_3_ach = {player: val
                 for i, (player, val) in
                 enumerate(achievements.items()) if i < 3}
    ach_counts = {player: categories[ach_cat[achievements]]
                  for player, achievements in top_3_ach.items()}
    for player in ach_counts:
        if ach_counts[player] == 1:
            ach_counts[player] = 3
        elif ach_counts[player] == 2:
            ach_counts[player] = 5
        else:
            ach_counts[player] = 7
    print("Achievement counts:", ach_counts)

    print("\n=== Set Comprehension Examples ===")
    unique_players = {player for player in players}
    print("Unique players:", unique_players)
    unique_achiev = {achievements[achievement] for achievement in achievements}
    print("Unique achievements:", unique_achiev)
    active_regions = {regions[player] for player in active_players}
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")
    print("Total players:", len(players))
    print("Total unique achievements:", len(unique_achiev))
    total_scores = [scores[player] for player in scores]
    average_score = sum(total_scores) / len(total_scores)
    print("Average score:", average_score)
    top_performer = max(scores, key=scores.get)
    top_performer_ach_counter = 0
    for player in achievements:
        if player == top_performer:
            top_performer_ach_counter += 1
    print(f"Top performer: {top_performer} \
({scores[top_performer]} points, {top_performer_ach_counter} achievements)")
