# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class MetacriticItem(Item):
    '''
    Class for the item retrieved by scrapy.
    '''
    # Here are the fields that will be crawled and stored
    date = Field()  # Release date
    title = Field()  # Game title
    link = Field()  # Link to individual game page
    cscore = Field()  # Critic score
    uscore = Field()   # User score
    desc = Field()  # Description of game
