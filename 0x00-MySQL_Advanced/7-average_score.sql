-- script that creates a stored procedure ComputeAverageScoreForUser

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10,2);
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
    UPDATE users SET avg_score = avg_score WHERE id = user_id;
END$$
DELIMITER ;

