import datetime, warnings, scipy 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import ConnectionPatch
from collections import OrderedDict
from matplotlib.gridspec import GridSpec
#from mpl_toolkits.basemap import Basemap
from sklearn import metrics, linear_model
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from scipy.optimize import curve_fit
plt.rcParams["patch.force_edgecolor"] = True
plt.style.use('fivethirtyeight')
mpl.rc('patch', edgecolor = 'dimgray', linewidth=1)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "last_expr"
pd.options.display.max_columns = 50
%matplotlib inline
warnings.filterwarnings("ignore")

#import the data and make a data fram out of it ]
df=pd.read_csv(r'C:\Users\666677\Documents\Data-Sets\flights.csv',low_memory=False)

##Data cleaning from the Date 

df["DATE"]=pd.to_datetime(df[['YEAR','MONTH','DAY']])

#cONVERTING THE DECIMAL FORMAT OF TIME TO NORMAL 

 #SCHEDULED_DEPARTURE variable, the hour of the take-off is coded as a float 
#where the two first digits indicate the hour and the two last, the minutes.
# This format is not convenient and I thus convert it. 
#Finally, I merge the take-off hour with the flight date. To proceed with these transformations, 
#I define a few functions:





























