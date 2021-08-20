from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Deep Divers project-2").getOrCreate()

df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("Deep-Divers-P2/hotel_bookings.csv")
spark.sparkContext.setLogLevel("ERROR")

df.createOrReplaceTempView("hotel_booking")

# q1 = spark.sql("SELECT COUNT(hotel) total_number_of_successful_booking_in_2015 from hotel_booking WHERE is_canceled=0 AND arrival_date_year=2015")
# q1.show()

# q2 = spark.sql("select country, count(company) total_company from hotel_booking where company!='NULL' group by country order by total_company desc")
# q2.show()

# q3 = spark.sql("select reserved_room_type, count(reserved_room_type) total_count from hotel_booking where adults>0 group by reserved_room_type order by total_count desc limit 1")
# q3.show()

# q6 = spark.sql("select count(hotel) from hotel_booking where stays_in_weekend_nights>=2 and stays_in_week_nights>=5")
# q6.show()

# q9 = spark.sql("select agent, count(hotel) total_booking_by_agent from hotel_booking where agent!='NULL' group by agent order by total_booking_by_agent desc limit 3")
# q9.show()

# q10 = spark.sql("select market_segment, count(hotel) number_of_booking_lies_in_segment from hotel_booking group by market_segment")
# q10.show()

# q12 = spark.sql("select arrival_date_year, count(hotel) number_of_times from hotel_booking where reserved_room_type!=assigned_room_type group by arrival_date_year")
# q12.show()

# q14 = spark.sql("select arrival_date_month, avg(days_in_waiting_list) average_waiting_days from hotel_booking where arrival_date_year=2015 group by arrival_date_month")
# q14.show()

# q15 = spark.sql("select arrival_date_month, arrival_date_year, sum(required_car_parking_spaces) total_number_of_car_parking_spaces_required_in_this_particular_month_and_year from hotel_booking group by arrival_date_year, arrival_date_month order by total_number_of_car_parking_spaces_required_in_this_particular_month_and_year desc limit 1")
# q15.show()