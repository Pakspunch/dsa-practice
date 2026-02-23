-- create a table:
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount DECIMAL(10,2),
    status TEXT,
    city TEXT,
    created_at TEXT
);

INSERT INTO transactions VALUES (1, 101, 5000.00, 'completed', 'Mumbai', '2025-01-15');
INSERT INTO transactions VALUES (2, 102, 1200.00, 'failed', 'Delhi', '2025-01-15');
INSERT INTO transactions VALUES (3, 101, 3400.00, 'completed', 'Mumbai', '2025-01-16');
INSERT INTO transactions VALUES (4, 103, 8900.00, 'pending', 'Pune', '2025-01-17');
INSERT INTO transactions VALUES (5, 102, 4500.00, 'completed', 'Delhi', '2025-01-18');
INSERT INTO transactions VALUES (6, 104, 650.00, 'failed', 'Mumbai', '2025-01-18');
INSERT INTO transactions VALUES (7, 103, 12000.00, 'completed', 'Pune', '2025-01-19');
INSERT INTO transactions VALUES (8, 101, 2200.00, 'pending', NULL, '2025-01-20');
INSERT INTO transactions VALUES (9, 104, 7800.00, 'completed', 'Delhi', '2025-01-21');
INSERT INTO transactions VALUES (10, 102, 3100.00, 'completed', 'Mumbai', '2025-01-22');

-- perform functions
SELECT * FROM transactions;
SELECT id, amount, status FROM transactions;
SELECT DISTINCT status FROM transactions;
SELECT DISTINCT city FROM transactions;
SELECT * FROM transactions WHERE city IS NULL;
SELECT * FROM transactions WHERE city = NULL;
