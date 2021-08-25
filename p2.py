from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Deep Divers project-2").getOrCreate()

df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("Deep-Divers-P2/hotel_bookings.csv")
spark.sparkContext.setLogLevel("ERROR")

df.createOrReplaceTempView("hotel_booking")

# 1. How many successful bookings were done in 2015?
# q1 = spark.sql("SELECT COUNT(hotel) total_number_of_successful_booking_in_2015 from hotel_booking WHERE is_canceled=0 AND arrival_date_year=2015")
# q1.show()

# 2. How many companies booked hotel rooms country-wise?
# q2 = spark.sql("select country, count(company) total_company from hotel_booking where company!='NULL' group by country order by total_company desc")
# q2.show()

# 3. Which room was most preferred by adults?
# q3 = spark.sql("select reserved_room_type, count(reserved_room_type) total_count from hotel_booking where adults>0 group by reserved_room_type order by total_count desc limit 1")
# q3.show()

# 6. number of customers who stayed weekend nights and weekday nights(atleast one time)
# q6 = spark.sql("select count(hotel) from hotel_booking where stays_in_weekend_nights>=2 and stays_in_week_nights>=5")
# q6.show()

# 10. list out all market segment and how many bookings lies in each market segment.
# q10 = spark.sql("select market_segment, count(hotel) number_of_booking_lies_in_segment from hotel_booking group by market_segment")
# q10.show()

# 11. How many children+baby stayed in hotel in USA?
# q11 = spark.sql(
#     "select country, sum(children+babies) \
#     from hotel_booking \
#     where country='USA' \
#     group by country"
# )
# q11.show()

# 12. Which country has highest average adr(average daily rate)?
# q12 = spark.sql(
#     "select country, avg(adr) average_adr \
#     from hotel_booking \
#     group by country \
#     order by average_adr desc \
#     limit 1"
# )
# q12.show()

# 13. top 3 agents who have booked the most hotel rooms.
# q13 = spark.sql(
#     "select agent, count(hotel) total_booking_by_agent \
#     from hotel_booking \
#     where agent!='NULL' \
#     group by agent \
#     order by total_booking_by_agent desc \
#     limit 3"
# )
# q13.show()

# 14. Which meal type most choose by people country-wise?
# q14 = spark.sql(
#     "select country_name, meal, max_total \
#     from (select country as country_name, max(c_total_meal) as max_total \
#         from (select country, count(meal) c_total_meal \
#             from hotel_booking \
#             group by country, meal) \
#         group by country) \
#     join (select country, meal, count(meal) as t_total_meal \
#         from hotel_booking \
#         group by country, meal) \
#     on max_total=t_total_meal and country_name=country"
# )
# q14.show()

# 15. In which month and year, the highest car parking space was required?
# q15 = spark.sql(
#     "select arrival_date_month, arrival_date_year, sum(required_car_parking_spaces) total_number_of_car_parking_spaces_required_in_this_particular_month_and_year \
#     from hotel_booking \
#     group by arrival_date_year, arrival_date_month \
#     order by total_number_of_car_parking_spaces_required_in_this_particular_month_and_year desc \
#     limit 1"
# )
# q15.show()

# 16. find percentage of each type of customer_type?
# q16 = spark.sql(
#     "select customer_type, round(count(*)*100.0 / sum(count(*)) over(), 2) percentage \
#     from hote_booking \
#     group by customer_type"
# )
# q16.show()

# 17. Average waiting days month-wise in the year 2016
# q17 = spark.sql(
#     "select arrival_date_month, avg(days_in_waiting_list) average_waiting_days \
#     from hotel_booking \
#     where arrival_date_year=2016 \
#     group by arrival_date_month"
# )
# q17.show()

# 18. How many times hotel did not assign room type same as a reserved type to customers year-wise
# q18 = spark.sql(
#     "select arrival_date_year, count(hotel) number_of_times \
#     from hotel_booking \
#     where reserved_room_type!=assigned_room_type \
#     group by arrival_date_year"
# )
# q18.show()

# 19. How many adults booked room in 2017.
# q19 = spark.sql("select sum(adults) as No_of_Adults from hotel_booking where arrival_date_year=2017")
# q19.show()

# 22.  Summary of reservation status
# q22 = spark.sql("select reservation_status from hotel_booking") 
# q22.show()

# 23. Select company whose lead time is between 100 and 1000.
# q23 = spark.sql("select count(company) from hotel_booking where lead lead_time between 100 and 1000")
# q23.show()