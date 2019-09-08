DATE=$(date +"%y-%m-%d")

mkdir $PWD"/dataset/company_fund_marketprice_prefilter/company_fund_marketprice_prefilter_"$DATE
mkdir $PWD"/dataset/company_fund_marketprice_raw/company_fund_marketprice_raw_"$DATE

for i in 0 A B C D E F G H I J L K M N O P Q R S T U V W X Y Z
do
   echo $i | scrapy crawl Fundbot -o $PWD"/dataset/company_fund_marketprice_raw/company_fund_marketprice_raw_$DATE/company_fund_marketprice_raw_"$DATE"_"$i".csv"    
done

do
   echo $i | python3 "$PWD/prefilter_script_fund_prefilter.py"
done
