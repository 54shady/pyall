#!/usr/bin/env python
# coding=utf-8

from random import randint, sample


def main():
    # 找多个字典中的公共键
    # find out who get scores in every game
    # 找出每场比赛都有进球的球员
    name_list = ['jordan', 'iverson', 'kobe', 'carter', 'tmac', 'garnet']

    # Game 1 data
    # fetch at least a player from the name list
    name1 = sample(name_list, randint(1, 6))

    # map name and their scores into dict
    game1_scores = {name: randint(0, 100) for name in name1}
    print 'Game1 rank %s' % game1_scores

    # Game 2 data
    name2 = sample(name_list, randint(1, 6))
    game2_scores = {name: randint(0, 100) for name in name2}
    print 'Game2 rank %s' % game2_scores

    # Game 3 data
    name3 = sample(name_list, randint(1, 6))
    game3_scores = {name: randint(0, 100) for name in name3}
    print 'Game3 rank %s' % game3_scores

    # it's time to find out who get socres in every game
    # 方法一:使用集合的操作
    print game1_scores.viewkeys() & game2_scores.viewkeys() & game3_scores.viewkeys()

    # 方法二:使用map and reduce
    # get player name get scores in each game
    player_name = map(
        dict.viewkeys, [game1_scores, game2_scores, game3_scores])
    print player_name
    player_score_everygame = reduce(lambda a, b: a & b, player_name)
    print player_score_everygame


if __name__ == '__main__':
    main()
