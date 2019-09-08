echo "[Comment]Portfolio Generator V1 , developed by Eugene Frazier"

echo "[Status]Querying Stocks"
python3 "$PWD/portfolio_generator_query.py"

echo "[Status]Copying Selected Stocks"
python3 "$PWD/ultility_copy_stock_marketprice.py"

echo "[Status]Generating Efficient Frontier Graph"
python3 "$PWD/portfolio_generator_efficient_portfolio_MYY.py"

echo "[Status]Plotting Correlation Graph"
python3 "$PWD/portfolio_generator_correl.py"

echo "[Status]Creating stock weightage allocation piechart"
python3 "$PWD/portfolio_generator_piechart.py"

echo "[Status]Creating total stocks close price"
python3 "$PWD/portfolio_generator_selected_stock_close_price.py"

echo "[Status]Backtesting Performance"
python3 "$PWD/portfolio_generator_company_vs_klci_dual_graph_plot.py"

echo "[Comment]Portfolio Generator has been ended .Task completed Successfully"
