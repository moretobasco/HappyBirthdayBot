TRUNCATE subscriptions;
DELETE FROM subscriptions;

INSERT INTO subscriptions (subscription_id, user_id, user_sub_id, notify_before_days, notify_on_day) VALUES
(1, 1, 275, '[1]', TRUE),
(2, 1, 276, '[1, 2]', TRUE),
(3, 1, 277, '[1, 2, 3]', TRUE)
