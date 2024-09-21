CREATE DATABASE game_haven;
USE game_haven;


CREATE TABLE `game_room_bookings` (
  `games` varchar(45) DEFAULT NULL,
  `16-17` int(11) DEFAULT NULL,
  `16-17-booking-id` varchar(20) DEFAULT NULL,
  `17-18` int(11) DEFAULT NULL,
  `17-18-booking-id` varchar(20) DEFAULT NULL,
  `18-19` int(11) DEFAULT NULL,
  `18-19-booking-id` varchar(20) DEFAULT NULL,
  `19-20` int(11) DEFAULT NULL,
  `19-20-booking-id` varchar(20) DEFAULT NULL,
  `20-21` int(11) DEFAULT NULL,
  `20-21-booking-id` varchar(20) DEFAULT NULL,
  `21-22` int(11) DEFAULT NULL,
  `21-22-booking-id` varchar(20) DEFAULT NULL,
  `bookingDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

select * from game_room_bookings;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `filldates`(dateStart DATE, dateEnd DATE, gamename VARCHAR(20))
BEGIN
  WHILE dateStart <= dateEnd DO
    INSERT INTO game_room_bookingss (games, bookingDate) VALUES (gamename, dateStart);
    SET dateStart = date_add(dateStart, INTERVAL 1 DAY);
  END WHILE;
END$$
DELIMITER ;

CALL `game_haven`.`filldates` (20240708,20240712,'Chess');
CALL `game_haven`.`filldates` (20240708,20240712,'Badminton');
CALL `game_haven`.`filldates` (20240708,20240712,'Table Tennis');
CALL `game_haven`.`filldates` (20240708,20240712,'Squash');


/*QUERIES TO CHECK THE OUTPUT/RESULT BEFORE USING IN PYTHON*/
SELECT games, slot1, slot2, slot3, slot4, slot5, slot6
FROM game_room_bookings
WHERE bookingdate = '2024-07-08';

Select * from game_room_bookings;

UPDATE game_room_bookings
SET slot1 = 1, slot1_booking_id = 'Ram'
WHERE bookingDate = '2024-07-08' AND games = 'Chess'; 




