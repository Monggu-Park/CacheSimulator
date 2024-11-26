#!/usr/bin/env python3

import argparse

from cachesimulator.simulator import Simulator


# Parse command-line arguments passed to the program
def parse_cli_args():
    parser = argparse.ArgumentParser()

    # 기존 L1 캐시 관련 인자
    parser.add_argument("--cache-size", type=int, required=True, help="L1 cache size")
    parser.add_argument(
        "--num-blocks-per-set", type=int, default=1, help="L1 blocks per set"
    )
    parser.add_argument(
        "--num-words-per-block", type=int, default=1, help="L1 words per block"
    )
    parser.add_argument(
        "--word-addrs",
        nargs="+",
        type=int,
        required=True,
        help="Word addresses in base-10",
    )
    parser.add_argument(
        "--num-addr-bits",
        type=int,
        default=1,
        help="Number of bits in each word address",
    )
    parser.add_argument(
        "--replacement-policy",
        choices=("lru", "mru"),
        default="lru",
        type=str.lower,
        help="Replacement policy for cache",
    )

    return parser.parse_args()


def main():
    cli_args = parse_cli_args()
    sim = Simulator()
    sim.run_2level_simulation(**vars(cli_args))


if __name__ == "__main__":
    main()

