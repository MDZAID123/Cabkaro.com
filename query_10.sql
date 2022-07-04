-- query1
SELECT user_id,booking_id
FROM booking
where destination='govindpuri';



-- query2
select b.user_id,b.booking_id from booking b,cars c,rides r where(b.booking_id=r.booking_id and r.registration_no=c.registration_no and c.car_type="prime sedan") order by b.user_id asc;



-- query3
select r.registration_no 
from rides r
where r.date<'2021/1/22' and exists( select * from cars c where c.registration_no=r.registration_no and c.seating<7);



-- query4
select e_id,first_name
from employees

where salary between 11000 and 13000

order by first_name;





-- query5
select count(car_type) as "car_type_count",car_type from cars where registration_no like"DL%" and milage between 20 and 40 group by car_type; 





-- query6
update fares
set cost_km=case
	when cost_km<=100 then cost_km*1.2
    else cost_km*1.05
	end;
    
    
-- query 7
update distance d
set d.total_price=(select d.distance*f.cost_km from rides r, cars c, fares f where d.booking_id=r.booking_id and r.registration_no=c.registration_no and c.car_type = f.car_type )
where booking_id<40;

-- query 8
select car_model,car_type from cars c where exists(select * from luxury_cars l where l.movies_tv=1 and l.wifi=1 and c.car_type=l.car_type);







-- query 9
SELECT Temp.name, Temp.AvgSalary
FROM ( SELECT c.registration_no, c.car_model AS name, AVG(e.salary) AS
AvgSalary FROM cars c, rides r, Employees e
WHERE c.registration_no = r.registration_no AND r.e_id = e.e_id AND c.milage >
40 GROUP BY c.registration_no, c.car_model ) AS Temp;



--  query 10
select d.booking_id,f.car_type, f.cost_km, d.distance, d.total_price
from distance d, rides r, cars c, fares f
where d.booking_id=r.booking_id and r.registration_no=c.registration_no and c.car_type=f.car_type
order by booking_id;







