import pandas as pd
from math import radians, sin, cos, acos
from pathlib import Path


class Analysis:

    def __init__(self, rdf, pdf):
        print('Reading dataset...')
        try:
            self.frame = pd.read_csv('data/'+rdf)
            print('Dataset loaded, Sample:')
            print(self.frame.head())
            print('Loading POI dataset...')
            self.poi = pd.read_csv('data/'+pdf)
            self.sep = '################'
            print(self.sep)
        except Exception as ex:
            print(str(ex))
            print("Loading default datasets")
            self.frame = pd.read_csv('data/DataSample.csv')
            print('Dataset loaded, Sample:')
            print(self.frame.head())
            print('Loading POI dataset...')
            self.poi = pd.read_csv('data/POIList.csv')
            self.sep = '################'
            print(self.sep)

    def cleaning(self):
        print('1- Cleanup Stage: ')
        print("Found {0} of suspicious records...".format(len(self.frame[self.frame.duplicated(['TimeSt','Latitude', 'Longitude'],keep=False)])))
        print("Deleting suspicious records...")
        self.frame = self.frame.drop_duplicates(['TimeSt','Latitude','Longitude'],keep=False)
        print("Size of clean dataset: {0} Records".format(len(self.frame)))
        print(self.sep)

    def calc(self, point):
        lat = point['Latitude']
        lng = point['Longitude']
        distances = {}
        dist = 0
        for i in range(len(self.poi)):
            slat = radians(float(lat))
            slon = radians(float(lng))
            elat = radians(float(self.poi['Latitude'][i]))
            elon = radians(float(self.poi['Longitude'][i]))
            dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
            distances[self.poi['POIID'][i]] = dist
        return min(distances, key=distances.get), dist

    def labeling(self):
        print('2- Labeling Stage: ')
        print('POIs: ')
        print(self.poi.head())
        print('Combining POIs in the same location...')
        self.poi = self.poi.groupby(['Latitude','Longitude'], sort=False)['POIID'].apply(','.join).reset_index()
        print('POIs after combining: ')
        print(self.poi.head())
        print('Labeling requests...')
        self.frame['POI'], self.frame['Distance'] = zip(*self.frame.apply(self.calc, axis=1))
        print('Labels sample: ')
        print(self.frame.head())
        print(self.sep)

    def analyzing(self):
        print('3- Analysis Stage: ')
        print('Calculating average distance for POIs...')
        self.poi['avg_distance'] = self.poi['POIID'].apply(lambda x:self.frame[self.frame['POI']==x]['Distance'].mean())
        print('Calculating standard deviation distance for POIs...')
        self.poi['std_distance'] = self.poi['POIID'].apply(lambda x:self.frame[self.frame['POI']==x]['Distance'].std())
        print('Analysis sample 1: ')
        print(self.poi.head())
        print('Calculating circle radius for POIs...')
        self.poi['Circle_radius_km'] = self.poi['POIID'].apply(lambda x: self.frame[self.frame['POI']==x]['Distance'].max())
        print('Calculating denisty for POIs...')
        self.poi['Density'] = self.poi['POIID'].apply(lambda x: self.frame[self.frame['POI']==x]['Distance'].count())/(3.14*(self.poi['Circle_radius_km'])**2)
        print('Analysis sample 2: ')
        print(self.poi.head())

    def exporting_dfs(self):
        print('Saving results...')
        Path("results").mkdir(parents=True, exist_ok=True)
        self.frame.to_csv('results/analysis_results.csv', index=False)
        self.poi.to_csv('results/POIList.csv', index=False)


if __name__ == '__main__':
    try:
        requests = input("Please enter requests dataframe's name: ")
        poi = input("Please enter POIs dataframe's name: ")
        ext = ".csv"
        if ext not in requests:
            requests = requests + ext
        if ext not in poi:
            poi = poi + ext
        analysis = Analysis(requests, poi)
        analysis.cleaning()
        analysis.labeling()
        analysis.analyzing()
        analysis.exporting_dfs()
    except Exception as ex:
        print(str(ex))
