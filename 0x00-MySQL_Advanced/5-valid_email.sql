--set trigger to reset valid-email attribute when email is changed
DROP TRIGGER IF EXISTS `reset_email`;
DELIMITER $$
CREATE TRIGGER `reset_email` BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END;
$$
DELIMITER ;
