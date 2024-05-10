-- create a view that lists all students who have a score under 80 (strict) and no last meeting in more than 1 month
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS SELECT name FROM students WHERE (score < 80) AND (last_meeting IS NULL OR DATEDIFF(CURDATE(), last_meeting) > 30);
