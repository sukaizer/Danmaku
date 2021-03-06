import pygame
import numpy as np
from Enemy import *
from Game import *
import random


def bullet_to_player(game, enemy):
    return angle_direction(enemy.rect.x + enemy.rect.width/2, enemy.rect.y + enemy.rect.height/2, game.player.rect.x + game.player.rect.width/2, game.player.rect.y + game.player.rect.height/2)


def angle_direction(x1, y1, x2, y2):
    line = np.array([1, 0])
    d = np.array([x2 - x1, y2 - y1])
    angle = np.arctan2(d[1] - line[1], d[0] - line[0])
    return angle



def bulletPattern0():
    """bullet shot randomly"""
    angle = random.random() * 2 * np.pi
    return angle

def bulletpattern_player(stage, enemy, v, cooldown, asset):
    if stage.time % cooldown == 0:
        enemy.create_bullet(enemy.rect.x + enemy.rect.width/2, enemy.rect.y + enemy.rect.height/2, bullet_to_player(stage, enemy), v, asset)

def bulletpattern_circle(stage, enemy, v, qtt, asset):
    for i in range(qtt):
        enemy.create_bullet(enemy.rect.x + enemy.rect.width/2, enemy.rect.y + enemy.rect.height/2, 2*np.pi*i/qtt, v, asset)