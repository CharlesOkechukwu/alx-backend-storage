-- createing a trigger that decreases the quantity of an item after adding new order

DROP TRIGGER IF EXISTS `decrease_qty`;
DELIMITER $$
CREATE TRIGGER `decrease_qty` AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END;
$$
DELIMITER ;
