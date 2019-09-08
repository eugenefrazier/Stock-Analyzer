echo "[Comment]Performing Single Stock Analysis"

echo "[Status]Predicting Values"
python3 "$PWD/analysis_prophet.py"

echo "[Status]Describing Statistical Values"
python3 "$PWD/analysis_describe.py"

echo "[Status]Displaying Prediction Analysis"
python3 "$PWD/analysis_prediction_graph.py"

echo "[Status]Displaying Correlation Graph of the actual vs predicted"
python3 "$PWD/analysis_predict_correl_graph.py"
 
echo "[Status]Performing Abnormality Detection"
python3 "$PWD/analysis_abnormal_detection.py"

echo "[Status]Analysing Stock Daily Percentage Change"
python3 "$PWD/analysis_pct_company.py"



