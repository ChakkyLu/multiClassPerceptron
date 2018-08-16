# multiClassPerceptron

## main.py
  there are three parts in main.py, first load iris data from UCI and then compare the accuracy from my model and scikit linear model
  the second is to train the model from house data
  the third is to train the model from position data
  
## house data
  the scrape_data/scrape_house helps you to grabber house information from website, after running this method you will get a house.csv file in data/, and if you want to use the data, you have to use the function "generate_data" in process_data/house.py, it will help you to preprocess the original data and leverize them and you can also adjust the parameters
  
## position_data
   in scape_data/socket_position.py, it will give you a socket thread and if you open the android application, you can collect the wifi message and after stopping collecting, you will get a position.txt under this directory. You need to run the test.py to generate a trainset.dat to help you train the perceptron model.
   
