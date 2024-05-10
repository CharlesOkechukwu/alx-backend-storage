-- create a stored procedure ComputeAverageScoreForUser which computes and store the average score of a student
DROP PROCEDURE IF EXISTS `ComputeAverageScoreForUser`;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE total INT DEFAULT 0;
	DECLARE project_count INT DEFAULT 0;
	SELECT SUM(score) INTO total FROM corrections WHERE corrections.user_id = user_id;
	SELECT COUNT(*) INTO project_count FROM corrections WHERE corrections.user_id = user_id;
	UPDATE users SET average_score = total / project_count WHERE users.id = user_id;
END;
$$
DELIMITER ;
