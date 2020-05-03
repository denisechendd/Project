# Sentiment Analysis Project

## Bi-LSTM Sentiment Analysis model (Binary Classification)
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
![alt text][photo/BiLSTM_model.png]
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
1. take doc2vec pretrained words embedding to feed as weights into the model (not update the learned word weights in this model)
2. take doc2vec pretrained words embedding to feed as weights into the model (pdate the learned word weights in this model) <br>Set parameter``trainable=True``
**First two methods: Embedding layer (35000, 300) needs to match with the input data shape (35000, 800) and the vocab size in tokenizer as 350, and output of doc2vec shape to be 350**
3. Use 1000 Vocab size for Tokenizer into the model
4. Use 5000 Vocab size of Tkenizer into the model

### Notes to improve model performance:
- Put Doc2Vec pretrained embedding into deep learning Model
- Set pretrained words embedding to be trained into the embedding layer
- Add more epochs for model training
- Add more layers since training document is large (35000 messages for training and 15000 for test)
- Set dropout rate for robust model on training and validation dataset

### References:
- How to Use Word Embedding Layers for Deep Learning with Keras, <br>https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/
