

-- change table constraint
-- SHOW CREATE TABLE Daily;

-- ALTER TABLE Daily DROP FOREIGN KEY daily_ibfk_1;

-- ALTER TABLE Daily 
-- ADD CONSTRAINT daily_ibfk_1 
-- FOREIGN KEY (ts_code) 
-- REFERENCES StockList (ts_code);

select count(*) from StockList WHERE list_status = 'P'

select * from Daily Limit 3

DELETE FROM Daily

SELECT count(distinct(ts_code)) FROM Daily WHERE trade_date = 20210129 

SELECT * FROM Daily 
WHERE trade_date = 20210129
 AND ts_code = '000001.SZ'