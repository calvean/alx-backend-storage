-- create stored procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight INT;
    DECLARE weighted_score DECIMAL(10, 2);
    DECLARE avg_score DECIMAL(10, 2);
    
    -- get total score and total weight
    SELECT SUM(score * weight) INTO total_score, SUM(weight) INTO total_weight
    FROM corrections
    WHERE user_id = user_id;
    
    -- compute weighted score and average score
    IF total_weight > 0 THEN
        SET weighted_score = total_score / total_weight;
        SET avg_score = ROUND(weighted_score, 2);
    ELSE
        SET avg_score = 0;
    END IF;
    
    -- insert or update user's average score in the table users
    INSERT INTO user_scores (user_id, avg_weighted_score)
    VALUES (user_id, avg_score)
    ON DUPLICATE KEY UPDATE avg_weighted_score = avg_score;
    
END $$
DELIMITER ;

