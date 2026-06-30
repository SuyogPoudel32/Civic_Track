


-- =========================
-- USERS TABLE
-- =========================

CREATE TABLE users (

    user_id INT AUTO_INCREMENT PRIMARY KEY,

    user_name VARCHAR(100) NOT NULL,

    role ENUM('admin','user') DEFAULT 'user',

    ward_no INT NOT NULL,

    phone_no VARCHAR(15) UNIQUE,

    is_verified BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- =========================
-- USER LOGIN CREDENTIALS
-- =========================

CREATE TABLE credentials (

    credential_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,


    FOREIGN KEY(user_id)
    REFERENCES users(user_id)
    ON DELETE CASCADE
);



-- =========================
-- COMPLAINT CATEGORY
-- =========================

CREATE TABLE categories (

    category_id INT AUTO_INCREMENT PRIMARY KEY,

    category_name VARCHAR(100) NOT NULL,

    description TEXT
);



-- =========================
-- COMPLAINTS
-- =========================

CREATE TABLE complaints (

    complaint_id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,

    category_id INT NOT NULL,


    ward_no INT NOT NULL,


    title VARCHAR(255) NOT NULL,

    description TEXT NOT NULL,


    latitude DECIMAL(10,8),

    longitude DECIMAL(11,8),
	location_name VARCHAR(255),

    status ENUM(

        'Reported',

        'Viewed',

        'Under Review',

        'In Progress',

        'Resolved',

        'Rejected'

    )

    DEFAULT 'Reported',



    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP,



    FOREIGN KEY(user_id)
    REFERENCES users(user_id),



    FOREIGN KEY(category_id)
    REFERENCES categories(category_id)

);



-- =========================
-- COMPLAINT MULTIPLE IMAGES
-- =========================

CREATE TABLE complaint_images (


    image_id INT AUTO_INCREMENT PRIMARY KEY,


    complaint_id INT NOT NULL,


    image_url VARCHAR(500) NOT NULL,


    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



    FOREIGN KEY(complaint_id)

    REFERENCES complaints(complaint_id)

    ON DELETE CASCADE

);



-- =========================
-- STATUS HISTORY
-- =========================

CREATE TABLE complaint_status_history (


    history_id INT AUTO_INCREMENT PRIMARY KEY,


    complaint_id INT NOT NULL,


    old_status ENUM(

        'Reported',

        'Viewed',

        'Under Review',

        'In Progress',

        'Resolved',

        'Rejected'

    ),



    new_status ENUM(

        'Reported',

        'Viewed',

        'Under Review',

        'In Progress',

        'Resolved',

        'Rejected'

    ),



    ward_no INT,


    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



    FOREIGN KEY(complaint_id)

    REFERENCES complaints(complaint_id)

    ON DELETE CASCADE

);




-- =========================
-- NOTIFICATIONS
-- =========================

CREATE TABLE notifications (


    notification_id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,


    complaint_id INT NOT NULL,


    message TEXT NOT NULL,


    is_read BOOLEAN DEFAULT FALSE,


    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



    FOREIGN KEY(user_id)

    REFERENCES users(user_id),



    FOREIGN KEY(complaint_id)

    REFERENCES complaints(complaint_id)

    ON DELETE CASCADE

);




-- =========================
-- BUDGET ALLOCATION
-- =========================

CREATE TABLE budget_allocations (


    budget_id INT AUTO_INCREMENT PRIMARY KEY,


    complaint_id INT NOT NULL,


    estimated_cost DECIMAL(12,2) NOT NULL,


    approved_budget DECIMAL(12,2) DEFAULT 0,


    spend_budget DECIMAL(12,2) DEFAULT 0,



    budget_status ENUM(

        'Pending',

        'Approved',

        'In Progress',

        'Completed'

    )

    DEFAULT 'Pending',



    ward_no INT NOT NULL,


    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,



    FOREIGN KEY(complaint_id)

    REFERENCES complaints(complaint_id)

    ON DELETE CASCADE

);




-- =========================
-- CITIZENSHIP VERIFICATION
-- =========================

CREATE TABLE citizenship_verification (


    verification_id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,


    citizenship_number VARCHAR(50) UNIQUE NOT NULL,


    front_image_url VARCHAR(255) NOT NULL,


    back_image_url VARCHAR(255) NOT NULL,



    verification_status ENUM(

        'Pending',

        'Approved',

        'Rejected'

    )

    DEFAULT 'Pending',



    remarks TEXT,


    verified_by INT,


    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    verified_at TIMESTAMP NULL,



    FOREIGN KEY(user_id)

    REFERENCES users(user_id)

    ON DELETE CASCADE,



    FOREIGN KEY(verified_by)

    REFERENCES users(user_id)

);

CREATE TABLE pending_users (

    pending_id INT AUTO_INCREMENT PRIMARY KEY,

    full_name VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    phone_no VARCHAR(15) NOT NULL unique,

    password VARCHAR(255) NOT NULL,

    ward_no INT NOT NULL,

    otp VARCHAR(6) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    role VARCHAR(10),
	is_verified bool default 0
);


-- =========================
-- INDEXES FOR FAST SEARCH
-- =========================

CREATE INDEX idx_complaint_status
ON complaints(status);


CREATE INDEX idx_complaint_ward
ON complaints(ward_no);


CREATE INDEX idx_user_ward
ON users(ward_no);