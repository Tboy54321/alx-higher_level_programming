-- selcets a group of data and orders it by state
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
