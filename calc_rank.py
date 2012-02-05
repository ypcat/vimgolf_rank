#!/usr/bin/python

import sys
import string

def main(overall_stat_strs, user_stat_strs):
    # stat string format: (challenge ID, rank, title of the challenge) per line
    
    user_stat = dict()
    rank      = 0
    for c in user_stat_strs:
        stats = c.split(",")
        if len(stats)<2:
            continue
        user_stat[stats[0]] = stats[1]
        print stats[0]
    for c in overall_stat_strs:
        stats = c.split(",")
        if len(stats)<3:
            continue
        if stats[0] in user_stat:
            rank_of_challenge = int(user_stat[stats[0]])
        else:
            rank_of_challenge = int(stats[1])
        rank += rank_of_challenge
        print "Rank of %s = %d" % (stats[2], rank_of_challenge)
    print "Total rank = %d" % rank

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print "Usage: calc_rank.py overall.stat userid.stat"
        sys.exit(1)
    overall_stat = open(sys.argv[1], "r")
    user_stat    = open(sys.argv[2], "r")
    main(overall_stat.read().split("\n"), user_stat.read().split("\n"))
