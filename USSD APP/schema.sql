CREATE TABLE students (
    index_number VARCHAR(20) PRIMARY KEY,
    full_name VARCHAR(100),
    program VARCHAR(100),
    gpa DECIMAL(3,2),
    fees_paid DECIMAL(10,2),
    fees_outstanding DECIMAL(10,2)
);