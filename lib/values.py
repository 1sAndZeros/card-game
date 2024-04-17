values = {
    key: i + 1
    for (i, key) in enumerate(
        ["Ace"] + list(range(2, 11)) + ["Jack", "Queen", "King"]
    )
}

suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
