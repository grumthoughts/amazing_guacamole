<<<<<<< HEAD
--Задание #1
SELECT 
    c.login, 
    COUNT(o.track) AS ordersInDelivery
FROM 
    "Couriers" AS c
INNER JOIN 
    "Orders" AS o ON c.id = o."courierId"
WHERE 
    o."inDelivery" = true
GROUP BY 
    c.login;


--Задание #2
SELECT 
    track,
    CASE 
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM 
=======
--Задание #1
SELECT 
    c.login, 
    COUNT(o.track) AS ordersInDelivery
FROM 
    "Couriers" AS c
INNER JOIN 
    "Orders" AS o ON c.id = o."courierId"
WHERE 
    o."inDelivery" = true
GROUP BY 
    c.login;


--Задание #2
SELECT 
    track,
    CASE 
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM 
>>>>>>> ded9de0ea44b32734579eec9a78f464e919853ed
    "Orders";