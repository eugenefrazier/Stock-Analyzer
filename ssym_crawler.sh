
for i in 0 A B C D E F G H I J L K M N O P Q R S T U V W X Y Z
do

   echo $i | scrapy crawl ssym -o $PWD'/dataset/company_datalist_raw/company_datalist_raw_'$i'.csv' 
done

for i in 0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
do
 
   echo $i | python3  $PWD"/prefilter_script_compdatalist_prefilter.py"
done
