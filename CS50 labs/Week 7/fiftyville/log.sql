-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check reports
SELECT * FROM crime_scene_reports;

-- Check reports made in Humphrey Street
SELECT id, day, month, year, description FROM crime_scene_reports 
WHERE street = 'Humphrey Street';


-- 295|28|7|2021|
-- Theft of the CS50 duck took place at 10:15am 
-- at the Humphrey Street bakery. 
-- Interviews were conducted today with three 
-- witnesses who were present at the time – each of their 
-- interview transcripts mentions the bakery.

-- Look at the transcriptions
SELECT id, name, transcript FROM interviews 
WHERE year = '2021' AND day = '28' AND month = '7' 
AND transcript LIKE '%bakery%';

-- 161|Ruth|
-- Sometime within ten minutes of the theft, I saw the thief get into
--  a car in the bakery parking lot and drive away. If you have 
--  security footage from the bakery parking lot, you might want to 
--  look for cars that left the parking lot in that time frame.
-- 162|Eugene|
-- I don't know the thief's name, but it was someone I recognized. 
--  Earlier this morning, before I arrived at Emma's bakery, 
--  I was walking by the ATM on Leggett Street and saw the thief there 
--  withdrawing some money.
-- 163|Raymond|
-- As the thief was leaving the bakery,
--  they called someone who talked to them for less than a minute.
--  In the call, I heard the thief say that they were planning
--  to take the earliest flight out of Fiftyville tomorrow.
--  The thief then asked the person on the other end of the
--  phone to purchase the flight ticket.

-- 1. Look at the time frame of the cars and xref plates
-- 2. Check ATM withdrawals on Leggett street that morning
-- 3. Check earlierst flight next day...
-- 4. ... and the bank accounts on that day (28|7|2021) after the theft 
-- 5. Check phone calls

-- 1: 
SELECT hour, minute, activity, license_plate FROM bakery_security_logs 
WHERE day = '28' AND month = '7' AND year = '2021' AND hour = '10' 
AND minute >= 20 AND minute < 30;
--      10|20|exit|G412CB7
--      10|21|exit|L93JTIZ
--      10|23|exit|322W7JE
--      10|23|exit|0NTHK55
-- 2: 
SELECT account_number, transaction_type, amount, atm_location FROM atm_transactions 
WHERE year = '2021' AND month = '7' AND day = 28 
AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'; 
--      28500762|withdraw|48|Leggett Street
--      28296815|withdraw|20|Leggett Street
--      76054385|withdraw|60|Leggett Street
--      49610011|withdraw|50|Leggett Street
--      16153065|withdraw|80|Leggett Street
--      25506511|withdraw|20|Leggett Street
--      81061156|withdraw|30|Leggett Street
--      26013199|withdraw|35|Leggett Street
-- 3: 
SELECT flights.id, day, hour, minute, destination_airport_id, (
    SELECT city FROM airports WHERE destination_airport_id = airports.id
    )
FROM flights JOIN airports ON origin_airport_id = airports.id
WHERE origin_airport_id = (
    SELECT id FROM airports WHERE city = 'Fiftyville'
    )
AND day = '29' AND month = '7' AND year = '2021'
ORDER BY hour
LIMIT 1;
--      36|29|8|20|4|New York City      


-- 4 ... and the bank accounts on that day (28|7|2021) after the theft 
SELECT account_number, (
    SELECT name FROM people WHERE person_id = people.id
    )
, creation_year 
FROM bank_accounts JOIN people ON person_id = people.id 
WHERE account_number IN (
        SELECT account_number FROM atm_transactions 
        WHERE year = '2021' AND month = '7' AND day = 28 
        AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'
        );

--      49610011|Bruce|2010
--      26013199|Diana|2012
--      16153065|Brooke|2012
--      28296815|Kenny|2014
--      25506511|Iman|2014
--      28500762|Luca|2014
--      76054385|Taylor|2015
--      81061156|Benista|2018


-- xref plates from bakery security logs with names from above, and names from bank accounts:
SELECT * FROM people
WHERE license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
    ) 
AND name IN (
    SELECT (
        SELECT name FROM people WHERE person_id = people.id
        )
    FROM bank_accounts JOIN people ON person_id = people.id 
    WHERE account_number IN (
        SELECT account_number FROM atm_transactions 
        WHERE year = '2021' AND month = '7' AND day = 28 
        AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'
        )
        );

-- 396669|Iman|(829) 555-5269|7049073643|L93JTIZ
-- 467400|Luca|(389) 555-5198|8496433585|4328GD8
-- 514354|Diana|(770) 555-1861|3592750733|322W7JE
-- 686048|Bruce|(367) 555-5533|5773159633|94KL13X

-- 5. Check phone calls
SELECT (
    SELECT name FROM people WHERE phone_number = caller
    ), 
    (SELECT name FROM people WHERE phone_number = receiver
    ), duration, day, month, year 
FROM phone_calls JOIN people ON people.phone_number = phone_calls.caller 
WHERE year = '2021' AND month = '7' AND day = '28' AND duration < 60 
AND name IN (SELECT name FROM people
WHERE license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
    ) 
AND name IN (
    SELECT (
        SELECT name FROM people WHERE person_id = people.id
        )
    FROM bank_accounts JOIN people ON person_id = people.id 
    WHERE account_number IN (
        SELECT account_number FROM atm_transactions 
        WHERE year = '2021' AND month = '7' AND day = 28 
        AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'
        )
        ));
--          Bruce|Robin|45|28|7|2021

-- Our thief is Bruce, the accomplice is Robin

SELECT (SELECT name FROM people WHERE people.passport_number = passengers.passport_number) FROM passengers JOIN flights ON passengers.flight_id = flights.id  WHERE flights.id = 36;

-- Confirmed Bruce is in the flight
