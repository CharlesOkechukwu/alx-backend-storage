-- create function SafeDiv that divides the first number by the second number and returns the result
DROP FUNCTION IF EXISTS `SafeDiv`;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE result FLOAT DEFAULT 0;
	IF b != 0 THEN
		SET result = a / b;
	END IF;
	RETURN result;
END;
$$
DELIMITER ;
