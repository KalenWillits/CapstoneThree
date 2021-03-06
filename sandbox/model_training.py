# model_training.py



# __Load Environment__
import numpy as np
import pandas as pd
from library import *

cd_data = 'data/'
cd_figures = 'figures/'
cd_docs = 'docs/'
cd_models = 'models/'

# __Create Required Arguments__s
user_article = ProcessArticle('Unneeded input for training.')
read_article = ProcessArticle('Unneeded input for training.')

# __load in training data__
with open(cd_data+'train_data.txt', 'r+') as file:
    train_doc = file.read()

# __Process Training Data__
train_article = ProcessArticle(train_doc)

# __Instantiate And Train Model__
big_model = ChatBotModel(user_article=user_article,
read_article=read_article,
train_article=train_article,
train_article_name='train_data.txt',
cd_data=cd_data)

# __Save Word2Vec Vectors__
big_model.vectors.save(cd_models+'big_vectors.w2v')
