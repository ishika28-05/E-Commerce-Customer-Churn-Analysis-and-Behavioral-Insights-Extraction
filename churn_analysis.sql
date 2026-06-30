use churn_analysis;
select*from cleaned_dataset limit 10;
-- count of total customers
select count(*) as total_customers 
from cleaned_dataset;
-- count of churned customers
select count(*) as churned_customers 
from cleaned_dataset 
where ChurnFlag = "Churned";
-- count of churned and retained customers
select ChurnFlag, count(*) as customer_count
from cleaned_dataset
group by ChurnFlag;
-- percentage of churned and retained customers
select ChurnFlag,count(*) as customer_count,
 round(count(*) * 100/(select count(*) from cleaned_dataset),2) as percentage
from cleaned_dataset
group by ChurnFlag;
-- churn by city tier
select CityTier, ChurnFlag,
count(*) as churned_city_tier
from cleaned_dataset
group by CityTier, ChurnFlag
order by CityTier;
-- avg satisfaction score by churn status
select ChurnFlag, round(avg(SatisfactionScore),2) as avg_ss
from cleaned_dataset
group by ChurnFlag;
-- churn by preferred login device
select PreferredLoginDevice, ChurnFlag, count(*) as count
from cleaned_dataset
group by PreferredLoginDevice, ChurnFlag;
-- churn by payment mode
select PreferredPaymentMode, ChurnFlag, count(*) as count
from cleaned_dataset
group by PreferredPaymentMode, ChurnFlag;
-- complaint impact on churn
select Complain, ChurnFlag, count(*) as count
from cleaned_dataset
group by Complain, ChurnFlag;
-- avg tenure by churn status
select ChurnFlag, round(avg(Tenure),2) as avg_tenure
from cleaned_dataset
group by ChurnFlag;
-- churn by order category
select PreferedOrderCat, ChurnFlag, count(*) as count
from cleaned_dataset
group by PreferedOrderCat,ChurnFlag;
-- high valued churned customer (cashback above avg and still churned)
select CustomerID,Tenure,CityTier,Gender,OrderCount,CashbackAmount
from cleaned_dataset 
where CashbackAmount > (select round(avg(CashbackAmount),2) from cleaned_dataset) and ChurnFlag = "Churned"
order by CashbackAmount desc;
-- customers with complain who didnt churn (loyal despite complaining)
select CustomerID,Tenure,CityTier,Gender,OrderCount,Complain
from cleaned_dataset
where Complain>0 and ChurnFlag = "Retained"; 
-- rank customers by cashback within each city tier
select CustomerID,CityTier,CashbackAmount,
dense_rank() over (partition by CityTier order by CashbackAmount desc) as rank_in_tier
from cleaned_dataset;
-- churn percentage within each complaint group
select Complain,ChurnFlag,count(*) as count,
round(count(*)*100 / (select count(*) from cleaned_dataset),2) as percentage
from cleaned_dataset
group by Complain,ChurnFlag;
-- 2nd method
select Complain,ChurnFlag,count(*) as count,
round(count(*)*100 / sum(count(*)) over (partition by Complain),2) as percentage
from cleaned_dataset
group by Complain,ChurnFlag;
-- running total of customers by tenure
select Tenure, count(*) as customers_at_tenure,
sum(count(*)) over (order by Tenure) as running_total
from cleaned_dataset
group by Tenure;
-- average satisfaction per city tier (compared to overall avg)
select CityTier, round(avg(SatisfactionScore),2) as avg_satisfaction,
round(avg(avg(SatisfactionScore)) over (order by round(avg(SatisfactionScore),2) desc ),2) as overall_avg
from cleaned_dataset
group by CityTier;
-- stored procedure to get churn summary by any city tier
delimiter //
create procedure get_churn_by_city_tier (in tier int)
begin
select ChurnFlag, count(*) as customer_count,
round(avg(SatisfactionScore)) as avg_ss,
round(avg(Tenure)) as avg_tenure,
round(avg(CashbackAmount)) as avg_cashback
from cleaned_dataset
where CityTier = tier
group by ChurnFlag;
end //
delimiter ;
call get_churn_by_city_tier(1);
call get_churn_by_city_tier(2);
call get_churn_by_city_tier(3);
-- create a view of only churned customers
create view churned_customers as 
select * from cleaned_dataset 
where Churn = 1;
select*from churned_customers;
-- churn rate by city tier using CTE
with churn_counts as(
select CityTier,Churn, count(*) as count
from cleaned_dataset
group by CityTier,Churn)
select CityTier,
sum(case when Churn = 1 then count else 0 end) as churned,
sum(case when Churn = 0 then count else 0 end) as retained
from churn_counts
group by CityTier;