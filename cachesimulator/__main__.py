#!/usr/bin/env python3

import argparse

from cachesimulator.simulator import Simulator


# Parse command-line arguments passed to the program
def parse_cli_args():

    parser = argparse.ArgumentParser()

    #L1 cache
    parser.add_argument(
        "--cache-size-l1", type=int, required=True, help="the size of L1 cache in words"
    )

    parser.add_argument(
        "--num-blocks-per-set-l1", type=int, default=1, help="the number of blocks per set in L1 cache"
    )

    parser.add_argument(
        "--num-words-per-block-l1",
        type=int,
        default=1,
        help="the number of words per block in L1 cache",
    )

    # L2 cache
    parser.add_argument(
        "--cache-size-l2", type=int, required=True, help="the size of L2 cache in words"
    )

    parser.add_argument(
        "--num-blocks-per-set-l2", type=int, default=1, help="blocks per set in L2 cache"
    )

    parser.add_argument(
        "--num-words-per-block-l2",
        type=int,
        default=1,
        help="the number of words per block in L2 cache",
    )

    # Word addresses
    parser.add_argument(
        "--word-addrs",
        nargs="+",
        type=int,
        required=True,
        help="one or more base-10 word addresses",
    )

    parser.add_argument(
        "--num-addr-bits",
        type=int,
        default=1,
        help="the number of bits in each given word address",
    )

    parser.add_argument(
        "--replacement-policy",
        choices=("lru", "mru"),
        default="lru",
        # Ignore argument case (e.g. "mru" and "MRU" are equivalent)
        type=str.lower,
        help="the cache replacement policy (LRU or MRU)",
    )

    return parser.parse_args()


def main():

    cli_args = parse_cli_args()

    sim = Simulator()

    l1_cache_params = (
        cli_args.num_blocks_per_set_l1,
        cli_args.num_words_per_block_l1,
        cli_args.cache_size_l1,
        cli_args.replacement_policy,
    )

    l2_cache_params = (
        cli_args.num_blocks_per_set_l2,
        cli_args.num_words_per_block_l2,
        cli_args.cache_size_l2,
        cli_args.replacement_policy,
    )

    sim.run_2level_simulation(
        l1_cache_params=l1_cache_params,
        l2_cache_params=l2_cache_params,
        num_addr_bits=cli_args.num_addr_bits,
        word_addrs=cli_args.word_addrs,
    )


if __name__ == "__main__":
    main()
