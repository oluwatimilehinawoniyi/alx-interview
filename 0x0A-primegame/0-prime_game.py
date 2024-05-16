#!/usr/bin/python3
"""
Prime Game

Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and
removing that number and its multiples from the set.
The player that cannot make a move loses the game.

This script determines the winner of multiple rounds
of the game and returns the player who won the most rounds.
"""


def sieve_of_eratosthenes(n):
    """
    Compute all prime numbers up to a given limit using
    the Sieve of Eratosthenes algorithm.

    Args:
    n (int): The upper limit for calculating prime numbers.

    Returns:
    list: A list of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def play_game(n, primes):
    """
    Simulate a single game round with a given
    upper limit and a list of prime numbers.

    Args:
    n (int): The upper limit of the set of consecutive integers.
    primes (list): A list of prime numbers up to the maximum possible n.

    Returns:
    int: 0 if Ben wins, 1 if Maria wins.
    """
    board = [True] * (n + 1)
    player_turn = 0  # 0 for Maria, 1 for Ben
    current_prime_index = 0

    while True:
        # Find the next available prime number
        while (current_prime_index < len(primes) and
                primes[current_prime_index] <= n and
                not board[primes[current_prime_index]]):
            current_prime_index += 1
        if (current_prime_index == len(primes) or
                primes[current_prime_index] > n):
            break

        prime = primes[current_prime_index]
        # Remove the prime and its multiples
        for multiple in range(prime, n + 1, prime):
            board[multiple] = False

        # Switch turn
        player_turn = 1 - player_turn

    return player_turn  # 0 if Ben wins, 1 if Maria wins


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the game.

    Args:
    x (int): The number of rounds.
    nums (list):
        A list of integers, each representing the upper limit of a round.

    Returns:
    str:
        The name of the player that won the most rounds,
        or None if there is no clear winner.
    """
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            winner = play_game(n, primes)
            if winner == 1:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
