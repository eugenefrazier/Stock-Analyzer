#Import scikit-learn dataset library
from sklearn import datasets
import pandas as pd
import pydotplus
from sklearn.externals.six import StringIO  
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

stock=pd.read_csv(current_dir+'/example_folder/C_D_E_F_G_Company_Fundamental_Dataset_MYY_2018.csv')
# Creating a DataFrame of given iris dataset.
print(stock.tail())

print("* Analyst Consensus:", stock["Analyst Consensus"].unique(), sep="\n")

def encode_target(stock, target_column):
    stock_mod = stock.copy()
    predict = stock_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(predict)}
    stock_mod["Prediction"] = stock_mod[target_column].replace(map_to_int)

    return (stock_mod, predict)

stock2, predict = encode_target(stock, "Analyst Consensus")

print("* stock2.head()", stock2[["Prediction", "Analyst Consensus"]].head(),sep="\n", end="\n\n")
print("* stock2.tail()", stock2[["Prediction", "Analyst Consensus"]].tail(),sep="\n", end="\n\n")
print("* Prediction", predict, sep="\n", end="\n\n")

features = list(stock2.columns[1:11])

print("* features:", features, sep="\n")

y = stock2["Prediction"]
X = stock2[features]
dt = DecisionTreeClassifier(min_samples_split=30, random_state=99)
dt.fit(X, y)

dot_data = StringIO()

# Export as dot file
export_graphviz(dt, out_file=dot_data, 
                feature_names = features,
                class_names = predict,
                rounded = True, proportion = False, 
                precision = 2, filled = True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  

graph.write_png(current_dir+"/example_folder/Analysis_Consensous_Prediction.png")