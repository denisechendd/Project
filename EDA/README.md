# EDA: Visualization in Geopandas, Matplotlib & Bokeh

## Code Files
- Jupyter files **Bokeh_Static.ipynb**
  - Static choropleth map for year 2015
- Jupyter files **Analytics_Plot.ipynb**
  - Analytics on worldwide dataset from 2016 to 2019
- Python files **EDA_Plot.py**
  - Command: bokeh serve --show EDA_Plot.py
  - Dynamic choropleth Plot from 2016 to 2019

## Bokeh_Static Plot
### 1. Static choropleth map for year 2015
### Analytics:
From the plot below, we see that countries like Canada, Mexico, and Australia have a higher happiness score. For South America, and European countries, the overall score is distributed around Index 5 and 6. In Contrast, African countries like Niger, Chad, Mali, and Benin show a much lower happiness index. <br />
![GitHub Logo](photo/photo_1.png)
### 2. Scatter Plot of GDP & Happiness_Score Index in 2016
### Analytics:
We look into the correlation of GDP Growth and happiness levels score in 2016. As the countries are color-coded by regions, we can see that southeast countries have lower GDP growth followed by underlying happiness scores. Most countries in central and eastern Europe have GDP growth fall within 0.8 and 1.4 with a happiness score between 5 and 6. For the region of Western Europe, they tend to show a higher range of economic growth along with the happiness index. <br/>
![GitHub Logo](photo/photo_2.png)
### 3. Top and Bottom 10 Countries of Economy Index (GDP per capita)
### Analytics:
For the top 10 economy trend countries, ‘United Arab Emirate’ has shown the increasing trend with 0.68 growth on the economy from 2015 to 2018. ‘Myanmar’ has a rising rate with 0.41 on GDP per Capita growth as one only Asian country. Surprisingly, Sub-Saharan Africa countries like ‘Malawi’, ‘Guinea’, ‘Tanzania’ are the top 5 countries with the upward economic trend. <br>
We can see that countries with decreased economic trends are mostly in Africa. Bottom 5 countries like ‘Libya’, ‘Yemen’, ‘Kuwait’, ‘Jordan’, ‘Sierra Leone’ have lower Economy Index from 2015 to 2018. Four of those countries are located in the Middle East and Northern Africa.  <br>
![GitHub Logo](photo/photo_3.png)
### 4. UAE Yearly GDP Change
### Analytics:
Seeing the top and Bottom 10 Countries of Economy Index (GDP per capita growth), we closely look into the United Arab Emirate’s economic trend. In 1980, UAE shows the max GDP growth value among 40 years. However, the growth becomes negative in the range of the year 1982 to 1986. In the next 10 years, UAE shows a quite stable GDP growth around 0.1 to 0.2 rise. In the year 2009, there’s a plunge on GDP growth followed by the impact of the financial crisis. <br>
![GitHub Logo](photo/photo_4.png)



### Preprocessing
- remove HTML tags
- remove stopwords
- remove punctuation
- Stemming: improve structure of text

### Text features for deep learning model
- tokenize sentences
- tranform tokenized text into integers
- **pad sequences:** All text inpute features have same length
- Interger encoded text data for embedding layer
- transforms text data into embedding layer for deep learning Model

### Deep Learning Model
<img src=https://github.com/denisechendd/Project/blob/master/EDA/photo/photo_1.png height="250" width="550">
<img src=https://github.com/denisechendd/Project/blob/master/EDA/photo/photo_2.png height="250" width="550">
<img src=https://github.com/denisechendd/Project/blob/master/EDA/photo/photo_3.png height="250" width="550">
<img src=https://github.com/denisechendd/Project/blob/master/EDA/photo/photo_4.png height="250" width="550">
![GitHub Logo](photo/BiLSTM_model.png)
- ``Embedding(1000, 100 ,input_length=800)``
   - input words have 800 in each document
   - vocab size 1000 (with integer encoded words from 0 to 999)
   - a vector space of 100 for each word encoded
   - output is 2D, for 1D vector encoded for each word
- ``Bidirectional(LSTM(64))``: the output of bidirectional LSTM would be 64
  - updates graident based on the future outcome
  - Bidirectional LSTM concatenates the feedforward and backward embedding
- ``Dense(2, activation='softmax')``: final output layer
  - ``softmax``: activation function for class prediction, outputs the probability of each input belongs to the class, the higher result would be predicted class.
  - ``to_categorical``: Keras function turn the output label into categorical feature
  - output of the LSTM layer is two dimension; therefore the dense layer is set as 2, Otherwise, we need to **Flatten()** the layer into 1D for **Full Connected Layer**
- Loss Function : ``binary_crossentropy``
  - Used for binary classification problem

### Model Performance Comparison
1. Transfer text into tokenizers, transform tokenizer into integer encoded, and feed into pad sequences for same length of each input text
<img src=https://github.com/denisechendd/Project/blob/master/Sentiment%20Analysis/Doc2Vec_BiLSTM/photo/photo_1.png height="250" width="550">
2. Take doc2vec pretrained words embedding to feed as weights into the model (not update the learned word weights in this model)
<img src=https://github.com/denisechendd/Project/blob/master/Sentiment%20Analysis/Doc2Vec_BiLSTM/photo/photo_2.png height="250" width="550">
3. Take doc2vec pretrained words embedding to feed as weights into the model (update the learned word weights in this model) <br>Set parameter``trainable=True``
<img src=https://github.com/denisechendd/Project/blob/master/Sentiment%20Analysis/Doc2Vec_BiLSTM/photo/photo_3.png height="250" width="550">

### Analysis
First Approach | Second Approach | Third Approach
------------ | ------------- | -------------
*Overfitting on training data<br> *Validation Acc decrease with more epochs | *Validation Acc higher than Training Acc after 2nd epoch <br>**dropout rate is high so model is more robust to validation data** | * Validation Acc higher than Training Acc from 1st epoc <br>**dropout rate is high so model is more robust to validation data**

### Notes to improve model performance:
- Put Doc2Vec pretrained embedding into deep learning Model for more epochs
- Set pretrained words embedding to be trained into the embedding layer for more epochs
- Add more layers since training document is large (35000 messages for training and 15000 for test)
- Set dropout rate for robust model on training and validation dataset

### References:
- How to Use Word Embedding Layers for Deep Learning with Keras, <br>https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/
