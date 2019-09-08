echo "[Comment]Running Technical Analysis"

echo "[Status]Analyzing Technical Analysis using Cycle Indicator"
python3 "$PWD/analysis_ta_cycle_indicator_loop.py"

echo "[Status]Analyzing Technical Analysis using Math Operator"
python3 "$PWD/analysis_ta_math_operator_loop.py"

echo "[Status]Analyzing Technical Analysis using Math Transform"
python3 "$PWD/analysis_ta_math_transform_loop.py"

echo "[Status]Analyzing Technical Analysis using Momentum Indicator"
python3 "$PWD/analysis_ta_momentum_indicator_loop.py"

echo "[Status]Analyzing Technical Analysis using Overlap Studies"
python3 "$PWD/analysis_ta_overlap_studies_loop.py"

echo "[Status]Analyzing Technical Analysis using Pattern Recognition"
python3 "$PWD/analysis_ta_pattern_recognition_loop.py"

echo "[Status]Analyzing Technical Analysis using Price Transform"
python3 "$PWD/analysis_ta_price_transform_loop.py"

echo "[Status]Analyzing Technical Analysis using Statistical Functions"
python3 "$PWD/analysis_ta_statistic_functions_loop.py"

echo "[Status]Analyzing Technical Analysis using Volatitility Indicator"
python3 "$PWD/analysis_ta_volatility_indicator_loop.py"

echo "[Status]Analyzing Technical Analysis using Volume Indicator"
python3 "$PWD/analysis_ta_volume_indicator_loop.py"

echo "[Comment]All Technical Analysis has been ended successfully"
