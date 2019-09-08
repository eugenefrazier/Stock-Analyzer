echo "[Comment]Processing Multiple Stock Analysis "

echo "[Status]Generating Price Prediction Graph"
python3 "$PWD/analysis_prediction_graph_loop.py"

echo "[Status]Displaying Correlation Graph of the actual vs predicted"
python3 "$PWD/analysis_predict_correl.py"

echo "[Status]Analysing Stock Daily Percentage Change"
python3 "$PWD/analysis_pct_company_loop.py"

bash "$PWD/ta_analysis.sh"


