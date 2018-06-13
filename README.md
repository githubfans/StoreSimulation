# StoreSimulation

> python GenTransaction.py

`mysql> select MAX(id), MIN(id), TIMEDIFF(MAX(dateadd), MIN(dateadd)) as timef, unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd)) as secs, MAX(id)/(unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd))) as trx_in_1sec, MAX(id)/((unix_timestamp(MAX(dateadd)) - unix_timestamp(MIN(dateadd)))/60) as trx_in_1minute from Transaction;`
