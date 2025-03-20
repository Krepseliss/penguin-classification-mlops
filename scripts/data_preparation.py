import pandas as pd
import seaborn as sns
from sqlalchemy import create_engine
from pathlib import Path

#load the dataset
penguins=sns.load_dataset('penguins').dropna()

#creating the ISLANDS table
islands_df=pd.DataFrame(penguins['island'].unique(), columns=['name']).reset_index()
islands_df.rename(columns={'index':'island_id'},inplace=True)

#merging island_id into penguins df
penguins=penguins.merge(islands_df, left_on='island', right_on='name', how='left')

#add unique animal_id for each penguin (primary key)
penguins['animal_id']=penguins.index

#define database's path
db_path=Path(r"C:\Users\alex\Data Engineering\penguin-classification-mlops\data\penguins_db.sqlite").resolve()

#create SQLite engine
engine=create_engine(r"sqlite:///C:\Users\alex\Data Engineering\penguin-classification-mlops\data\penguins_db.sqlite")

#save ISLANDS table
islands_df.to_sql('ISLANDS', con=engine, if_exists='replace', index=False)

#save PENGUINS table + foreign key
penguins[['species', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
          'body_mass_g', 'sex', 'island_id', 'animal_id']].to_sql('PENGUINS', con=engine, if_exists='replace', index=False)

print('Success!')