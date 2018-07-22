import pandas as pd
import numpy as np

'''
 * @author maiziying
 * @email mrzi168@gmail.com
 * @create date 2018-07-22 11:19:53
'''


#change line width
desired_width = 320    
pd.set_option('display.width', desired_width)

def main():
    # california_housing_dataframe = pd.read_csv(
    #     "california_housing_train.csv", sep=",")
    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([852469, 1015785, 485199])
    cities = pd.DataFrame({'City name': city_names, 'Population': population})
    cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
    cities['Population density'] = cities['Population'] / cities['Area square miles']
    cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(
        lambda name: name.startswith('San'))
    print(cities)
    print('\n')
    print(cities.reindex([2, 0, 1]))     #change index
    print('\n')
    print(cities.reindex(np.random.permutation(cities.index))) #change index by random
    print('\n')
    print(cities.reindex([0, 4, 5, 2])) #with unknow index,NaN will be use
main()